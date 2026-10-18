# Intelligent Systems, Machine Learning & AI Security Projects

A collection of end-to-end machine learning, time-series analytics, and AI security applications built using Python, Scikit-Learn, PyTorch, and Streamlit.

---

## 📁 Repository Projects

### 1.  [LLM Prompt Injection Guardrail](./llm-prompt-guardrail)
* **Description:** A low-latency (< 10 ms) AI security firewall that intercepts incoming user prompts in real time to detect and block prompt injection attacks, system overrides, and jailbreak attempts before reaching downstream LLMs.
* **Key Features:** $N$-gram feature extraction ($1$-grams and $2$-grams), TF-IDF term weighting, Logistic Regression risk scoring, and interactive Streamlit security dashboard.
* **Tech Stack:** Python, Scikit-Learn, Streamlit, Joblib.

### 2. [Hourly Server Energy & Power Surge Forecaster](./server-energy-forecaster)
* **Description:** An infrastructure monitoring tool that forecasts 24-hour server electrical wattage load and isolates anomalous hardware power surges.
* **Key Features:** Lag feature engineering ($\text{Lag}_1$, $\text{Lag}_{24}$, 6-hour rolling averages), Random Forest Regressor, and a statistical residual anomaly engine ($\mu + 2.5\sigma$) rendered on interactive Plotly charts.
* **Tech Stack:** Python, Pandas, Scikit-Learn, Plotly, Streamlit.

### 3.  [Software Bug & Defect Severity Classifier](./bug-severity-classifier)
* **Description:** An automated NLP triage system that classifies software defect reports and stack traces into four priority tiers (Low, Medium, High, Critical).
* **Key Features:** Text pre-processing, TF-IDF vectorization targeting critical stack trace tokens (`NullPointerException`, `Fatal Crash`, `Memory Leak`), and confidence score reporting.
* **Tech Stack:** Python, Scikit-Learn, Pandas, Streamlit.

---

## Getting Started

### Prerequisites
* Python 3.9+
* Git

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/syedsibtulhasan/Intelligent-systems-projects.git](https://github.com/syedsibtulhasan/Intelligent-systems-projects.git)
   cd Intelligent-systems-projects