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
            f'<div style="margin-bottom:28px;">'
            f'<div style="font-family:\'Georgia\', serif; font-size:18px; font-weight:bold; line-height:1.4; margin-bottom:8px;">'
            f'<a href="{link}" style="color:#0b2a1f; text-decoration:none; border-bottom:1px solid #d1d8d5;">{title}</a>'
            f'<span style="font-size:12px; color:#64748b; font-weight:normal; margin-left:8px;">{suffix}</span>'
            f'</div>'
            f'<div style="font-family:Arial, sans-serif; font-size:14px; color:#444; line-height:1.6;">{abstract}</div>'
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
            f'<div style="margin-bottom:24px;">'
            f'<div style="font-family:Arial, sans-serif; font-size:15px; font-weight:bold; line-height:1.4; margin-bottom:6px;">'
            f'<a href="{link}" style="color:#1e293b; text-decoration:none; border-bottom:1px solid #e2e8f0;">{title}</a>'
            f'<span style="font-size:11px; color:#64748b; font-weight:normal; margin-left:6px;">{suffix}</span>'
            f'</div>'
            f'<div style="font-family:Arial, sans-serif; font-size:13px; color:#475569; line-height:1.5;">{abstract}</div>'
            f'</div>'
        )
    return "\n".join(rendered) if rendered else "<li>No AI news matched today.</li>"


def build_industry_news_html(items):
    if not items:
        return "<li>No industry updates matched today.</li>"
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
            f'<div style="margin-bottom:24px;">'
            f'<div style="font-family:Arial, sans-serif; font-size:15px; font-weight:bold; line-height:1.4; margin-bottom:6px;">'
            f'<a href="{link}" style="color:#0c4a6e; text-decoration:none; border-bottom:1px solid #bae6fd;">{title}</a>'
            f'<span style="font-size:11px; color:#64748b; font-weight:normal; margin-left:6px;">{suffix}</span>'
            f'</div>'
            f'<div style="font-family:Arial, sans-serif; font-size:13px; color:#334155; line-height:1.5;">{abstract}</div>'
            f'</div>'
        )
    return "\n".join(rendered) if rendered else "<li>No industry updates matched today.</li>"


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


def build_industry_news_text(items):
    if not items:
        return "- No industry updates matched today."
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
    return "\n".join(rendered) if rendered else "- No industry updates matched today."


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

    def coerce_list(value):
        if isinstance(value, list):
            return value
        if isinstance(value, dict):
            return [value]
        return []

    # Career / Community helper
    def format_career(title, org, link):
        return f'<strong style="color:#1c2b26;">{title}</strong> at {org}: <a href="{link}" style="color:#0b6e4f; text-decoration:none; border-bottom:1px solid #c8e1d9;">View Openings &rarr;</a>'

    datasets = coerce_list(issue.get("dataset"))
    tools = coerce_list(issue.get("tool"))
    events = coerce_list((issue.get("community") or {}).get("event"))
    jobs = coerce_list((issue.get("community") or {}).get("job"))

    dataset_main = datasets[0] if datasets else {}
    tool_main = tools[0] if tools else {}
    event_main = events[0] if events else {}
    job_main = jobs[0] if jobs else {}

    raw_data = {
        "newsletter_name": issue.get("newsletter_name", ""),
        "newsletter_tagline": issue.get("newsletter_tagline", ""),
        "issue_date": datetime.strptime(issue.get("issue_date"), "%Y-%m-%d").strftime("%A, %B %d, %Y"),
        "issue_number": str(issue.get("issue_number", "")),
        "edition_time": issue.get("edition_time", ""),
        "preheader_text": issue.get("preheader_text", ""),
        "signal_title": issue.get("signal", {}).get("title", ""),
        "signal_summary": issue.get("signal", {}).get("summary", ""),
        "signal_why_it_matters": issue.get("signal", {}).get("why_it_matters", ""),
        "signal_link": issue.get("signal", {}).get("link", ""),
        "dataset_title": dataset_main.get("title", ""),
        "dataset_summary": dataset_main.get("summary", ""),
        "dataset_link": dataset_main.get("link", ""),
        "tool_title": tool_main.get("title", ""),
        "tool_summary": tool_main.get("summary", ""),
        "tool_link": tool_main.get("link", ""),
        "pipeline_tip": issue.get("pipeline_tip", ""),
        "event_title": event_main.get("title", ""),
        "event_date": event_main.get("date", ""),
        "event_link": event_main.get("link", ""),
        "job_title": job_main.get("title", ""),
        "job_org": job_main.get("org", ""),
        "job_link": job_main.get("link", ""),
        "quote": issue.get("quote", {}).get("text", ""),
        "quote_source": issue.get("quote", {}).get("source", ""),
        "manage_prefs_link": issue.get("manage_prefs_link", ""),
        "unsubscribe_link": issue.get("unsubscribe_link", ""),
        "sender_address": issue.get("sender_address", ""),
    }

    # Build HTML Context
    html_context = {k: html.escape(str(v)) for k, v in raw_data.items()}
    html_context["quick_reads_html"] = build_quick_reads_html(quick_reads)
    html_context["ai_news_html"] = build_ai_news_html(ai_news)
    html_context["industry_news_html"] = build_industry_news_html(issue.get("industry_news", []))
    html_context["job_display"] = format_career(html_context["job_title"], html_context["job_org"], html_context["job_link"])
    html_context["event_display"] = format_career(html_context["event_title"], "Community Hub", html_context["event_link"])

    extra_datasets = datasets[1:] if len(datasets) > 1 else []
    extra_tools = tools[1:] if len(tools) > 1 else []
    extra_events = events[1:] if len(events) > 1 else []
    extra_jobs = jobs[1:] if len(jobs) > 1 else []

    html_context["dataset_extra_html"] = "".join(
        f'<div style="margin-top:8px;"><a href="{html.escape(str(item.get("link", "")), quote=True)}" style="color:#0f172a; text-decoration:none; border-bottom:1px solid #e2e8f0;">{html.escape(str(item.get("title", "")))}</a><div style="font-family:Arial, sans-serif; font-size:12px; color:#64748b; margin-top:4px;">{html.escape(str(item.get("summary", "")))}</div></div>'
        for item in extra_datasets
    )
    html_context["tool_extra_html"] = "".join(
        f'<div style="margin-top:8px;"><a href="{html.escape(str(item.get("link", "")), quote=True)}" style="color:#0f172a; text-decoration:none; border-bottom:1px solid #e2e8f0;">{html.escape(str(item.get("title", "")))}</a><div style="font-family:Arial, sans-serif; font-size:12px; color:#64748b; margin-top:4px;">{html.escape(str(item.get("summary", "")))}</div></div>'
        for item in extra_tools
    )
    html_context["event_list_html"] = "<br>".join(
        format_career(html.escape(str(item.get("title", ""))), "Community Hub", html.escape(str(item.get("link", ""))))
        for item in extra_events
    )
    html_context["job_list_html"] = "<br>".join(
        format_career(html.escape(str(item.get("title", ""))), html.escape(str(item.get("org", ""))), html.escape(str(item.get("link", ""))))
        for item in extra_jobs
    )

    signal_extras = issue.get("signal_extras") or []
    if signal_extras:
        extras_body = "".join(
            f'<div style="margin-top:18px;"><div style="font-family:Arial, sans-serif; font-size:15px; font-weight:bold; margin-bottom:6px;"><a href="{html.escape(str(item.get("link", "")), quote=True)}" style="color:#0f172a; text-decoration:none; border-bottom:1px solid #e2e8f0;">{html.escape(str(item.get("title", "")))}</a></div><div style="font-family:Arial, sans-serif; font-size:13px; color:#475569; line-height:1.5;">{html.escape(str(item.get("abstract", "")))}</div></div>'
            for item in signal_extras
        )
        html_context["signal_extras_html"] = (
            '<div style="margin-top:30px; padding-top:20px; border-top:1px solid #f1f5f9;">'
            '<div style="font-family:Arial, sans-serif; font-size:12px; color:#64748b; font-weight:bold; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:12px;">'
            '⭐ Additional Signals</div>'
            f"{extras_body}</div>"
        )
    else:
        html_context["signal_extras_html"] = ""

    # Build Text Context
    text_context = {k: str(v) for k, v in raw_data.items()}
    text_context["quick_reads_text"] = build_quick_reads_text(quick_reads)
    text_context["ai_news_text"] = build_ai_news_text(ai_news)
    text_context["industry_news_text"] = build_industry_news_text(issue.get("industry_news", []))
    text_context["dataset_list_text"] = "\n".join(
        f"- {item.get('title', '')} ({item.get('link', '')})"
        for item in extra_datasets
    )
    text_context["tool_list_text"] = "\n".join(
        f"- {item.get('title', '')} ({item.get('link', '')})"
        for item in extra_tools
    )
    text_context["event_list_text"] = "\n".join(
        f"- {item.get('title', '')} ({item.get('link', '')})"
        for item in extra_events
    )
    text_context["job_list_text"] = "\n".join(
        f"- {item.get('title', '')} ({item.get('link', '')})"
        for item in extra_jobs
    )
    text_context["signal_extras_text"] = "\n".join(
        f"- {item.get('title', '')} ({item.get('link', '')})"
        for item in signal_extras
    )

    subject = optional_field(issue, "subject", "").strip()
    if not subject:
        subject = f"{raw_data['newsletter_name']} - {raw_data['issue_date']}"

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
