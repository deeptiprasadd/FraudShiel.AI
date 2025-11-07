document.addEventListener("DOMContentLoaded", function () {
  // Fraud Trend Line Chart
  const ctxTrend = document.getElementById("fraudTrendChart");
  if (ctxTrend) {
    new Chart(ctxTrend, {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
          label: "Detected Frauds",
          data: [120, 180, 160, 220, 190, 260],
          borderColor: "#00b4d8",
          backgroundColor: "rgba(0,180,216,0.2)",
          tension: 0.4,
          fill: true,
        }],
      },
      options: {
        plugins: { legend: { display: false } },
        scales: {
          x: { ticks: { color: "#fff" } },
          y: { ticks: { color: "#fff" } },
        },
      },
    });
  }

  // Fraud Cases by Region (Bar Chart)
  const ctxRegion = document.getElementById("fraudRegionChart");
  if (ctxRegion) {
    new Chart(ctxRegion, {
      type: "bar",
      data: {
        labels: ["Asia", "Europe", "US", "Africa", "Australia"],
        datasets: [{
          data: [350, 280, 190, 100, 70],
          backgroundColor: ["#00b4d8", "#90e0ef", "#0077b6", "#48cae4", "#0096c7"],
        }],
      },
      options: {
        plugins: { legend: { display: false } },
        scales: {
          x: { ticks: { color: "#fff" } },
          y: { ticks: { color: "#fff" } },
        },
      },
    });
  }

  // Fraud Ratio (Doughnut)
  const ctxRatio = document.getElementById("fraudRatioChart");
  if (ctxRatio) {
    new Chart(ctxRatio, {
      type: "doughnut",
      data: {
        labels: ["Legit", "Fraudulent"],
        datasets: [{
          data: [78, 22],
          backgroundColor: ["#00ff88", "#ff4d4d"],
          borderWidth: 0,
        }],
      },
      options: {
        plugins: { legend: { labels: { color: "#fff" } } },
      },
    });
  }

  // Risk Score Distribution (Radar Chart)
  const ctxRisk = document.getElementById("riskScoreChart");
  if (ctxRisk) {
    new Chart(ctxRisk, {
      type: "radar",
      data: {
        labels: ["Payment", "Login", "Refund", "Purchase", "Transfer"],
        datasets: [{
          label: "Average Risk Score",
          data: [0.7, 0.8, 0.6, 0.9, 0.75],
          backgroundColor: "rgba(255, 215, 0, 0.2)",
          borderColor: "#ffd60a",
          pointBackgroundColor: "#ffd60a",
          borderWidth: 2,
        }],
      },
      options: {
        scales: { r: { angleLines: { color: "#333" }, pointLabels: { color: "#fff" } } },
        plugins: { legend: { labels: { color: "#fff" } } },
      },
    });
  }
});
