#!/usr/bin/env python3
"""CLI dashboard and report generator for newsletter analytics."""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from .storage import AnalyticsDB


def format_percentage(value: float) -> str:
    """Format a percentage value."""
    return f"{value:.1f}%"


def print_issue_stats(stats: dict):
    """Print formatted stats for a single issue."""
    print("\n" + "=" * 60)
    print(f"  Issue: {stats['issue_date']}")
    print("=" * 60)

    print(f"\n  Delivery")
    print(f"  {'Total Sent:':<20} {stats['total_sent']}")

    print(f"\n  Opens")
    print(f"  {'Unique Opens:':<20} {stats['unique_opens']}")
    print(f"  {'Total Opens:':<20} {stats['total_opens']}")
    print(f"  {'Open Rate:':<20} {format_percentage(stats['open_rate'])}")

    print(f"\n  Clicks")
    print(f"  {'Unique Clickers:':<20} {stats['unique_clickers']}")
    print(f"  {'Total Clicks:':<20} {stats['total_clicks']}")
    print(f"  {'Click Rate:':<20} {format_percentage(stats['click_rate'])}")

    if stats['top_links']:
        print(f"\n  Top Links")
        for i, link in enumerate(stats['top_links'][:5], 1):
            url = link['link_url'][:50] + "..." if len(link['link_url']) > 50 else link['link_url']
            link_type = f" [{link['link_type']}]" if link.get('link_type') else ""
            print(f"  {i}. {link['click_count']:>3}x {url}{link_type}")

    if stats['sources']:
        print(f"\n  Source Performance")
        print(f"  {'Source':<20} {'Fetched':>10} {'Selected':>10} {'Score':>8}")
        print(f"  {'-' * 50}")
        for src in stats['sources']:
            score = f"{src['avg_score']:.1f}" if src['avg_score'] else "-"
            print(f"  {src['source']:<20} {src['papers_fetched']:>10} {src['papers_selected']:>10} {score:>8}")

    print()


def print_trends(trends: list, title: str = "Recent Performance"):
    """Print trend summary."""
    if not trends:
        print("\n  No trend data available.")
        return

    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)
    print(f"\n  {'Date':<12} {'Sent':>8} {'Opens':>8} {'Open%':>8} {'Clicks':>8} {'Click%':>8}")
    print(f"  {'-' * 56}")

    for t in trends[:10]:
        sent = t.get('total_sent', 0)
        opens = t.get('unique_opens', 0)
        clicks = t.get('unique_clickers', 0)
        open_pct = (opens / sent * 100) if sent > 0 else 0
        click_pct = (clicks / sent * 100) if sent > 0 else 0

        print(f"  {t['issue_date']:<12} {sent:>8} {opens:>8} {open_pct:>7.1f}% {clicks:>8} {click_pct:>7.1f}%")

    # Summary
    total_sent = sum(t.get('total_sent', 0) for t in trends)
    total_opens = sum(t.get('unique_opens', 0) for t in trends)
    total_clicks = sum(t.get('unique_clickers', 0) for t in trends)

    print(f"  {'-' * 56}")
    avg_open = (total_opens / total_sent * 100) if total_sent > 0 else 0
    avg_click = (total_clicks / total_sent * 100) if total_sent > 0 else 0
    print(f"  {'TOTAL':<12} {total_sent:>8} {total_opens:>8} {avg_open:>7.1f}% {total_clicks:>8} {avg_click:>7.1f}%")
    print()


def print_source_performance(sources: list):
    """Print source performance summary."""
    if not sources:
        print("\n  No source data available.")
        return

    print("\n" + "=" * 70)
    print("  Paper Source Performance")
    print("=" * 70)
    print(f"\n  {'Source':<25} {'Fetched':>10} {'Selected':>10} {'Rate':>8} {'Score':>8}")
    print(f"  {'-' * 62}")

    for src in sources:
        fetched = src.get('total_fetched', 0)
        selected = src.get('total_selected', 0)
        rate = (selected / fetched * 100) if fetched > 0 else 0
        score = src.get('avg_score', 0) or 0

        print(f"  {src['source']:<25} {fetched:>10} {selected:>10} {rate:>7.1f}% {score:>7.1f}")

    print()


def generate_html_report(db: AnalyticsDB, output_path: Path, days: int = 30):
    """Generate a standalone HTML report."""
    trends = db.get_trend_data(days)
    sources = db.get_source_performance(days)

    total_sent = sum(t.get('total_sent', 0) for t in trends)
    total_opens = sum(t.get('unique_opens', 0) for t in trends)
    total_clicks = sum(t.get('unique_clickers', 0) for t in trends)
    avg_open = (total_opens / total_sent * 100) if total_sent > 0 else 0
    avg_click = (total_clicks / total_sent * 100) if total_sent > 0 else 0

    trend_rows = ""
    for t in trends:
        sent = t.get('total_sent', 0)
        opens = t.get('unique_opens', 0)
        clicks = t.get('unique_clickers', 0)
        open_pct = (opens / sent * 100) if sent > 0 else 0
        click_pct = (clicks / sent * 100) if sent > 0 else 0
        trend_rows += f"""
        <tr>
            <td>{t['issue_date']}</td>
            <td>{sent}</td>
            <td>{opens} ({open_pct:.1f}%)</td>
            <td>{clicks} ({click_pct:.1f}%)</td>
        </tr>"""

    source_rows = ""
    for s in sources:
        fetched = s.get('total_fetched', 0)
        selected = s.get('total_selected', 0)
        rate = (selected / fetched * 100) if fetched > 0 else 0
        score = s.get('avg_score', 0) or 0
        source_rows += f"""
        <tr>
            <td>{s['source']}</td>
            <td>{fetched}</td>
            <td>{selected}</td>
            <td>{rate:.1f}%</td>
            <td>{score:.1f}</td>
        </tr>"""

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Newsletter Analytics Report - {datetime.now().strftime('%Y-%m-%d')}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; padding: 2rem; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        h1 {{ font-size: 1.75rem; font-weight: 700; margin-bottom: 0.5rem; color: #0f172a; }}
        h2 {{ font-size: 1.125rem; font-weight: 600; margin: 2rem 0 1rem; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
        .subtitle {{ color: #64748b; margin-bottom: 2rem; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-bottom: 2rem; }}
        .stat-card {{ background: white; border-radius: 8px; padding: 1.25rem; box-shadow: 0 1px 2px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; }}
        .stat-value {{ font-size: 1.5rem; font-weight: 700; color: #0f172a; }}
        .stat-label {{ font-size: 0.75rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; }}
        table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 2px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; }}
        th, td {{ padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid #f1f5f9; font-size: 0.875rem; }}
        th {{ background: #f8fafc; font-weight: 600; color: #475569; }}
        tr:hover {{ background: #fafafa; }}
        .section {{ margin-bottom: 2.5rem; }}
        .footer {{ color: #94a3b8; font-size: 0.75rem; margin-top: 2rem; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Protein Design Digest Analytics</h1>
        <p class="subtitle">Report generated {datetime.now().strftime('%B %d, %Y at %H:%M')} - Last {days} days</p>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Total Sent</div>
                <div class="stat-value">{total_sent}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Unique Opens</div>
                <div class="stat-value">{total_opens}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Avg Open Rate</div>
                <div class="stat-value">{avg_open:.1f}%</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Avg Click Rate</div>
                <div class="stat-value">{avg_click:.1f}%</div>
            </div>
        </div>

        <div class="section">
            <h2>Issue Performance</h2>
            <table>
                <thead>
                    <tr><th>Date</th><th>Sent</th><th>Opens</th><th>Clicks</th></tr>
                </thead>
                <tbody>{trend_rows or '<tr><td colspan="4" style="text-align:center;color:#94a3b8;">No data</td></tr>'}</tbody>
            </table>
        </div>

        <div class="section">
            <h2>Source Performance</h2>
            <table>
                <thead>
                    <tr><th>Source</th><th>Fetched</th><th>Selected</th><th>Rate</th><th>Avg Score</th></tr>
                </thead>
                <tbody>{source_rows or '<tr><td colspan="5" style="text-align:center;color:#94a3b8;">No data</td></tr>'}</tbody>
            </table>
        </div>

        <p class="footer">Generated by Newsletter Analytics</p>
    </div>
</body>
</html>"""

    output_path.write_text(html, encoding="utf-8")
    return output_path


def generate_report(db_path: Optional[Path] = None, output_path: Optional[Path] = None, days: int = 30):
    """Generate analytics report (main entry point)."""
    db = AnalyticsDB(db_path)

    if output_path:
        return generate_html_report(db, output_path, days)
    else:
        # Print to console
        trends = db.get_trend_data(days)
        sources = db.get_source_performance(days)
        print_trends(trends, f"Last {days} Days Performance")
        print_source_performance(sources)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Newsletter Analytics Dashboard")
    parser.add_argument("--date", help="Show stats for specific issue date (YYYY-MM-DD)")
    parser.add_argument("--days", type=int, default=30, help="Number of days for trends")
    parser.add_argument("--db", help="Path to SQLite database")
    parser.add_argument("--output", help="Output HTML report to file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    db_path = Path(args.db) if args.db else None
    db = AnalyticsDB(db_path)

    if args.date:
        # Show specific issue stats
        stats = db.get_issue_stats(args.date)
        if args.json:
            print(json.dumps(stats, indent=2))
        else:
            print_issue_stats(stats)
    elif args.output:
        # Generate HTML report
        output_path = Path(args.output)
        generate_html_report(db, output_path, args.days)
        print(f"Report saved to: {output_path}")
    else:
        # Show trends
        trends = db.get_trend_data(args.days)
        sources = db.get_source_performance(args.days)

        if args.json:
            print(json.dumps({"trends": trends, "sources": sources}, indent=2))
        else:
            print_trends(trends, f"Last {args.days} Days Performance")
            print_source_performance(sources)


if __name__ == "__main__":
    main()
