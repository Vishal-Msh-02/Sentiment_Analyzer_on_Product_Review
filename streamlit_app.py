import streamlit as st
import joblib
import re

# Load files
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Text cleaning function
def clean_review(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Streamlit UI
st.set_page_config(page_title="Sentiment Analyzer", page_icon="🧠")
st.title("📦 Product Review Sentiment Analyzer")
st.write("Type a review and see if it's Positive, Negative, or Neutral!")

user_input = st.text_area("📝 Enter your review:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review first.")
    else:
        cleaned = clean_review(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]
        sentiment = label_encoder.inverse_transform([prediction])[0]

        # Show result
        st.subheader("🔍 Sentiment:")
        if sentiment == "Positive":
            st.success("This review is Positive 😄")
        elif sentiment == "Negative":
            st.error("This review is Negative 😠")
        else:
            st.info("This review is Neutral 😐")
