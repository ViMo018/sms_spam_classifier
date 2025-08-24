# 📩 SMS Spam Classifier

A **smart SMS spam detection system** built using **Python**, **TF-IDF**, and **Naive Bayes classifiers**.  
Trained on the **Kaggle SMS Spam Collection dataset**, it efficiently classifies messages as **spam** or **ham**.  

---

## 🔹 Features & Workflow

- **Data Cleaning & EDA** – Explored and preprocessed text messages.  
- **Text Preprocessing** – Tokenization, lowercasing, and TF-IDF vectorization.  
- **Modeling** – Tried multiple Naive Bayes algorithms:
  - **Multinomial NB (MNB)** – *Best performance*  
  - **Bernoulli NB (BNB)** – Excellent precision  
  - **Gaussian NB (GNB)** – Baseline comparison  
- **Evaluation** – Metrics include accuracy, precision, and confusion matrix.  
- **UI/UX Design** – Built an interactive interface using **Streamlit**, aided by ChatGPT.  
- **Deployment** – Fully deployable web app on **Streamlit Cloud**.  

---

## 🧪 Model Performance

| **Model** | **Accuracy** | **Precision** |
|-----------|--------------|---------------|
| **GNB**   | 87.6%        | 0.52          |
| **MNB**   | 97.2%        | 1.0 ✅        |
| **BNB**   | 97.1%        | 0.97          |

> **Multinomial NB** achieved the best results and is used in the deployed app.  

---

## 💻 Tech Stack

- **Python**, **Pandas**, **NumPy**  
- **scikit-learn** (TF-IDF, Naive Bayes)  
- **Streamlit** (Web UI/UX)  
- **Kaggle SMS Spam Dataset**  

---

## ⚡ Try it Online

Experience the live app: [https://spam-detection-vimo.streamlit.app/](#)  

---


