
#dekh bhai ye wala code mene nhi likha itna sab likne me mujhe aalas aata hai
#isliye chatgpt se likhwa raha hun normal wala toh me likh sakta hun hu lekin ye colorfull
#mere se nhi hona


# app_streamlit_colored.py

import pickle
import streamlit as st

# ---------------- Load model & vectorizer ----------------
model = pickle.load(open("model3.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer3.pkl", "rb"))

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Spam Classifier",
    page_icon="✉️",
    layout="centered"
)

# ---------------- Custom CSS for colors ----------------
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color:white;
        height: 3em;
        width: 10em;
        font-size:16px;
    }
    .stTextArea textarea {
        background-color: #ffffe0;
        color: #000000;
        font-size:16px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Title & Description ----------------
st.markdown("<h1 style='text-align:center;color:#ff4500;'>Spam Message Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#555555;'>Type your message below and find out if it's SPAM or HAM!</p>", unsafe_allow_html=True)

# ---------------- Input ----------------
msg = st.text_area("Enter your message:", height=120)

# ---------------- Prediction ----------------
if st.button("Predict"):
    if msg.strip() == "":
        st.warning("⚠️ Please enter a message!")
    else:
        msg_vec = vectorizer.transform([msg])
        pred = model.predict(msg_vec)[0]
        if pred == 1:
            st.markdown("<h2 style='color:red;'>Prediction: SPAM ✋</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color:green;'>Prediction: HAM ✅</h2>", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("<p style='text-align:center;color:#888888;font-size:12px;'>Built with ❤️ using Streamlit & Python</p>", unsafe_allow_html=True)

