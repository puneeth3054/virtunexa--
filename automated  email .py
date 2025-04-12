import smtplib
import pandas as pd
import os
from email.message import EmailMessage

# SMTP Server Details (Update with your email credentials)
SMTP_SERVER = "smtp.gmail.com"  # For Gmail (change if using another provider)
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your_app_password"  # Use an App Password if 2FA is enabled

# Load contacts from CSV (Format: Name, Email)
CSV_FILE = "contacts.csv"
contacts = pd.read_csv(CSV_FILE)

# Email Subject & Body Template
SUBJECT = "Your Personalized Email"
BODY_TEMPLATE = """Hello {name},

This is an automated email sent using Python.

Best regards,
Your Name
"""

# Attachment File (optional)
ATTACHMENT_PATH = "sample.pdf"  # Change this to your actual file path

def send_email(to_email, name):
    """Sends an email with an attachment."""
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = SUBJECT
        msg.set_content(BODY_TEMPLATE.format(name=name))

        # Attach File
        if os.path.exists(ATTACHMENT_PATH):
            with open(ATTACHMENT_PATH, "rb") as file:
                msg.add_attachment(file.read(), maintype="application", subtype="octet-stream", filename=os.path.basename(ATTACHMENT_PATH))

        # Connect to SMTP Server & Send Email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure Connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email sent to {name} ({to_email}) ✅")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Loop through contacts & send emails
for _, row in contacts.iterrows():
    send_email(row["Email"], row["Name"])
