# 🛍️ Amazon Product Review Sentiment Analysis

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to analyze Amazon product reviews and predict whether a review is **Positive** or **Negative**. The model is trained on real Amazon user feedback and deployed using **Streamlit** as a live web application.

---
## 🌐 Live Demo

Try the live Streamlit app 👉  
🔗 [Sentiment Analysis App](https://sentimentanalyzeronappuctreview-giqxozqk9nkln8u3jy2ejq.streamlit.app/)


## 📌 Project Highlights

- ✅ **Binary Sentiment Classification** (Positive vs. Negative)
- ✅ **Text cleaning**, preprocessing, and vectorization using **TF-IDF**
- ✅ **Class imbalance handled** via upsampling (resample technique)
- ✅ Trained using **Multinomial Naive Bayes**
- ✅ Achieved **96% accuracy** with balanced precision/recall
- ✅ **Interactive Streamlit app** for real-time predictions

---

## 🧠 Tools & Technologies

| Category       | Tools Used                          |
|----------------|-------------------------------------|
| Programming    | Python                              |
| NLP            | NLTK, TextBlob, TF-IDF              |
| ML Models      | Multinomial Naive Bayes             |
| Preprocessing  | Regex, Pandas                       |
| Deployment     | Streamlit                           |
| Visualization  | Seaborn, Matplotlib                 |
| Model Storage  | Joblib                              |

---

## 📂 Dataset Description

The dataset contains Amazon product reviews including:
- `reviewText`: The full customer review
- `overall`: Star rating (not used in model)
- `reviewTime`: Date of review (2014–2015)
- `helpful_yes`, `helpful_no`: Helpfulness votes

> Reviews were labeled using **TextBlob polarity**:
> - Positive (polarity > 0)
> - Negative (polarity < 0)
> - Neutral (polarity = 0) — excluded from final model

---

## ⚖️ Class Balancing

The dataset was **imbalanced**, with far more Positive than Negative reviews.

To address this:
- Negative reviews were **upsampled** using `sklearn.utils.resample` to match the number of Positive samples
- Result: a **balanced training dataset** leading to much better model performance

---

## 📊 Model Performance

After training and evaluation:
Accuracy: 96%
F1-Score: 0.96 (Positive), 0.96 (Negative)
Precision/Recall: Balanced and reliable

## 🚀 Streamlit App

A web application was built using **Streamlit** for real-time sentiment prediction.

### 🔧 How to Run:

1. Clone the repo  
2. Install requirements  
3. Launch the app

## 🖼️ Screenshots
<img width="1017" height="695" alt="image" src="https://github.com/user-attachments/assets/ab341ca1-7b70-4937-b29c-3812bf48c591" />
<img width="965" height="695" alt="image" src="https://github.com/user-attachments/assets/8546c6b3-d007-451d-a90d-2fbbd7ec4355" />


```bash
pip install -r requirements.txt
streamlit run streamlit_app.py

📁 Project Structure
bash
Copy
Edit
📦 Sentiment Analysis/
│
├── sentiment_model.pkl          # Trained Naive Bayes model
├── tfidf_vectorizer.pkl         # TF-IDF Vectorizer
├── label_encoder.pkl            # Label encoder for sentiment
├── streamlit_app.py             # Streamlit app file
├── amazon.csv                   # Dataset
├── README.md                    # This file
└── requirements.txt             # Python dependencies


| Review Text                                            | Prediction |
| ------------------------------------------------------ | ---------- |
| "Absolutely love this product. Exceeded expectations!" | ✅ Positive |
| "It broke after one use. Waste of money."              | ❌ Negative |

🧑‍💻 Author
Vishal Maheshwary
📍 Data Analyst | Aspiring Data Scientist

💡 Future Work
Add Neutral class with better separation (using BERT or transformer-based model)

Explore other models like Logistic Regression, Random Forest

Deploy to Heroku or HuggingFace Spaces

⭐️ Give a Star!
If you find this project useful, consider ⭐️ starring the repo — it helps others find it too!
