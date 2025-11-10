import os
import pandas as pd
import joblib
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.join(BASE, "models")

# Load ML assets
def load(path):
    full = os.path.join(MODELS, path)
    if not os.path.exists(full):
        raise FileNotFoundError(f"Missing: {full}")
    return joblib.load(full)

model = load("fraud_model.pkl")
scaler = load("fraud_scaler.pkl")
features = load("fraud_features.pkl")

LAST_RESULTS = None   # Stores last processed dataframe


# BLOG ARTICLES (FINAL LIST — ALL 8 ITEMS)
BLOG_ARTICLES = [
    {
        "slug": "ai-in-banking-fraud-detection",
        "title": "AI in Banking Fraud Detection",
        "overview": "How AI/ML models reduce fraud losses in modern banking via anomaly detection and predictive scoring.",
        "external_url": "https://www.ijfmr.com/papers/2024/6/31034.pdf",
        "image": "img/blog/bank-ai.jpg",
    },
    {
        "slug": "ecommerce-fraud-case-studies",
        "title": "E-Commerce Fraud Case Studies",
        "overview": "Real-world fraud patterns across online marketplaces and how companies fight back.",
        "external_url": "https://investissue.com/ecommerce-frauds-case-study/",
        "image": "img/blog/ecommerce-fraud.jpg",
    },
    {
        "slug": "top-5-tips-to-prevent-online-fraud",
        "title": "Top 5 Tips to Prevent Online Fraud",
        "overview": "Simple steps individuals and companies can take to reduce phishing and scam risks.",
        "external_url": "https://whitehatrecoverie.com/blog/ways-to-avoid-online-scams/",
        "image": "img/blog/online-safety.jpg",
    },
    {
        "slug": "mastercard-tackles-fraud-and-productivity",
        "title": "Mastercard Tackles Fraud and Productivity",
        "overview": "How Mastercard applies enterprise AI to fight payment fraud and improve efficiency.",
        "external_url": "https://www.futuriom.com/articles/news/enterprise-ai-profile-mastercard-test/2025/11",
        "image": "img/blog/mastercard-ai.jpg",
    },
    {
        "slug": "what-is-fraud-detection-ibm",
        "title": "What Is Fraud Detection? — IBM",
        "overview": "A deep look into how fraud systems work and what modern AI brings to the table.",
        "external_url": "https://www.ibm.com/think/topics/fraud-detection",
        "image": "img/blog/ibm-fraud.jpg",
    },
    {
        "slug": "modernizing-financial-systems-and-fraud-prevention",
        "title": "Modernizing Financial Systems & Fraud Prevention",
        "overview": "Strategies for transforming legacy systems with AI-powered fraud monitoring.",
        "external_url": "https://finovate.com/modernizing-financial-systems-a-strategic-approach-to-legacy-transformation-and-fraud-prevention/",
        "image": "img/blog/fintech-modern.jpg",
    },
    {
        "slug": "what-is-fraud-detection-and-why-needed",
        "title": "What is Fraud Detection & Why Is It Needed?",
        "overview": "A complete guide to fraud detection fundamentals and system workflows.",
        "external_url": "https://www.fraud.com/post/fraud-detection",
        "image": "img/blog/fraud-basics.jpg",
    },
    {
        "slug": "fraud-detection-using-machine-learning-stanford",
        "title": "Fraud Detection using Machine Learning — Stanford",
        "overview": "Stanford CS229 research comparing ML algorithms for large-scale fraud classification.",
        "external_url": "https://cs229.stanford.edu/proj2018/report/261.pdf",
        "image": "img/blog/ml-research.jpg",
    },
]


def get_article(slug):
    for a in BLOG_ARTICLES:
        if a["slug"] == slug:
            return a
    return None


# ROUTES

@app.route("/")
def index():
    return render_template("index.html")


# Manual Form Checker
@app.route("/checker", methods=["GET", "POST"])
def checker():
    global LAST_RESULTS

    if request.method == "POST":
        row = {f: float(request.form.get(f, 0) or 0) for f in features}
        X = pd.DataFrame([row])
        Xs = scaler.transform(X)

        pred = model.predict(Xs).astype(int)
        risk = model.predict_proba(Xs)[:, 1] * 100

        LAST_RESULTS = pd.DataFrame({
            "prediction": pred,
            "risk": risk.round(2)
        })

        return redirect(url_for("analytics"))

    return render_template("checker.html", features=features)


# ---------- CSV Upload ----------
@app.route("/upload_csv", methods=["POST"])
def upload_csv():
    global LAST_RESULTS

    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded."}), 400

    df = pd.read_csv(file)

    missing = [c for c in features if c not in df.columns]
    if missing:
        return jsonify({"error": f"Dataset missing required columns: {missing}"}), 400

    Xs = scaler.transform(df[features])
    df["prediction"] = model.predict(Xs).astype(int)
    df["risk"] = model.predict_proba(Xs)[:, 1] * 100

    LAST_RESULTS = df

    return jsonify({
        "ok": True,
        "total": len(df),
        "fraud_count": int((df["prediction"] == 1).sum()),
        "fraud_rate": round(df["prediction"].mean() * 100, 2),
        "download_link": "/static/results/latest_results.csv"
    })


#  Fix: alias route for frontend compatibility
@app.route("/upload", methods=["POST"])
def upload_alias():
    return upload_csv()


# Analytics 
@app.route("/analytics")
def analytics():
    global LAST_RESULTS

    if LAST_RESULTS is None or LAST_RESULTS.empty:
        return render_template("analytics.html", no_data=True)

    df = LAST_RESULTS.copy()

    total = len(df)
    fraud = int((df["prediction"] == 1).sum())
    legit = total - fraud
    avg_risk = float(df["risk"].mean().round(2))

    region_counts = df["region"].value_counts().to_dict() if "region" in df.columns else {}

    records = df[["prediction", "risk"]].to_dict(orient="records")

    return render_template(
        "analytics.html",
        no_data=False,
        total=total,
        fraud=fraud,
        legit=legit,
        avg_risk=avg_risk,
        region_counts=region_counts,
        records=records
    )


# Resources 
@app.route("/resources")
def resources():
    return render_template("resources.html")


# Blog 
@app.route("/blog")
def blog():
    return render_template("blog.html", articles=BLOG_ARTICLES)


@app.route("/blog/<slug>")
def blog_post(slug):
    article = get_article(slug)
    if not article:
        abort(404)
    return render_template("blog_post.html", article=article)


# Run App
if __name__ == "__main__":
    app.run(debug=True)

