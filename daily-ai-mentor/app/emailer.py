import os
import smtplib

from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


def send_email(
    subject: str,
    body: str,
    attachment_path: Path
):

    sender = os.getenv("GMAIL_SENDER")
    password = os.getenv("GMAIL_APP_PASSWORD")
    receiver = os.getenv("GMAIL_RECEIVER")

    if not sender:
        raise ValueError("GMAIL_SENDER not found")

    if not password:
        raise ValueError("GMAIL_APP_PASSWORD not found")

    if not receiver:
        raise ValueError("GMAIL_RECEIVER not found")

    message = EmailMessage()

    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    message.set_content(body)

    with open(attachment_path, "rb") as file:

        pdf_data = file.read()

    message.add_attachment(
        pdf_data,
        maintype="application",
        subtype="pdf",
        filename=attachment_path.name
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender,
            password
        )

        smtp.send_message(message)