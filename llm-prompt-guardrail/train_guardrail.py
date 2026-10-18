import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Load dataset
df = pd.read_csv("prompt_injection_dataset.csv")

# 2. Vectorize text with N-gram tokenization (unigrams + bigrams)
vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
X = vectorizer.fit_transform(df["prompt"])
y = df["label"]

# 3. Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# 4. Save model and vectorizer assets to disk
assets = {
    "model": model,
    "vectorizer": vectorizer
}

joblib.dump(assets, "guardrail_assets.pkl")
print("✅ Trained AI Security Guardrail and saved assets to 'guardrail_assets.pkl'.")