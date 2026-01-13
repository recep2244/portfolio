#!/usr/bin/env python3
"""Send weekly analytics report via email."""

import argparse
import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from .storage import AnalyticsDB


def generate_email_report(db: AnalyticsDB, days: int = 7, tracker_url: str = "") -> str:
    """Generate HTML email report."""
    trends = db.get_trend_data(days)
    sources = db.get_source_performance(days)

    total_sent = sum(t.get("total_sent", 0) for t in trends)
    total_opens = sum(t.get("unique_opens", 0) for t in trends)
    total_clicks = sum(t.get("unique_clickers", 0) for t in trends)
    avg_open = (total_opens / total_sent * 100) if total_sent > 0 else 0
    avg_click = (total_clicks / total_sent * 100) if total_sent > 0 else 0

    # Build trend rows
    trend_rows = ""
    for t in trends:
        sent = t.get("total_sent", 0)
        opens = t.get("unique_opens", 0)
        clicks = t.get("unique_clickers", 0)
        open_pct = (opens / sent * 100) if sent > 0 else 0
        click_pct = (clicks / sent * 100) if sent > 0 else 0
        trend_rows += f"""
        <tr>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;">{t['issue_date']}</td>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;text-align:center;">{sent}</td>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;text-align:center;">{opens} ({open_pct:.1f}%)</td>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;text-align:center;">{clicks} ({click_pct:.1f}%)</td>
        </tr>"""

    # Build source rows
    source_rows = ""
    for s in sources:
        fetched = s.get("total_fetched", 0)
        selected = s.get("total_selected", 0)
        rate = (selected / fetched * 100) if fetched > 0 else 0
        score = s.get("avg_score", 0) or 0
        source_rows += f"""
        <tr>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;">{s['source']}</td>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;text-align:center;">{fetched}</td>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;text-align:center;">{selected}</td>
            <td style="padding:12px;border-bottom:1px solid #e2e8f0;text-align:center;">{rate:.1f}%</td>
        </tr>"""

    dashboard_link = ""
    if tracker_url:
        dashboard_link = f"""
        <div style="text-align:center;margin:30px 0;">
            <a href="{tracker_url}/dashboard" style="background:#0b6e4f;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:bold;display:inline-block;">
                View Full Dashboard
            </a>
        </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body style="margin:0;padding:0;background:#f8fafc;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
        <table width="100%" cellspacing="0" cellpadding="0" style="background:#f8fafc;padding:40px 20px;">
            <tr>
                <td align="center">
                    <table width="600" cellspacing="0" cellpadding="0" style="background:white;border-radius:16px;overflow:hidden;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
                        <!-- Header -->
                        <tr>
                            <td style="background:linear-gradient(135deg,#0b6e4f,#10b981);padding:40px;text-align:center;">
                                <h1 style="margin:0;color:white;font-size:28px;">Weekly Analytics Report</h1>
                                <p style="margin:10px 0 0;color:rgba(255,255,255,0.9);font-size:14px;">
                                    Protein Design Digest - {datetime.now().strftime('%B %d, %Y')}
                                </p>
                            </td>
                        </tr>

                        <!-- Summary Stats -->
                        <tr>
                            <td style="padding:40px;">
                                <h2 style="margin:0 0 20px;color:#0f172a;font-size:18px;">Last {days} Days Summary</h2>
                                <table width="100%" cellspacing="0" cellpadding="0">
                                    <tr>
                                        <td width="25%" style="text-align:center;padding:20px;background:#f0fdf4;border-radius:12px;">
                                            <div style="font-size:32px;font-weight:bold;color:#0b6e4f;">{total_sent}</div>
                                            <div style="font-size:12px;color:#64748b;margin-top:4px;">Emails Sent</div>
                                        </td>
                                        <td width="5%"></td>
                                        <td width="25%" style="text-align:center;padding:20px;background:#f0f9ff;border-radius:12px;">
                                            <div style="font-size:32px;font-weight:bold;color:#0369a1;">{total_opens}</div>
                                            <div style="font-size:12px;color:#64748b;margin-top:4px;">Opens</div>
                                        </td>
                                        <td width="5%"></td>
                                        <td width="20%" style="text-align:center;padding:20px;background:#fef3c7;border-radius:12px;">
                                            <div style="font-size:32px;font-weight:bold;color:#d97706;">{avg_open:.1f}%</div>
                                            <div style="font-size:12px;color:#64748b;margin-top:4px;">Open Rate</div>
                                        </td>
                                        <td width="5%"></td>
                                        <td width="20%" style="text-align:center;padding:20px;background:#fce7f3;border-radius:12px;">
                                            <div style="font-size:32px;font-weight:bold;color:#db2777;">{avg_click:.1f}%</div>
                                            <div style="font-size:12px;color:#64748b;margin-top:4px;">Click Rate</div>
                                        </td>
                                    </tr>
                                </table>

                                {dashboard_link}

                                <!-- Issue Performance -->
                                <h2 style="margin:40px 0 20px;color:#0f172a;font-size:18px;">Issue Performance</h2>
                                <table width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #e2e8f0;border-radius:8px;overflow:hidden;">
                                    <tr style="background:#f8fafc;">
                                        <th style="padding:12px;text-align:left;font-size:12px;color:#64748b;text-transform:uppercase;">Date</th>
                                        <th style="padding:12px;text-align:center;font-size:12px;color:#64748b;text-transform:uppercase;">Sent</th>
                                        <th style="padding:12px;text-align:center;font-size:12px;color:#64748b;text-transform:uppercase;">Opens</th>
                                        <th style="padding:12px;text-align:center;font-size:12px;color:#64748b;text-transform:uppercase;">Clicks</th>
                                    </tr>
                                    {trend_rows if trend_rows else '<tr><td colspan="4" style="padding:20px;text-align:center;color:#94a3b8;">No data yet</td></tr>'}
                                </table>

                                <!-- Source Performance -->
                                <h2 style="margin:40px 0 20px;color:#0f172a;font-size:18px;">Paper Source Performance</h2>
                                <table width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #e2e8f0;border-radius:8px;overflow:hidden;">
                                    <tr style="background:#f8fafc;">
                                        <th style="padding:12px;text-align:left;font-size:12px;color:#64748b;text-transform:uppercase;">Source</th>
                                        <th style="padding:12px;text-align:center;font-size:12px;color:#64748b;text-transform:uppercase;">Fetched</th>
                                        <th style="padding:12px;text-align:center;font-size:12px;color:#64748b;text-transform:uppercase;">Selected</th>
                                        <th style="padding:12px;text-align:center;font-size:12px;color:#64748b;text-transform:uppercase;">Rate</th>
                                    </tr>
                                    {source_rows if source_rows else '<tr><td colspan="4" style="padding:20px;text-align:center;color:#94a3b8;">No data yet</td></tr>'}
                                </table>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="padding:30px;background:#f8fafc;text-align:center;">
                                <p style="margin:0;color:#64748b;font-size:12px;">
                                    Protein Design Digest Analytics<br>
                                    Generated automatically every Sunday at 5 PM
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    return html


def send_report(
    to_email: str,
    html_body: str,
    smtp_user: str,
    smtp_pass: str,
    from_email: str = None,
):
    """Send the report via Gmail."""
    from_email = from_email or smtp_user

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Weekly Newsletter Analytics - {datetime.now().strftime('%B %d, %Y')}"
    msg["From"] = f"Newsletter Analytics <{from_email}>"
    msg["To"] = to_email

    # Plain text version
    text_body = f"""
Weekly Newsletter Analytics Report
Generated: {datetime.now().strftime('%B %d, %Y at %H:%M')}

View the full dashboard for detailed analytics.

This report is sent automatically every Sunday at 5 PM.
    """

    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(smtp_user, smtp_pass)
        smtp.sendmail(from_email, [to_email], msg.as_string())

    print(f"Analytics report sent to {to_email}")


def main():
    parser = argparse.ArgumentParser(description="Send weekly analytics report")
    parser.add_argument("--to", default=os.getenv("ANALYTICS_REPORT_EMAIL", "recepadiyaman2244@gmail.com"),
                        help="Email to send report to")
    parser.add_argument("--days", type=int, default=7, help="Number of days to include")
    parser.add_argument("--db", default=os.getenv("NEWSLETTER_ANALYTICS_DB", ""),
                        help="Path to analytics database")
    parser.add_argument("--tracker-url", default=os.getenv("NEWSLETTER_TRACKER_URL", "http://localhost:8080"),
                        help="URL to analytics dashboard")
    parser.add_argument("--smtp-user", default=os.getenv("NEWSLETTER_GMAIL_USER"))
    parser.add_argument("--smtp-pass", default=os.getenv("NEWSLETTER_GMAIL_APP_PASSWORD"))
    parser.add_argument("--dry-run", action="store_true", help="Print report without sending")
    args = parser.parse_args()

    # Find database
    db_path = args.db
    if not db_path:
        db_path = Path(__file__).parent.parent / "analytics.db"
    else:
        db_path = Path(db_path)

    db = AnalyticsDB(db_path)
    html_report = generate_email_report(db, args.days, args.tracker_url)

    if args.dry_run:
        print("=== DRY RUN - Report Preview ===")
        # Save to file for preview
        preview_path = Path(__file__).parent.parent / "analytics_report_preview.html"
        preview_path.write_text(html_report, encoding="utf-8")
        print(f"Preview saved to: {preview_path}")
        return

    if not args.smtp_user or not args.smtp_pass:
        print("Error: SMTP credentials required (NEWSLETTER_GMAIL_USER and NEWSLETTER_GMAIL_APP_PASSWORD)")
        return

    send_report(args.to, html_report, args.smtp_user, args.smtp_pass)


if __name__ == "__main__":
    main()
