import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.mailfence.com"  # Or any SMTP server (e.g., SendGrid, etc.)
SMTP_PORT = 465
SMTP_USERNAME = "prove23t@mailfence.com"
SMTP_PASSWORD = "HelloWorld321!"

def send_email(recipient: str, subject: str, content: str):
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(content, 'plain'))

        # Create SMTP session for sending the mail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SMTP_USERNAME, recipient, text)
        server.quit()
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")
