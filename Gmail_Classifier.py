import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
import joblib

# Load trained model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def classify_email(email_text):
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)[0]
    return "PHISHING/SPAM" if prediction == 1 else "SAFE"

EMAIL_ADDRESS = " " #Enter your Email
EMAIL_PASSWORD = " " #Enter your generated password

mail_server = imaplib.IMAP4_SSL("imap.gmail.com")
mail_server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
mail_server.select("inbox")

status, data = mail_server.search(None, "ALL")
email_id_list = data[0].split()
print(f"Found {len(email_id_list)} emails.\n")

for email_id in email_id_list[-5:]:
    status, message_data = mail_server.fetch(email_id, "(RFC822)")
    raw_email = email.message_from_bytes(message_data[0][1])
    raw_subject, encoding = decode_header(raw_email["Subject"])[0]
    subject = raw_subject.decode(encoding or "utf-8", errors="ignore") if isinstance(raw_subject, bytes) else raw_subject

    sender = raw_email.get("From")

    # Extract email body
    email_body = ""
    if raw_email.is_multipart():
        for part in raw_email.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if content_type == "text/plain" and "attachment" not in content_disposition:
                email_body = part.get_payload(decode=True).decode(errors="ignore")
                break
            elif content_type == "text/html":
                html_content = part.get_payload(decode=True).decode(errors="ignore")
                email_body = BeautifulSoup(html_content, "html.parser").get_text()
                break
    else:
        email_body = raw_email.get_payload(decode=True).decode(errors="ignore")

    combined_text = f"{subject}\n{email_body}"
    prediction = classify_email(combined_text)


    print(f"From: {sender}")
    print(f"Subject: {subject}")
    print(f"Prediction: {prediction}")
    print("=" * 60)

mail_server.logout()
