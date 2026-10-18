import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Load dataset
df = pd.read_csv("bug_reports.csv")

# 2. Extract features and target labels
X = df["description"]
y = df["severity"]

# 3. Convert text into numerical TF-IDF feature vectors
vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
X_tfidf = vectorizer.fit_transform(X)

# 4. Train Multinomial Naive Bayes Model
model = MultinomialNB(alpha=0.5)
model.fit(X_tfidf, y)

# 5. Evaluate training accuracy
train_acc = model.score(X_tfidf, y) * 100
print(f"[+] Model trained successfully! Training Accuracy: {train_acc:.2f}%")

# 6. Save model and vectorizer artifacts to disk
joblib.dump(model, "bug_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("[+] Saved 'bug_model.pkl' and 'tfidf_vectorizer.pkl'.")