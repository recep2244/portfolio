#!/usr/bin/env python3
import argparse
import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def load_recipients(path):
    emails = []
    seen = set()
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "email" not in reader.fieldnames:
            raise ValueError("preview_subscribers.csv must have an email column")
        for row in reader:
            email = (row.get("email") or "").strip()
            status = (row.get("status") or "").strip().lower()
            if not email:
                continue
            if status in {"unsubscribed", "inactive", "bounced"}:
                continue
            if email in seen:
                continue
            seen.add(email)
            emails.append(email)
    return emails


def build_message(subject, from_email, to_email, body_text):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.attach(MIMEText(body_text, "plain", "utf-8"))
    return msg


def main():
    parser = argparse.ArgumentParser(description="Send a curation reminder email")
    parser.add_argument("--preview-list", default="preview_subscribers.csv")
    parser.add_argument("--from-email", default=os.getenv("NEWSLETTER_FROM_EMAIL"))
    parser.add_argument("--smtp-user", default=os.getenv("NEWSLETTER_GMAIL_USER"))
    parser.add_argument("--smtp-pass", default=os.getenv("NEWSLETTER_GMAIL_APP_PASSWORD"))
    parser.add_argument("--subject", default="Protein Design Digest: curation ready")
    parser.add_argument("--body", default="Your daily curation is ready. Open http://127.0.0.1:5050 to curate and approve.")
    args = parser.parse_args()

    from_email = args.from_email or args.smtp_user
    if not from_email:
        raise ValueError("from email is required (NEWSLETTER_FROM_EMAIL or NEWSLETTER_GMAIL_USER)")
    if not args.smtp_user or not args.smtp_pass:
        raise ValueError("SMTP credentials missing (NEWSLETTER_GMAIL_USER and NEWSLETTER_GMAIL_APP_PASSWORD)")

    recipients = load_recipients(args.preview_list)
    if not recipients:
        raise ValueError("No preview recipients found")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(args.smtp_user, args.smtp_pass)
        for email in recipients:
            msg = build_message(args.subject, from_email, email, args.body)
            smtp.sendmail(from_email, [email], msg.as_string())

    print(f"Reminder sent to {len(recipients)} recipients")


if __name__ == "__main__":
    main()
