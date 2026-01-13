"""SQLite storage layer for newsletter analytics."""

import hashlib
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_DB_PATH = Path(__file__).parent.parent / "analytics.db"


def hash_email(email: str) -> str:
    """Hash email for privacy-preserving storage."""
    return hashlib.sha256(email.lower().strip().encode()).hexdigest()[:16]


def hash_ip(ip: str) -> str:
    """Hash IP address for privacy."""
    if not ip:
        return ""
    return hashlib.sha256(ip.encode()).hexdigest()[:12]


class AnalyticsDB:
    """SQLite database for newsletter analytics."""

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or DEFAULT_DB_PATH
        self._init_db()

    def _init_db(self):
        """Initialize database schema."""
        with self._connect() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS opens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_date TEXT NOT NULL,
                    subscriber_hash TEXT NOT NULL,
                    opened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    user_agent TEXT,
                    ip_hash TEXT
                );

                CREATE TABLE IF NOT EXISTS clicks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_date TEXT NOT NULL,
                    subscriber_hash TEXT NOT NULL,
                    link_url TEXT NOT NULL,
                    link_type TEXT,
                    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS source_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_date TEXT NOT NULL,
                    source TEXT NOT NULL,
                    papers_fetched INTEGER DEFAULT 0,
                    papers_selected INTEGER DEFAULT 0,
                    avg_score REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS social_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_date TEXT NOT NULL,
                    platform TEXT NOT NULL,
                    post_type TEXT,
                    posted_at TIMESTAMP,
                    post_id TEXT
                );

                CREATE TABLE IF NOT EXISTS sends (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_date TEXT NOT NULL,
                    total_sent INTEGER DEFAULT 0,
                    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                CREATE INDEX IF NOT EXISTS idx_opens_issue ON opens(issue_date);
                CREATE INDEX IF NOT EXISTS idx_clicks_issue ON clicks(issue_date);
                CREATE INDEX IF NOT EXISTS idx_source_metrics_issue ON source_metrics(issue_date);
            """)

    @contextmanager
    def _connect(self):
        """Context manager for database connections."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def record_send(self, issue_date: str, total_sent: int):
        """Record newsletter send event."""
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO sends (issue_date, total_sent) VALUES (?, ?)",
                (issue_date, total_sent),
            )

    def record_open(
        self,
        issue_date: str,
        subscriber_hash: str,
        user_agent: Optional[str] = None,
        ip_address: Optional[str] = None,
    ):
        """Record an email open event."""
        with self._connect() as conn:
            conn.execute(
                """INSERT INTO opens (issue_date, subscriber_hash, user_agent, ip_hash)
                   VALUES (?, ?, ?, ?)""",
                (issue_date, subscriber_hash, user_agent, hash_ip(ip_address or "")),
            )

    def record_click(
        self,
        issue_date: str,
        subscriber_hash: str,
        link_url: str,
        link_type: Optional[str] = None,
    ):
        """Record a link click event."""
        with self._connect() as conn:
            conn.execute(
                """INSERT INTO clicks (issue_date, subscriber_hash, link_url, link_type)
                   VALUES (?, ?, ?, ?)""",
                (issue_date, subscriber_hash, link_url, link_type),
            )

    def record_source_metrics(
        self,
        issue_date: str,
        source: str,
        papers_fetched: int,
        papers_selected: int,
        avg_score: Optional[float] = None,
    ):
        """Record paper source performance metrics."""
        with self._connect() as conn:
            conn.execute(
                """INSERT INTO source_metrics
                   (issue_date, source, papers_fetched, papers_selected, avg_score)
                   VALUES (?, ?, ?, ?, ?)""",
                (issue_date, source, papers_fetched, papers_selected, avg_score),
            )

    def record_social_post(
        self,
        issue_date: str,
        platform: str,
        post_type: Optional[str] = None,
        post_id: Optional[str] = None,
    ):
        """Record social media post."""
        with self._connect() as conn:
            conn.execute(
                """INSERT INTO social_metrics (issue_date, platform, post_type, posted_at, post_id)
                   VALUES (?, ?, ?, ?, ?)""",
                (issue_date, platform, post_type, datetime.utcnow().isoformat(), post_id),
            )

    def get_issue_stats(self, issue_date: str) -> Dict[str, Any]:
        """Get comprehensive stats for a specific issue."""
        with self._connect() as conn:
            # Get send count
            send_row = conn.execute(
                "SELECT total_sent FROM sends WHERE issue_date = ? ORDER BY sent_at DESC LIMIT 1",
                (issue_date,),
            ).fetchone()
            total_sent = send_row["total_sent"] if send_row else 0

            # Get unique opens
            opens_row = conn.execute(
                "SELECT COUNT(DISTINCT subscriber_hash) as unique_opens, COUNT(*) as total_opens FROM opens WHERE issue_date = ?",
                (issue_date,),
            ).fetchone()

            # Get unique clicks
            clicks_row = conn.execute(
                "SELECT COUNT(DISTINCT subscriber_hash) as unique_clickers, COUNT(*) as total_clicks FROM clicks WHERE issue_date = ?",
                (issue_date,),
            ).fetchone()

            # Get top clicked links
            top_links = conn.execute(
                """SELECT link_url, link_type, COUNT(*) as click_count
                   FROM clicks WHERE issue_date = ?
                   GROUP BY link_url ORDER BY click_count DESC LIMIT 10""",
                (issue_date,),
            ).fetchall()

            # Get source metrics
            sources = conn.execute(
                """SELECT source, papers_fetched, papers_selected, avg_score
                   FROM source_metrics WHERE issue_date = ?""",
                (issue_date,),
            ).fetchall()

            unique_opens = opens_row["unique_opens"] if opens_row else 0
            unique_clickers = clicks_row["unique_clickers"] if clicks_row else 0

            return {
                "issue_date": issue_date,
                "total_sent": total_sent,
                "unique_opens": unique_opens,
                "total_opens": opens_row["total_opens"] if opens_row else 0,
                "open_rate": (unique_opens / total_sent * 100) if total_sent > 0 else 0,
                "unique_clickers": unique_clickers,
                "total_clicks": clicks_row["total_clicks"] if clicks_row else 0,
                "click_rate": (unique_clickers / total_sent * 100) if total_sent > 0 else 0,
                "top_links": [dict(row) for row in top_links],
                "sources": [dict(row) for row in sources],
            }

    def get_trend_data(self, days: int = 30) -> List[Dict[str, Any]]:
        """Get trend data for the last N days."""
        cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        with self._connect() as conn:
            rows = conn.execute(
                """SELECT
                       s.issue_date,
                       s.total_sent,
                       COUNT(DISTINCT o.subscriber_hash) as unique_opens,
                       COUNT(DISTINCT c.subscriber_hash) as unique_clickers
                   FROM sends s
                   LEFT JOIN opens o ON s.issue_date = o.issue_date
                   LEFT JOIN clicks c ON s.issue_date = c.issue_date
                   WHERE s.issue_date >= ?
                   GROUP BY s.issue_date
                   ORDER BY s.issue_date DESC""",
                (cutoff,),
            ).fetchall()
            return [dict(row) for row in rows]

    def get_source_performance(self, days: int = 30) -> List[Dict[str, Any]]:
        """Get aggregated source performance over time."""
        cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        with self._connect() as conn:
            rows = conn.execute(
                """SELECT
                       source,
                       SUM(papers_fetched) as total_fetched,
                       SUM(papers_selected) as total_selected,
                       AVG(avg_score) as avg_score,
                       COUNT(*) as issue_count
                   FROM source_metrics
                   WHERE issue_date >= ?
                   GROUP BY source
                   ORDER BY total_selected DESC""",
                (cutoff,),
            ).fetchall()
            return [dict(row) for row in rows]
