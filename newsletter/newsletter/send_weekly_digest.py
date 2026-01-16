#!/usr/bin/env python3
import argparse
import html
import json
import os
import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from zoneinfo import ZoneInfo

from generate_weekly_digest import generate_digest_md, load_issue
from send_newsletter import build_message, chunk_list, load_subscribers


def get_week_range(today):
    weekday = today.weekday()
    days_since_friday = (weekday - 4) % 7
    end_date = today.date() - timedelta(days=days_since_friday)
    start_date = end_date - timedelta(days=4)
    return start_date, end_date


def collect_issues(issues_dir, start_date, end_date):
    collected = []
    for filename in os.listdir(issues_dir):
        if not filename.endswith(".json"):
            continue
        date_str = filename.replace(".json", "")
        try:
            file_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            continue
        if start_date <= file_date <= end_date:
            data = load_issue(os.path.join(issues_dir, filename))
            if data:
                collected.append(data)
    return collected


def build_html_from_markdown(markdown_text):
    escaped = html.escape(markdown_text)
    return (
        "<pre style=\"font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "
        "'Liberation Mono', 'Courier New', monospace; white-space: pre-wrap; line-height: 1.5;\">"
        f"{escaped}</pre>"
    )


def load_config(path):
    if not path:
        return {}
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}


def main():
    parser = argparse.ArgumentParser(description="Send weekly digest to weekly subscribers.")
    parser.add_argument("--issues-dir", default="newsletter/issues")
    parser.add_argument("--subscribers", default="newsletter/subscribers.csv")
    parser.add_argument("--config", default="newsletter/generate_config.json")
    parser.add_argument("--timezone", default="Europe/London")
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--max-recipients", type=int, default=500)
    parser.add_argument(
        "--frequency",
        default="",
        help="Subscriber frequency to target: weekly, daily, or all (default: env NEWSLETTER_WEEKLY_FREQUENCY or weekly).",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    tz = ZoneInfo(args.timezone)
    today = datetime.now(tz)
    start_date, end_date = get_week_range(today)
    issues_dir = args.issues_dir

    issues = collect_issues(issues_dir, start_date, end_date)
    if not issues:
        raise ValueError("No issues found for the weekly digest window.")

    md_content = generate_digest_md(issues, start_date, end_date)
    config = load_config(args.config)
    newsletter_name = config.get("newsletter_name", "Protein Design Digest")
    date_range = f"{start_date.strftime('%b %d')} - {end_date.strftime('%b %d, %Y')}"
    subject = f"{newsletter_name} Weekly Digest: {date_range}"

    manage_prefs_link = config.get("manage_prefs_link", "")
    unsubscribe_link = config.get("unsubscribe_link", "")
    sender_address = config.get("sender_address", "")

    footer_lines = []
    if manage_prefs_link:
        footer_lines.append(f"Manage preferences: {manage_prefs_link}")
    if unsubscribe_link:
        footer_lines.append(f"Unsubscribe: {unsubscribe_link}")
    if sender_address:
        footer_lines.append(sender_address)
    footer_text = "\n\n" + "\n".join(footer_lines) if footer_lines else ""

    text_body = md_content + footer_text
    html_body = build_html_from_markdown(md_content)
    if footer_lines:
        html_body += "<p style=\"margin-top:16px; font-size:12px; color:#666;\">" + "<br>".join(
            html.escape(line) for line in footer_lines
        ) + "</p>"

    freq = (args.frequency or os.getenv("NEWSLETTER_WEEKLY_FREQUENCY") or "weekly").strip().lower()
    if freq in {"", "all", "any"}:
        subscribers = load_subscribers(args.subscribers, None)
    elif freq in {"daily", "weekly"}:
        subscribers = load_subscribers(args.subscribers, freq)
    else:
        raise ValueError(f"Unknown frequency '{freq}'. Use daily, weekly, or all.")
    if not subscribers:
        raise ValueError("No weekly subscribers found.")
    if args.max_recipients and len(subscribers) > args.max_recipients:
        raise ValueError(
            f"Subscriber count {len(subscribers)} exceeds max {args.max_recipients}"
        )

    smtp_user = os.getenv("NEWSLETTER_GMAIL_USER")
    smtp_pass = os.getenv("NEWSLETTER_GMAIL_APP_PASSWORD")
    from_email = os.getenv("NEWSLETTER_FROM_EMAIL") or smtp_user
    from_name = os.getenv("NEWSLETTER_FROM_NAME", "")
    reply_to = os.getenv("NEWSLETTER_REPLY_TO", "")
    if not from_email or not smtp_user or not smtp_pass:
        raise ValueError("SMTP credentials missing (NEWSLETTER_GMAIL_USER and NEWSLETTER_GMAIL_APP_PASSWORD)")

    if args.dry_run:
        print(f"Dry run: would send '{subject}' to {len(subscribers)} weekly subscribers.")
        return

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(smtp_user, smtp_pass)
        for batch in chunk_list(subscribers, args.batch_size):
            msg = build_message(
                subject,
                from_email,
                from_name,
                from_email,
                reply_to,
                text_body,
                html_body,
                unsubscribe_link,
            )
            smtp.sendmail(from_email, batch, msg.as_string())

    print(f"Weekly digest sent to {len(subscribers)} subscribers.")


if __name__ == "__main__":
    main()
