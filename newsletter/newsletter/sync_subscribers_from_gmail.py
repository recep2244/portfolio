#!/usr/bin/env python3
import argparse
import csv
import html
import imaplib
import os
import re
import sys
from datetime import datetime, timedelta
from email import message_from_bytes
from email.header import decode_header
from email.utils import parseaddr
from pathlib import Path


DEFAULT_SUBJECT = "New Protein Digest Subscriber!"
DEFAULT_SENDERS = "formsubmit.co,formspree.io"
ACTIVE_STATUSES = {"active", ""}
SKIP_STATUSES = {"unsubscribed", "inactive", "bounced"}
DEFAULT_UNSUBSCRIBE_KEYWORDS = "unsubscribe,remove me,stop emails,stop sending"


def decode_header_value(value):
    if not value:
        return ""
    parts = decode_header(value)
    decoded = []
    for part, encoding in parts:
        if isinstance(part, bytes):
            decoded.append(part.decode(encoding or "utf-8", errors="replace"))
        else:
            decoded.append(part)
    return "".join(decoded)


def decode_part(part):
    payload = part.get_payload(decode=True) or b""
    charset = part.get_content_charset() or "utf-8"
    return payload.decode(charset, errors="replace")


def extract_text(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            disposition = (part.get("Content-Disposition") or "").lower()
            if content_type == "text/plain" and "attachment" not in disposition:
                return decode_part(part)
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                text = decode_part(part)
                text = re.sub(r"<[^>]+>", " ", text)
                return html.unescape(text)
    else:
        return decode_part(msg)
    return ""


def extract_fields(text):
    fields = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        if key and value:
            fields[key] = value

    name = fields.get("name") or fields.get("first name") or fields.get("first_name")
    email_addr = fields.get("email")
    frequency = fields.get("frequency") or fields.get("digest")

    if not email_addr:
        match = re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text, re.I)
        if match:
            email_addr = match.group(0)

    if frequency:
        frequency = frequency.strip().lower()
    else:
        if re.search(r"\bweekly\b", text, re.I):
            frequency = "weekly"
        elif re.search(r"\bdaily\b", text, re.I):
            frequency = "daily"

    if frequency not in {"daily", "weekly"}:
        frequency = "daily"

    return name, email_addr, frequency


def load_subscribers(path):
    rows = []
    fieldnames = ["email", "name", "status", "frequency"]
    if path.exists():
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames:
                fieldnames = reader.fieldnames
            for row in reader:
                rows.append(row)
    for field in ["email", "name", "status", "frequency"]:
        if field not in fieldnames:
            fieldnames.append(field)
    return rows, fieldnames


def write_subscribers(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalize_email(value):
    return (value or "").strip().lower()


def extract_email_from_text(text):
    match = re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text, re.I)
    return match.group(0) if match else ""


def normalize_frequency(value):
    value = (value or "").strip().lower()
    return value if value in {"daily", "weekly"} else "daily"


def normalize_status(value):
    value = (value or "").strip().lower()
    if value in {"unsubscribed", "inactive", "bounced"}:
        return value
    if value in ACTIVE_STATUSES:
        return "active"
    return value or "active"


def status_rank(status):
    status = (status or "").strip().lower()
    if status == "unsubscribed":
        return 3
    if status == "bounced":
        return 2
    if status == "inactive":
        return 1
    return 0


def merge_rows(existing, incoming):
    changed = False

    existing_status = normalize_status(existing.get("status"))
    incoming_status = normalize_status(incoming.get("status"))
    if status_rank(incoming_status) > status_rank(existing_status):
        existing["status"] = incoming_status
        changed = True
    else:
        if existing.get("status") != existing_status:
            existing["status"] = existing_status
            changed = True

    existing_freq = normalize_frequency(existing.get("frequency"))
    incoming_freq = normalize_frequency(incoming.get("frequency"))
    desired_freq = "weekly" if "weekly" in {existing_freq, incoming_freq} else "daily"
    if existing.get("frequency") != desired_freq:
        existing["frequency"] = desired_freq
        changed = True

    if not (existing.get("name") or "").strip() and (incoming.get("name") or "").strip():
        existing["name"] = incoming.get("name")
        changed = True

    for key, value in incoming.items():
        if key in {"email", "status", "frequency", "name"}:
            continue
        if value and not existing.get(key):
            existing[key] = value
            changed = True

    return changed


def load_blocklist(path):
    blocked = set()
    if not path or not path.exists():
        return blocked
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            first_line = handle.readline()
            handle.seek(0)
            if "email" in (first_line or "").lower():
                reader = csv.DictReader(handle)
                for row in reader:
                    email = normalize_email(row.get("email"))
                    if email:
                        blocked.add(email)
            else:
                for line in handle:
                    email = normalize_email(line.split(",")[0])
                    if email:
                        blocked.add(email)
    except OSError:
        return blocked
    return blocked


def dedupe_rows(rows, blocklist):
    merged = []
    index = {}
    changed = False

    for row in rows:
        email_raw = row.get("email")
        email_norm = normalize_email(email_raw)
        if not email_norm:
            continue
        if blocklist and email_norm in blocklist:
            changed = True
            continue
        if email_norm not in index:
            normalized = dict(row)
            normalized["email"] = email_norm
            normalized["status"] = normalize_status(row.get("status"))
            normalized["frequency"] = normalize_frequency(row.get("frequency"))
            merged.append(normalized)
            index[email_norm] = normalized
            if email_raw != email_norm:
                changed = True
            if normalized["status"] != (row.get("status") or ""):
                changed = True
            if normalized["frequency"] != (row.get("frequency") or ""):
                changed = True
        else:
            existing = index[email_norm]
            if merge_rows(existing, row):
                changed = True
            changed = True

    return merged, index, changed


def should_process(subject, sender, subjects, senders):
    subject = (subject or "").lower()
    sender = (sender or "").lower()
    if subjects and any(item in subject for item in subjects):
        return True
    if senders and any(item in sender for item in senders):
        return True
    return False


def is_unsubscribe_request(subject, keywords):
    subject = (subject or "").lower()
    return any(keyword in subject for keyword in keywords)


def main():
    parser = argparse.ArgumentParser(description="Sync FormSubmit/Formspree subscribers from Gmail.")
    parser.add_argument("--subscribers", required=True, help="Path to subscribers.csv")
    parser.add_argument("--imap-host", default="imap.gmail.com")
    parser.add_argument("--imap-user", default=os.getenv("NEWSLETTER_GMAIL_USER"))
    parser.add_argument("--imap-password", default=os.getenv("NEWSLETTER_GMAIL_APP_PASSWORD"))
    parser.add_argument("--subjects", default=os.getenv("NEWSLETTER_SUBSCRIBE_SUBJECTS", DEFAULT_SUBJECT))
    parser.add_argument("--senders", default=os.getenv("NEWSLETTER_SUBSCRIBE_SENDERS", DEFAULT_SENDERS))
    parser.add_argument(
        "--unsubscribe-keywords",
        default=os.getenv("NEWSLETTER_UNSUBSCRIBE_KEYWORDS", DEFAULT_UNSUBSCRIBE_KEYWORDS),
    )
    parser.add_argument(
        "--since-days",
        type=int,
        default=int(os.getenv("NEWSLETTER_SUBSCRIBE_SINCE_DAYS", "2")),
        help="Look back N days (set 0 to process only unread).",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    subjects = [s.strip().lower() for s in args.subjects.split(",") if s.strip()]
    senders = [s.strip().lower() for s in args.senders.split(",") if s.strip()]
    unsubscribe_keywords = [s.strip().lower() for s in args.unsubscribe_keywords.split(",") if s.strip()]

    path = Path(args.subscribers)
    rows, fieldnames = load_subscribers(path)
    blocklist_env = {
        normalize_email(item)
        for item in (os.getenv("NEWSLETTER_INVALID_EMAILS") or "").split(",")
        if item.strip()
    }
    blocklist_path = Path(
        os.getenv("NEWSLETTER_INVALID_EMAILS_PATH", path.parent / "invalid_emails.csv")
    )
    blocked = load_blocklist(blocklist_path)
    blocked |= blocklist_env
    rows, index, dedupe_changed = dedupe_rows(rows, blocked)

    if not args.imap_user or not args.imap_password:
        if dedupe_changed and not args.dry_run:
            write_subscribers(path, rows, fieldnames)
            print("Subscriber sync: duplicates removed (no Gmail sync).")
        else:
            print("Subscriber sync skipped: missing NEWSLETTER_GMAIL_USER or NEWSLETTER_GMAIL_APP_PASSWORD.")
        return 0

    try:
        mail = imaplib.IMAP4_SSL(args.imap_host)
        mail.login(args.imap_user, args.imap_password)
        mail.select("INBOX")
    except imaplib.IMAP4.error as exc:
        print(f"Subscriber sync failed: {exc}")
        return 1

    if args.since_days > 0:
        since_date = (datetime.now() - timedelta(days=args.since_days)).strftime("%d-%b-%Y")
        typ, data = mail.search(None, "SINCE", since_date)
    else:
        typ, data = mail.search(None, "UNSEEN")
    if typ != "OK":
        print("Subscriber sync failed: unable to search inbox.")
        return 1

    new_count = 0
    updated_count = 0
    unsub_count = 0
    processed = 0
    for msg_id in data[0].split():
        typ, msg_data = mail.fetch(msg_id, "(BODY.PEEK[])")
        if typ != "OK" or not msg_data:
            continue
        raw = msg_data[0][1]
        msg = message_from_bytes(raw)
        subject = decode_header_value(msg.get("Subject"))
        sender = decode_header_value(msg.get("From"))
        text = extract_text(msg)
        if is_unsubscribe_request(subject, unsubscribe_keywords):
            from_email = parseaddr(sender)[1]
            email_addr = from_email or extract_email_from_text(text)
            email_norm = normalize_email(email_addr)
            if email_norm and email_norm in blocked:
                mail.store(msg_id, "+FLAGS", "\\Seen")
                processed += 1
                continue
            if email_norm and email_norm in index:
                row = index[email_norm]
                if (row.get("status") or "").strip().lower() != "unsubscribed":
                    row["status"] = "unsubscribed"
                    unsub_count += 1
            mail.store(msg_id, "+FLAGS", "\\Seen")
            processed += 1
            continue

        if not should_process(subject, sender, subjects, senders):
            continue

        name, email_addr, frequency = extract_fields(text)
        email_norm = normalize_email(email_addr)
        if not email_norm:
            continue
        if email_norm in blocked:
            mail.store(msg_id, "+FLAGS", "\\Seen")
            processed += 1
            continue

        if email_norm in index:
            row = index[email_norm]
            status = (row.get("status") or "").strip().lower()
            if status in SKIP_STATUSES:
                mail.store(msg_id, "+FLAGS", "\\Seen")
                processed += 1
                continue
            changed = False
            if name and not row.get("name"):
                row["name"] = name
                changed = True
            if frequency and row.get("frequency") != frequency:
                row["frequency"] = frequency
                changed = True
            if changed:
                updated_count += 1
        else:
            new_row = {
                "email": email_addr,
                "name": name or "",
                "status": "active",
                "frequency": frequency or "daily",
            }
            rows.append(new_row)
            index[email_norm] = new_row
            new_count += 1

        mail.store(msg_id, "+FLAGS", "\\Seen")
        processed += 1

    mail.logout()

    if args.dry_run:
        print(
            f"Dry run: {new_count} new, {updated_count} updated, {unsub_count} unsubscribed, {processed} processed from inbox."
        )
        return 0

    rows, _, dedupe_after = dedupe_rows(rows, blocked)
    if new_count or updated_count or unsub_count or dedupe_changed or dedupe_after:
        write_subscribers(path, rows, fieldnames)
        print(
            f"Subscriber sync: {new_count} new, {updated_count} updated, {unsub_count} unsubscribed."
        )
    else:
        print("Subscriber sync: no new subscribers found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
