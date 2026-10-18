import streamlit as st
import joblib

st.set_page_config(page_title="Bug Severity Classifier", page_icon="🐛", layout="centered")

st.title("📁 Software Bug & Defect Classifier")
st.write("Upload a code snippet, stack trace, or log file to analyze its defect severity.")

# 1. Load trained model and vectorizer from disk
@st.cache_resource
def load_assets():
    model = joblib.load("bug_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_assets()

# 2. File uploader widget
uploaded_file = st.file_uploader(
    "Upload a code file (.py, .js, .java) or log file (.txt, .log):",
    type=["py", "js", "java", "txt", "log"]
)

if uploaded_file is not None:
    # Read file contents as text string
    file_text = uploaded_file.getvalue().decode("utf-8")
    
    # Display file contents preview
    with st.expander("📄 View Uploaded File Contents"):
        st.code(file_text)

    if st.button("Scan File for Bugs"):
        # 3. Transform text using vectorizer and predict severity
        vectorized_text = vectorizer.transform([file_text])
        prediction = model.predict(vectorized_text)[0]
        probs = model.predict_proba(vectorized_text)[0]
        confidence = max(probs) * 100

        st.divider()
        st.subheader("Triage Results")

        color_map = {
            "Low": "🟢 LOW",
            "Medium": "🟡 MEDIUM",
            "High": "🟠 HIGH",
            "Critical": "🔴 CRITICAL"
        }

        col1, col2 = st.columns(2)
        col1.metric("Predicted Severity", color_map.get(prediction, prediction))
        col2.metric("Confidence Score", f"{confidence:.1f}%")

        if prediction in ["High", "Critical"]:
            st.error(f"🚨 **High Risk Issue Detected** ({prediction}). Priority fix required!")
        else:
            st.success(f"✅ **Clean / Low Risk Ticket**: Categorized as {prediction} priority.")