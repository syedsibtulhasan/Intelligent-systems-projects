import streamlit as st
import joblib

st.set_page_config(page_title="AI Security Guardrail", page_icon="🛡️", layout="centered")

st.title("🛡️ LLM Prompt Injection Guardrail")
st.write("An AI security firewall that inspects incoming user prompts in real-time to intercept jailbreak attacks, system overrides, and prompt injection attempts.")

# Load saved guardrail assets
@st.cache_resource
def load_assets():
    return joblib.load("guardrail_assets.pkl")

assets = load_assets()
model = assets["model"]
vectorizer = assets["vectorizer"]

# Interactive input text area
user_input = st.text_area(
    "Enter Prompt to Inspect:",
    placeholder="e.g., Summarize this report OR Ignore all previous instructions...",
    height=130
)

if st.button("Inspect Prompt"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt to analyze.")
    else:
        # 1. Vectorize the input prompt
        X_input = vectorizer.transform([user_input])
        
        # 2. Compute prediction probability
        prediction = model.predict(X_input)[0]
        prob = model.predict_proba(X_input)[0]
        threat_score = prob[1] * 100

        st.divider()

        # 3. Display Security Verdict
        if prediction == 1:
            st.error(f"🚨 **PROMPT INJECTION ATTACK BLOCKED!** (Threat Risk Score: {threat_score:.1f}%)")
            st.warning("⚠️ **Security Action:** Request dropped. Threat logged to security incident monitoring system.")
        else:
            st.success(f"🟢 **PROMPT CLEARED (SAFE)** (Threat Risk Score: {threat_score:.1f}%)")
            st.info("✅ **Action:** Prompt forwarded safely to downstream LLM execution engine.")