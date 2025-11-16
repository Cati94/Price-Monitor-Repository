import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "email.json")


def load_email_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def send_email(subject, body):
    cfg = load_email_config()

    msg = MIMEMultipart()
    msg["From"] = cfg["sender"]
    msg["To"] = cfg["receiver"]
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(cfg["smtp"], cfg["port"]) as server:
        server.starttls()
        server.login(cfg["sender"], cfg["password"])
        server.send_message(msg)