# 📧 Phishing Email Detection using Machine Learning

This project uses Natural Language Processing (NLP) and Machine Learning to detect phishing or spam emails. The model is trained on labeled email datasets and can connect to your Gmail inbox to classify real emails as **SAFE** or **PHISHING/SPAM** using the IMAP protocol.

---

## 📁 Project Structure

```text
Phishing-Email-Detection/
├── dataset/                # Folder containing training CSV files
├── model_train.py          # Script to train and save the model
├── gmail_classifier.py     # Script to classify Gmail emails using the trained model
├── phishing_model.pkl      # (Generated after training - not included)
├── vectorizer.pkl          # (Generated after training - not included)
├── requirements.txt        # Dependencies
└── README.md               # You're reading it!
```

## 🚀 How It Works

1. **Training the Model (`model_train.py`)**:
    - Loads all CSVs from the `dataset/` folder.
    - Cleans and vectorizes email text using `TfidfVectorizer`.
    - Trains a `MultinomialNB` classifier.
    - Saves the model to `phishing_model.pkl` and the vectorizer to `vectorizer.pkl`.

2. **Classifying Real Emails (`gmail_classifier.py`)**:
    - Connects to your Gmail inbox via **IMAP**.
    - Fetches the latest emails.
    - Applies the model to classify them as **PHISHING/SPAM** or **SAFE**.
    - Prints the sender, subject, and prediction.

---

## 🛠️ Installation

1. Clone the repo:
```bash
git clone https://github.com/Vink0217/Phishing-Email-Detection.git
cd Phishing-Email-Detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train the Model
```bash
python model_train.py
```
This will create:

1. Phishing_model.pkl — your trained model

2. Vectorizer.pkl — the TF-IDF vectorizer

## 🔒 Gmail Setup for IMAP
**To use Gmail classification:**

Make sure IMAP is enabled in Gmail settings
Use an App Password if you have 2-Step Verification enabled
Replace your credentials in gmail_classifier.py:
```bash
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
```

## 📬 Classify Your Gmail Emails
```bash
python gmail_classifier.py
```

## ⚠️ Disclaimer
For educational/research purposes only.

Never expose your real passwords in source files.

Always use App Passwords and environment variables for security.

## 🧠 Future Ideas
Export results to CSV

Automatically move phishing emails to spam

Add web dashboard to monitor predictions


