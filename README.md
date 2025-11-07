# FraudShield.AI — AI-Powered Fraud Detection Platform

Live Demo: https://fraudshiel-ai.onrender.com

A complete real-time fraud detection web platform powered by Machine Learning, built with Flask, Chart.js, and a fully responsive UI.

FraudShield.AI helps users detect fraudulent transactions using manual inputs or CSV datasets, visualize analytics, and learn from curated fraud-research articles.

## Features at a Glance

- Real-time Fraud Prediction
- CSV Dataset Upload & Batch Processing
- Interactive Analytics Dashboard
- Modern Neural-Network Hero Animation
- Fraud Detection Blog Section
- Downloadable Results
- Clean Bootstrap UI
- Fully Deployable on Render

## 1. Website Overview

The website contains the following main sections:

- **Home** — Overview of the platform
- **Fraud Checker** — Manual input fraud prediction
- **Resources** — Download/demo datasets & CSV analyzer
- **Blog** — 8 curated fraud-research articles
- **Analytics** — Visualization dashboard for predictions

## 2. Fraud Checker (Manual Mode)

### Step 1: Open Fraud Checker

Navigate to:
```
Fraud Checker → Manual Form
```

### Step 2: Enter Feature Values

Enter values for all model features (empty fields default to 0).

### Step 3: Predict Fraud

Click **Predict Fraud** to generate:

- Fraud/Legit result
- Risk Probability (%)
- Stored results for analytics

You are automatically redirected to the Analytics page.

## 3. Fraud Checker (CSV Upload Mode)

### Step 1: Go to Resources

Navigate:
```
Resources → Test This Dataset
```

### Step 2: Choose or Upload Dataset

Supported: `.csv`

### Step 3: System Processing

Backend:

- Validates missing columns
- Scales input using trained scaler
- Generates prediction for every row
- Computes:
  - Total transactions
  - Fraud count
  - Fraud percentage
- Provides download link for results

### Step 4: View Results

Summary appears on the same page.

## 4. Analytics Dashboard

After running any prediction, the dashboard shows:

### Metrics

- Total Records
- Fraudulent Transactions
- Legit Transactions
- Average Risk Score

### Charts (Chart.js)

- Fraud Detection Trend
- Fraud by Region
- Fraud vs Legit (Pie Chart)
- Risk Score Distribution

## 5. Blog Section

### Step 1: Open Blog

Navigate: **Blog**

You will see all 8 articles, each with:

- Title
- Image
- Overview
- Read Overview → Button

### Step 2: Article Page

Displays:

- Header Image
- Overview Text
- "Open Full Article" (external link)

## 6. Resources Section

Includes:

- Downloadable datasets
- Test-this-dataset tools
- External ML guides
- Learning material for fraud detection

## 7. Workflow Diagram
```
[index.html]
      │
      ▼
[checker.html]
   ├── Manual Input → checker()
   └── CSV Upload → upload_csv()
      │
      ▼
backend (app.py)
   → load(model/scaler/features)
   → Predict Fraud
   → Save to LAST_RESULTS
      │
      ▼
[analytics.html]
   → Chart.js visualizations
   → Statistics summary
```

## 8. Function Descriptions

### load(path)

Loads model, scaler, and feature list. Ensures files exist.

### checker()

Processes manual form submission:

- Converts features
- Scales
- Predicts fraud
- Stores results
- Redirects to analytics dashboard

### upload_csv()

Processes CSV uploads:

- Validates feature columns
- Runs predictions for entire dataset
- Returns JSON summary
- Generates downloadable CSV

### analytics()

Reads LAST_RESULTS and sends:

- totals
- region counts
- risk values
- predictions

into analytics.html for visualization.

### blog()

Displays all defined blog articles.

### blog_post(slug)

Shows selected article page.

## 9. Project Structure
```
FraudShield.AI/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── models/
│     ├── fraud_model.pkl
│     ├── fraud_scaler.pkl
│     └── fraud_features.pkl
│
├── static/
│     ├── css/
│     ├── js/
│     ├── img/blog/
│     ├── datasets/
│     └── results/
│
└── templates/
      ├── base.html
      ├── index.html
      ├── checker.html
      ├── analytics.html
      ├── resources.html
      ├── blog.html
      └── blog_post.html
```

## 10. Deployment (Render)

This project runs on Render using:

- Flask
- Gunicorn
- Procfile
- Auto-deploy from GitHub

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/fraudshield-ai.git

# Navigate to project directory
cd fraudshield-ai

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Visualization**: Chart.js
- **Machine Learning**: scikit-learn
- **Deployment**: Render

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
