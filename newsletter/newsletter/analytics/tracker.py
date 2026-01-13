#!/usr/bin/env python3
"""FastAPI tracking server for newsletter analytics."""

import argparse
import base64
import os
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse

try:
    from fastapi import FastAPI, Request, Response, Query
    from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
    import uvicorn
except ImportError:
    FastAPI = None

from .storage import AnalyticsDB

# 1x1 transparent GIF
TRACKING_PIXEL = base64.b64decode(
    "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
)

app = FastAPI(title="Newsletter Analytics", docs_url="/docs") if FastAPI else None
db: Optional[AnalyticsDB] = None


def get_db() -> AnalyticsDB:
    """Get or create database instance."""
    global db
    if db is None:
        db_path = os.getenv("ANALYTICS_DB_PATH")
        db = AnalyticsDB(Path(db_path) if db_path else None)
    return db


if app:
    @app.get("/pixel/{issue_date}/{subscriber_hash}.gif")
    async def tracking_pixel(
        issue_date: str,
        subscriber_hash: str,
        request: Request,
    ):
        """Return tracking pixel and record open."""
        user_agent = request.headers.get("user-agent", "")
        ip = request.client.host if request.client else ""

        get_db().record_open(
            issue_date=issue_date,
            subscriber_hash=subscriber_hash,
            user_agent=user_agent,
            ip_address=ip,
        )

        return Response(
            content=TRACKING_PIXEL,
            media_type="image/gif",
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
            },
        )

    @app.get("/click/{issue_date}/{subscriber_hash}")
    async def track_click(
        issue_date: str,
        subscriber_hash: str,
        url: str = Query(..., description="Target URL to redirect to"),
        link_type: Optional[str] = Query(None, description="Type of link"),
    ):
        """Record click and redirect to target URL."""
        decoded_url = unquote(url)

        # Validate URL
        parsed = urlparse(decoded_url)
        if not parsed.scheme or not parsed.netloc:
            return JSONResponse({"error": "Invalid URL"}, status_code=400)

        get_db().record_click(
            issue_date=issue_date,
            subscriber_hash=subscriber_hash,
            link_url=decoded_url,
            link_type=link_type,
        )

        return RedirectResponse(url=decoded_url, status_code=302)

    @app.get("/api/stats/{issue_date}")
    async def get_stats(issue_date: str):
        """Get statistics for a specific issue."""
        stats = get_db().get_issue_stats(issue_date)
        return JSONResponse(stats)

    @app.get("/api/trends")
    async def get_trends(days: int = Query(30, ge=1, le=365)):
        """Get trend data for the last N days."""
        trends = get_db().get_trend_data(days)
        return JSONResponse({"days": days, "data": trends})

    @app.get("/api/sources")
    async def get_sources(days: int = Query(30, ge=1, le=365)):
        """Get source performance data."""
        sources = get_db().get_source_performance(days)
        return JSONResponse({"days": days, "data": sources})

    @app.get("/dashboard", response_class=HTMLResponse)
    async def dashboard(days: int = Query(30, ge=1, le=365)):
        """HTML dashboard for analytics."""
        trends = get_db().get_trend_data(days)
        sources = get_db().get_source_performance(days)

        # Calculate summary stats
        total_sent = sum(t.get("total_sent", 0) for t in trends)
        total_opens = sum(t.get("unique_opens", 0) for t in trends)
        total_clicks = sum(t.get("unique_clickers", 0) for t in trends)
        avg_open_rate = (total_opens / total_sent * 100) if total_sent > 0 else 0
        avg_click_rate = (total_clicks / total_sent * 100) if total_sent > 0 else 0

        # Build trend rows
        trend_rows = ""
        for t in trends[:15]:
            issue_date = t.get("issue_date", "")
            sent = t.get("total_sent", 0)
            opens = t.get("unique_opens", 0)
            clicks = t.get("unique_clickers", 0)
            open_rate = (opens / sent * 100) if sent > 0 else 0
            click_rate = (clicks / sent * 100) if sent > 0 else 0
            trend_rows += f"""
            <tr>
                <td>{issue_date}</td>
                <td>{sent}</td>
                <td>{opens} ({open_rate:.1f}%)</td>
                <td>{clicks} ({click_rate:.1f}%)</td>
            </tr>"""

        # Build source rows
        source_rows = ""
        for s in sources:
            source = s.get("source", "")
            fetched = s.get("total_fetched", 0)
            selected = s.get("total_selected", 0)
            avg_score = s.get("avg_score", 0) or 0
            selection_rate = (selected / fetched * 100) if fetched > 0 else 0
            source_rows += f"""
            <tr>
                <td>{source}</td>
                <td>{fetched}</td>
                <td>{selected}</td>
                <td>{selection_rate:.1f}%</td>
                <td>{avg_score:.1f}</td>
            </tr>"""

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Newsletter Analytics Dashboard</title>
            <style>
                * {{ box-sizing: border-box; margin: 0; padding: 0; }}
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; padding: 2rem; }}
                .container {{ max-width: 1200px; margin: 0 auto; }}
                h1 {{ font-size: 2rem; font-weight: 700; margin-bottom: 2rem; color: #0f172a; }}
                h2 {{ font-size: 1.25rem; font-weight: 600; margin: 2rem 0 1rem; color: #334155; }}
                .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }}
                .stat-card {{ background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
                .stat-value {{ font-size: 2rem; font-weight: 700; color: #0f172a; }}
                .stat-label {{ font-size: 0.875rem; color: #64748b; margin-top: 0.25rem; }}
                table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
                th, td {{ padding: 1rem; text-align: left; border-bottom: 1px solid #e2e8f0; }}
                th {{ background: #f1f5f9; font-weight: 600; color: #475569; }}
                tr:hover {{ background: #f8fafc; }}
                .section {{ margin-bottom: 3rem; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Protein Design Digest Analytics</h1>
                <p style="color: #64748b; margin-bottom: 2rem;">Last {days} days</p>

                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-value">{total_sent}</div>
                        <div class="stat-label">Total Emails Sent</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{total_opens}</div>
                        <div class="stat-label">Total Opens</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{avg_open_rate:.1f}%</div>
                        <div class="stat-label">Avg Open Rate</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{avg_click_rate:.1f}%</div>
                        <div class="stat-label">Avg Click Rate</div>
                    </div>
                </div>

                <div class="section">
                    <h2>Recent Issues</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Issue Date</th>
                                <th>Sent</th>
                                <th>Opens</th>
                                <th>Clicks</th>
                            </tr>
                        </thead>
                        <tbody>
                            {trend_rows if trend_rows else '<tr><td colspan="4" style="text-align:center;color:#94a3b8;">No data yet</td></tr>'}
                        </tbody>
                    </table>
                </div>

                <div class="section">
                    <h2>Source Performance</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Source</th>
                                <th>Papers Fetched</th>
                                <th>Papers Selected</th>
                                <th>Selection Rate</th>
                                <th>Avg Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            {source_rows if source_rows else '<tr><td colspan="5" style="text-align:center;color:#94a3b8;">No data yet</td></tr>'}
                        </tbody>
                    </table>
                </div>

                <p style="color: #94a3b8; font-size: 0.875rem; margin-top: 2rem;">
                    API endpoints: <a href="/api/trends">/api/trends</a> | <a href="/api/sources">/api/sources</a> | <a href="/docs">/docs</a>
                </p>
            </div>
        </body>
        </html>
        """
        return HTMLResponse(html)

    @app.get("/health")
    async def health():
        """Health check endpoint."""
        return {"status": "ok"}


def main():
    """Run the tracking server."""
    if not FastAPI:
        print("FastAPI not installed. Run: pip install fastapi uvicorn")
        return

    parser = argparse.ArgumentParser(description="Newsletter Analytics Tracker")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8080, help="Port to listen on")
    parser.add_argument("--db", help="Path to SQLite database")
    args = parser.parse_args()

    if args.db:
        os.environ["ANALYTICS_DB_PATH"] = args.db

    print(f"Starting analytics tracker on http://{args.host}:{args.port}")
    print(f"Dashboard: http://{args.host}:{args.port}/dashboard")
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
