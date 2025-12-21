#!/usr/bin/env python3
import argparse
import csv
import html
import json
import os
import re
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from zoneinfo import ZoneInfo

DEFAULT_TIMEZONE = "Europe/London"


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def require_field(data, path):
    cur = data
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise ValueError(f"Missing field: {path}")
        cur = cur[part]
    if cur is None:
        raise ValueError(f"Empty field: {path}")
    if isinstance(cur, str) and not cur.strip():
        raise ValueError(f"Empty field: {path}")
    return cur


def optional_field(data, path, default=""):
    cur = data
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    if cur is None:
        return default
    return cur


def build_quick_reads_html(items):
    rendered = []
    for item in items:
        title = html.escape(str(item.get("title", "")).strip())
        note = html.escape(str(item.get("note", "")).strip())
        link = html.escape(str(item.get("link", "")).strip(), quote=True)
        abstract = html.escape(str(item.get("abstract", "")).strip())
        
        if not title or not link:
            raise ValueError("Quick reads require title and link")
            
        suffix = f" - {note}" if note else ""
        
        rendered.append(
            f'<div style="margin-bottom:24px; border-bottom:1px solid #f0f0f0; padding-bottom:12px;">'
            f'<div style="font-weight:bold; font-size:16px; margin-bottom:8px;"><a href="{link}" style="color:#0b6e4f; text-decoration:none;">{title}</a>{suffix}</div>'
            f'<div style="font-size:14px; color:#444; line-height:1.6; margin-bottom:12px;">{abstract}</div>'
            f'<div><a href="{link}" style="font-size:12px; font-weight:bold; color:#0b6e4f; text-decoration:none; text-transform:uppercase;">Read Paper &rarr;</a></div>'
            f'</div>'
        )
    return "\n".join(rendered)


def build_quick_reads_text(items):
    rendered = []
    for item in items:
        title = str(item.get("title", "")).strip()
        note = str(item.get("note", "")).strip()
        link = str(item.get("link", "")).strip()
        abstract = str(item.get("abstract", "")).strip()
        
        if not title or not link:
            raise ValueError("Quick reads require title and link")
        suffix = f" - {note}" if note else ""
        
        entry = f"- {title}{suffix} ({link})"
        if abstract:
             entry += f"\n  Abstract: {abstract[:400]}..." if len(abstract) > 400 else f"\n  Abstract: {abstract}"
        rendered.append(entry)
    return "\n".join(rendered)


def build_ai_news_html(items):
    if not items:
        return "<li>No AI news matched today.</li>"
    rendered = []
    for item in items:
        title = html.escape(str(item.get("title", "")).strip())
        note = html.escape(str(item.get("note", "")).strip())
        link = html.escape(str(item.get("link", "")).strip(), quote=True)
        abstract = html.escape(str(item.get("abstract", "")).strip())

        if not title or not link:
            continue
        suffix = f" - {note}" if note else ""
        
        rendered.append(
            f'<div style="margin-bottom:20px;">'
            f'<div style="font-weight:bold; font-size:15px; margin-bottom:4px;"><a href="{link}" style="color:#0b6e4f; text-decoration:none;">{title}</a>{suffix}</div>'
            f'<div style="font-size:13px; color:#555; line-height:1.5;">{abstract}</div>'
            f'</div>'
        )
    return "\n".join(rendered) if rendered else "<li>No AI news matched today.</li>"


def build_ai_news_text(items):
    if not items:
        return "- No AI news matched today."
    rendered = []
    for item in items:
        title = str(item.get("title", "")).strip()
        note = str(item.get("note", "")).strip()
        link = str(item.get("link", "")).strip()
        abstract = str(item.get("abstract", "")).strip()

        if not title or not link:
            continue
        suffix = f" - {note}" if note else ""
        
        entry = f"- {title}{suffix} ({link})"
        if abstract:
             entry += f"\n  Abstract: {abstract[:300]}..." if len(abstract) > 300 else f"\n  Abstract: {abstract}"
        rendered.append(entry)
    return "\n".join(rendered) if rendered else "- No AI news matched today."


def render_template(template, context):
    pattern = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")
    missing = set()

    def replacer(match):
        key = match.group(1)
        if key not in context:
            missing.add(key)
            return match.group(0)
        return str(context[key])

    rendered = pattern.sub(replacer, template)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Missing template values: {missing_list}")
    return rendered


def build_context(issue):
    newsletter_name = optional_field(issue, "newsletter_name", "Genome Daily")
    newsletter_tagline = optional_field(
        issue, "newsletter_tagline", "Bioinformatics signals, every morning"
    )

    issue_date = str(require_field(issue, "issue_date")).strip()
    issue_number = str(require_field(issue, "issue_number")).strip()
    edition_time = str(require_field(issue, "edition_time")).strip()
    preheader_text = str(require_field(issue, "preheader_text")).strip()

    signal = require_field(issue, "signal")
    dataset = require_field(issue, "dataset")
    tool = require_field(issue, "tool")
    community = require_field(issue, "community")
    quote = require_field(issue, "quote")

    quick_reads = issue.get("quick_reads", [])
    if not isinstance(quick_reads, list) or not quick_reads:
        raise ValueError("quick_reads must be a non-empty list")
    ai_news = issue.get("ai_news", [])
    if not isinstance(ai_news, list):
        ai_news = []

    raw_context = {
        "newsletter_name": newsletter_name,
        "newsletter_tagline": newsletter_tagline,
        "issue_date": issue_date,
        "issue_number": issue_number,
        "edition_time": edition_time,
        "preheader_text": preheader_text,
        "signal_title": str(require_field(signal, "title")).strip(),
        "signal_summary": str(require_field(signal, "summary")).strip(),
        "signal_why_it_matters": str(require_field(signal, "why_it_matters")).strip(),
        "signal_link": str(require_field(signal, "link")).strip(),
        "dataset_title": str(require_field(dataset, "title")).strip(),
        "dataset_summary": str(require_field(dataset, "summary")).strip(),
        "dataset_link": str(require_field(dataset, "link")).strip(),
        "tool_title": str(require_field(tool, "title")).strip(),
        "tool_summary": str(require_field(tool, "summary")).strip(),
        "tool_link": str(require_field(tool, "link")).strip(),
        "pipeline_tip": str(require_field(issue, "pipeline_tip")).strip(),
        "event_title": str(require_field(community, "event.title")).strip(),
        "event_date": str(require_field(community, "event.date")).strip(),
        "event_link": str(require_field(community, "event.link")).strip(),
        "job_title": str(require_field(community, "job.title")).strip(),
        "job_org": str(require_field(community, "job.org")).strip(),
        "job_link": str(require_field(community, "job.link")).strip(),
        "quote": str(require_field(quote, "text")).strip(),
        "quote_source": str(require_field(quote, "source")).strip(),
        "manage_prefs_link": str(require_field(issue, "manage_prefs_link")).strip(),
        "unsubscribe_link": str(require_field(issue, "unsubscribe_link")).strip(),
        "sender_address": str(require_field(issue, "sender_address")).strip(),
    }

    subject = optional_field(issue, "subject", "").strip()
    if not subject:
        subject = f"{newsletter_name} - {issue_date}"

    text_context = dict(raw_context)
    text_context["quick_reads_text"] = build_quick_reads_text(quick_reads)
    text_context["ai_news_text"] = build_ai_news_text(ai_news)

    html_context = {k: html.escape(v) for k, v in raw_context.items()}
    html_context["quick_reads_html"] = build_quick_reads_html(quick_reads)
    html_context["ai_news_html"] = build_ai_news_html(ai_news)
    html_context["signal_link"] = html.escape(raw_context["signal_link"], quote=True)
    html_context["dataset_link"] = html.escape(raw_context["dataset_link"], quote=True)
    html_context["tool_link"] = html.escape(raw_context["tool_link"], quote=True)
    html_context["event_link"] = html.escape(raw_context["event_link"], quote=True)
    html_context["job_link"] = html.escape(raw_context["job_link"], quote=True)
    html_context["manage_prefs_link"] = html.escape(
        raw_context["manage_prefs_link"], quote=True
    )
    html_context["unsubscribe_link"] = html.escape(
        raw_context["unsubscribe_link"], quote=True
    )

    return html_context, text_context, subject


def load_subscribers(path):
    emails = []
    seen = set()
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "email" not in reader.fieldnames:
            raise ValueError("subscribers.csv must have an email column")
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


def chunk_list(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def build_message(subject, from_email, from_name, to_email, reply_to, text_body, html_body, unsubscribe_link):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    if from_name:
        msg["From"] = f"{from_name} <{from_email}>"
    else:
        msg["From"] = from_email
    msg["To"] = to_email
    if reply_to:
        msg["Reply-To"] = reply_to
    if unsubscribe_link:
        msg["List-Unsubscribe"] = f"<{unsubscribe_link}>"

    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    return msg


def resolve_issue_path(args):
    if args.issue:
        return args.issue
    tz = ZoneInfo(args.timezone)
    if args.issue_date and args.issue_date.lower() != "today":
        issue_date = datetime.strptime(args.issue_date, "%Y-%m-%d").date()
    else:
        issue_date = datetime.now(tz).date()
    filename = f"{issue_date.isoformat()}.json"
    return os.path.join(args.issues_dir, filename)


def save_outputs(output_dir, issue_date, html_body, text_body):
    os.makedirs(output_dir, exist_ok=True)
    html_path = os.path.join(output_dir, f"{issue_date}.html")
    text_path = os.path.join(output_dir, f"{issue_date}.txt")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_body)
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text_body)
    return html_path, text_path


def main():
    parser = argparse.ArgumentParser(description="Send a daily Gmail newsletter")
    parser.add_argument("--issue", help="Path to issue JSON")
    parser.add_argument("--issue-date", help="YYYY-MM-DD or 'today'")
    parser.add_argument("--issues-dir", default="newsletter/issues", help="Directory of issue JSON files")
    parser.add_argument("--subscribers", default="newsletter/subscribers.csv", help="CSV of subscribers")
    parser.add_argument("--template-html", default="newsletter/template.html")
    parser.add_argument("--template-text", default="newsletter/template.txt")
    parser.add_argument("--output-dir", default="newsletter/out")
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--max-recipients", type=int, default=500)
    parser.add_argument("--timezone", default=DEFAULT_TIMEZONE)
    parser.add_argument("--render-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--from-email", default=os.getenv("NEWSLETTER_FROM_EMAIL"))
    parser.add_argument("--from-name", default=os.getenv("NEWSLETTER_FROM_NAME", ""))
    parser.add_argument("--reply-to", default=os.getenv("NEWSLETTER_REPLY_TO", ""))
    parser.add_argument("--smtp-user", default=os.getenv("NEWSLETTER_GMAIL_USER"))
    parser.add_argument("--smtp-pass", default=os.getenv("NEWSLETTER_GMAIL_APP_PASSWORD"))
    args = parser.parse_args()

    issue_path = resolve_issue_path(args)
    issue = load_json(issue_path)
    html_template = load_text(args.template_html)
    text_template = load_text(args.template_text)

    html_context, text_context, subject = build_context(issue)
    html_body = render_template(html_template, html_context)
    text_body = render_template(text_template, text_context)

    issue_date = str(text_context.get("issue_date", "issue"))
    html_path, text_path = save_outputs(args.output_dir, issue_date, html_body, text_body)

    if args.render_only:
        print(f"Rendered: {html_path}")
        print(f"Rendered: {text_path}")
        return

    subscribers = load_subscribers(args.subscribers)
    if not subscribers:
        raise ValueError("No subscribers found")
    if args.max_recipients and len(subscribers) > args.max_recipients:
        raise ValueError(
            f"Subscriber count {len(subscribers)} exceeds max {args.max_recipients}"
        )

    from_email = args.from_email or args.smtp_user
    if not from_email:
        raise ValueError("from email is required (NEWSLETTER_FROM_EMAIL or --from-email)")
    if not args.smtp_user or not args.smtp_pass:
        raise ValueError("SMTP credentials missing (NEWSLETTER_GMAIL_USER and NEWSLETTER_GMAIL_APP_PASSWORD)")

    to_email = from_email
    if args.dry_run:
        print(f"Dry run: would send '{subject}' to {len(subscribers)} recipients")
        print(f"Rendered: {html_path}")
        print(f"Rendered: {text_path}")
        return

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(args.smtp_user, args.smtp_pass)
        for batch in chunk_list(subscribers, args.batch_size):
            msg = build_message(
                subject,
                from_email,
                args.from_name,
                to_email,
                args.reply_to,
                text_body,
                html_body,
                text_context.get("unsubscribe_link"),
            )
            msg["Bcc"] = ", ".join(batch)
            smtp.sendmail(from_email, [to_email] + batch, msg.as_string())

    print(f"Sent '{subject}' to {len(subscribers)} recipients")


if __name__ == "__main__":
    main()
