import streamlit as st
import pickle

# Load saved models
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("models/logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔍 AI Resume Screening System")
resume = st.text_area("📄 Paste Resume")
job = st.text_area("🧾 Paste Job Description")

if st.button("🎯 Match"):
    if resume and job:
        text = resume + " [SEP] " + job
        vec = vectorizer.transform([text])
        prob = model.predict_proba(vec)[0][1]
        st.success(f"✅ Match Score: {prob:.2f}")
    else:
        st.warning("Please fill both fields")
