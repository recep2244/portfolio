#!/usr/bin/env python3
"""Trending topics detection for newsletter content."""

import argparse
import json
import re
import sqlite3
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

DEFAULT_DB_PATH = Path(__file__).parent / "trending.db"

# Keywords to track (can be extended)
TRACKED_KEYWORDS = [
    # Methods
    "alphafold", "rosettafold", "esmfold", "openfold", "colabfold",
    "rfdiffusion", "proteinmpnn", "diffusion", "transformer",
    # Concepts
    "protein design", "de novo", "structure prediction", "docking",
    "molecular dynamics", "binding affinity", "drug discovery",
    "antibody", "enzyme", "binder", "scaffold",
    # Techniques
    "deep learning", "machine learning", "generative", "language model",
    "cryo-em", "crystallography", "nmr",
    # Applications
    "therapeutics", "vaccine", "cancer", "clinical trial",
    # Tools/Databases
    "pdb", "uniprot", "foldseek", "mmseqs2",
]


class TrendingDB:
    """SQLite database for tracking keyword trends."""

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or DEFAULT_DB_PATH
        self._init_db()

    def _init_db(self):
        with self._connect() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS keyword_counts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    keyword TEXT NOT NULL,
                    count INTEGER DEFAULT 0,
                    source TEXT,
                    UNIQUE(date, keyword, source)
                );

                CREATE TABLE IF NOT EXISTS paper_keywords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    paper_title TEXT NOT NULL,
                    keywords TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_keyword_date ON keyword_counts(date);
                CREATE INDEX IF NOT EXISTS idx_keyword_name ON keyword_counts(keyword);
            """)

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def record_keywords(self, date: str, keyword_counts: Dict[str, int], source: str = "all"):
        """Record keyword counts for a specific date."""
        with self._connect() as conn:
            for keyword, count in keyword_counts.items():
                conn.execute("""
                    INSERT INTO keyword_counts (date, keyword, count, source)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(date, keyword, source) DO UPDATE SET count = count + ?
                """, (date, keyword.lower(), count, source, count))

    def get_keyword_history(self, keyword: str, days: int = 30) -> List[Dict[str, Any]]:
        """Get historical counts for a keyword."""
        cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        with self._connect() as conn:
            rows = conn.execute("""
                SELECT date, SUM(count) as total
                FROM keyword_counts
                WHERE keyword = ? AND date >= ?
                GROUP BY date
                ORDER BY date
            """, (keyword.lower(), cutoff)).fetchall()
            return [dict(row) for row in rows]

    def get_trending(self, days: int = 7, min_count: int = 2) -> List[Dict[str, Any]]:
        """
        Get trending keywords by comparing this week vs last week.

        Returns keywords sorted by growth rate.
        """
        today = datetime.now().date()
        this_week_start = (today - timedelta(days=days)).strftime("%Y-%m-%d")
        last_week_start = (today - timedelta(days=days * 2)).strftime("%Y-%m-%d")
        last_week_end = (today - timedelta(days=days + 1)).strftime("%Y-%m-%d")

        with self._connect() as conn:
            # This week's counts
            this_week = conn.execute("""
                SELECT keyword, SUM(count) as total
                FROM keyword_counts
                WHERE date >= ?
                GROUP BY keyword
                HAVING total >= ?
            """, (this_week_start, min_count)).fetchall()

            # Last week's counts
            last_week = conn.execute("""
                SELECT keyword, SUM(count) as total
                FROM keyword_counts
                WHERE date >= ? AND date <= ?
                GROUP BY keyword
            """, (last_week_start, last_week_end)).fetchall()

        this_week_dict = {row["keyword"]: row["total"] for row in this_week}
        last_week_dict = {row["keyword"]: row["total"] for row in last_week}

        trending = []
        for keyword, this_count in this_week_dict.items():
            last_count = last_week_dict.get(keyword, 0)

            if last_count == 0:
                # New keyword this week
                growth = float('inf') if this_count >= min_count else 0
                growth_display = "NEW"
            else:
                growth = ((this_count - last_count) / last_count) * 100
                growth_display = f"+{growth:.0f}%" if growth > 0 else f"{growth:.0f}%"

            if growth > 0 or growth == float('inf'):
                trending.append({
                    "keyword": keyword,
                    "this_week": this_count,
                    "last_week": last_count,
                    "growth": growth,
                    "growth_display": growth_display,
                })

        # Sort by growth rate (NEW items first, then by percentage)
        trending.sort(key=lambda x: (x["growth"] != float('inf'), -x["growth"] if x["growth"] != float('inf') else 0))

        return trending[:10]  # Top 10 trending

    def get_top_keywords(self, days: int = 7, limit: int = 20) -> List[Dict[str, Any]]:
        """Get most frequent keywords in the period."""
        cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        with self._connect() as conn:
            rows = conn.execute("""
                SELECT keyword, SUM(count) as total
                FROM keyword_counts
                WHERE date >= ?
                GROUP BY keyword
                ORDER BY total DESC
                LIMIT ?
            """, (cutoff, limit)).fetchall()
            return [dict(row) for row in rows]


def extract_keywords(text: str, keyword_list: List[str] = None) -> Dict[str, int]:
    """Extract and count keywords from text."""
    keywords = keyword_list or TRACKED_KEYWORDS
    text_lower = text.lower()
    counts = Counter()

    for keyword in keywords:
        # Count occurrences (word boundary matching)
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        matches = len(re.findall(pattern, text_lower))
        if matches > 0:
            counts[keyword.lower()] = matches

    return dict(counts)


def analyze_papers(papers: List[Any], keyword_list: List[str] = None) -> Dict[str, int]:
    """Analyze a list of papers and extract keyword counts."""
    total_counts = Counter()

    for paper in papers:
        # Get title and summary
        if hasattr(paper, 'title'):
            title = paper.title
            summary = getattr(paper, 'summary', '') or ''
        elif isinstance(paper, dict):
            title = paper.get('title', '')
            summary = paper.get('summary', '') or paper.get('abstract', '') or ''
        else:
            continue

        text = f"{title} {summary}"
        counts = extract_keywords(text, keyword_list)
        total_counts.update(counts)

    return dict(total_counts)


def analyze_issue(issue_path: Path, keyword_list: List[str] = None) -> Dict[str, int]:
    """Analyze a newsletter issue JSON file."""
    with open(issue_path, 'r', encoding='utf-8') as f:
        issue = json.load(f)

    total_counts = Counter()

    # Analyze signal
    signal = issue.get('signal', {})
    if signal:
        text = f"{signal.get('title', '')} {signal.get('summary', '')}"
        total_counts.update(extract_keywords(text, keyword_list))

    # Analyze quick reads
    for item in issue.get('quick_reads', []):
        text = f"{item.get('title', '')} {item.get('abstract', '')}"
        total_counts.update(extract_keywords(text, keyword_list))

    # Analyze signal extras
    for item in issue.get('signal_extras', []):
        text = f"{item.get('title', '')} {item.get('abstract', '')}"
        total_counts.update(extract_keywords(text, keyword_list))

    # Analyze AI news
    for item in issue.get('ai_news', []):
        text = f"{item.get('title', '')} {item.get('abstract', '')}"
        total_counts.update(extract_keywords(text, keyword_list))

    return dict(total_counts)


def backfill_from_issues(issues_dir: Path, db: TrendingDB, days: int = 30):
    """Backfill trending database from existing issue files."""
    cutoff = datetime.now().date() - timedelta(days=days)

    for issue_path in issues_dir.glob("*.json"):
        try:
            date_str = issue_path.stem  # e.g., "2026-01-09"
            issue_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if issue_date < cutoff:
                continue

            counts = analyze_issue(issue_path)
            if counts:
                db.record_keywords(date_str, counts)
                print(f"Processed {date_str}: {len(counts)} keywords")
        except Exception as e:
            print(f"Error processing {issue_path}: {e}")


def format_trending_section(trending: List[Dict[str, Any]], top_keywords: List[Dict[str, Any]]) -> str:
    """Format trending data for newsletter inclusion."""
    if not trending and not top_keywords:
        return ""

    lines = []

    if trending:
        lines.append("**Trending This Week:**")
        for i, item in enumerate(trending[:5], 1):
            keyword = item['keyword'].title()
            growth = item['growth_display']
            lines.append(f"  {i}. {keyword} ({growth})")

    if top_keywords:
        lines.append("\n**Most Discussed:**")
        top_5 = top_keywords[:5]
        keywords_str = ", ".join(k['keyword'].title() for k in top_5)
        lines.append(f"  {keywords_str}")

    return "\n".join(lines)


def format_trending_html(trending: List[Dict[str, Any]]) -> str:
    """Format trending data as HTML for newsletter template."""
    if not trending:
        return ""

    items_html = ""
    for item in trending[:5]:
        keyword = item['keyword'].title()
        growth = item['growth_display']

        # Color based on growth
        if growth == "NEW":
            badge_style = "background:#dcfce7;color:#166534;"
        else:
            badge_style = "background:#dbeafe;color:#1e40af;"

        items_html += f'''
        <div style="display:inline-block;margin:4px;">
            <span style="font-family:Arial,sans-serif;font-size:13px;color:#334155;">{keyword}</span>
            <span style="font-family:Arial,sans-serif;font-size:11px;padding:2px 6px;border-radius:4px;{badge_style}">{growth}</span>
        </div>
        '''

    return f'''
    <div style="margin-top:30px;padding:20px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
        <div style="font-family:Arial,sans-serif;font-size:12px;color:#0b6e4f;font-weight:bold;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;">
            📈 Trending This Week
        </div>
        <div>
            {items_html}
        </div>
    </div>
    '''


def main():
    parser = argparse.ArgumentParser(description="Trending topics detection")
    parser.add_argument("--backfill", action="store_true", help="Backfill from existing issues")
    parser.add_argument("--issues-dir", default="newsletter/issues", help="Issues directory")
    parser.add_argument("--days", type=int, default=30, help="Days to analyze")
    parser.add_argument("--db", help="Path to trending database")
    parser.add_argument("--show", action="store_true", help="Show current trending topics")
    args = parser.parse_args()

    db_path = Path(args.db) if args.db else None
    db = TrendingDB(db_path)

    if args.backfill:
        issues_dir = Path(args.issues_dir)
        if issues_dir.exists():
            backfill_from_issues(issues_dir, db, args.days)
            print(f"\nBackfill complete from {issues_dir}")
        else:
            print(f"Issues directory not found: {issues_dir}")
        return

    if args.show or True:  # Default to showing
        print("\n" + "=" * 50)
        print("TRENDING TOPICS (This Week vs Last Week)")
        print("=" * 50)

        trending = db.get_trending(days=7)
        if trending:
            for i, item in enumerate(trending, 1):
                print(f"{i:2}. {item['keyword']:<20} {item['this_week']:>3} papers ({item['growth_display']})")
        else:
            print("No trending data yet. Run --backfill first.")

        print("\n" + "=" * 50)
        print("TOP KEYWORDS (Last 7 Days)")
        print("=" * 50)

        top = db.get_top_keywords(days=7)
        if top:
            for i, item in enumerate(top[:10], 1):
                print(f"{i:2}. {item['keyword']:<20} {item['total']:>3} mentions")
        else:
            print("No data yet.")


if __name__ == "__main__":
    main()
