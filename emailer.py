import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

def send_match_email(to_email, match_results, sender_email, sender_password):
    subject = "TalentMatch: CV Match Results"
    body = "Here are your CV match results:\n\n"

    for i, result in enumerate(match_results, 1):
        body += f"{i}. Match Score: {result['similarity']}%\n"
        body += f"   Missing Skills: {', '.join(result['missing_skills']) or 'None'}\n\n"

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

# Test için sadece bu kısım çalışır
if __name__ == "__main__":
    load_dotenv()  # .env dosyasını yükle

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    dummy_results = [
        {"similarity": 85.3, "missing_skills": ["Docker"]},
        {"similarity": 79.1, "missing_skills": ["TensorFlow", "FastAPI"]}
    ]

    send_match_email(
        to_email="ndemir22@posta.pau.edu.tr", 
        match_results=dummy_results,
        sender_email=sender_email,
        sender_password=sender_password
    )
