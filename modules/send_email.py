
from  . import gmail_auth
from email.mime.text import MIMEText
import base64


def create_message(to, subject, body):
    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}


def send_email(recipient_name, recipient_email, subject, body):
    try:
        service = gmail_auth.gmail_login()
        message = create_message(recipient_email, subject, body)
        send = service.users().messages().send(userId="me", body=message).execute()
        return True
    except Exception as e:
        print("Error:", e)
        return False