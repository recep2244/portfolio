#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

DEFAULT_TIMEZONE = "Europe/London"


def run_python(script_path, args, cwd):
    cmd = [os.environ.get("PYTHON", "python3"), str(script_path)] + args
    subprocess.run(cmd, check=True, cwd=cwd)


class CurationServer(BaseHTTPRequestHandler):
    def _send(self, status, payload, content_type="application/json"):
        body = payload if isinstance(payload, (bytes, bytearray)) else json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _load_issue(self):
        if not self.server.issue_path.exists():
            return None
        with self.server.issue_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _save_issue(self, data):
        with self.server.issue_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True)
            f.write("\n")

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            html_path = self.server.html_path
            if not html_path.exists():
                self._send(404, {"error": "curate_issue.html not found"})
                return
            content = html_path.read_bytes()
            self._send(200, content, content_type="text/html; charset=utf-8")
            return
        if parsed.path == "/issue.json":
            issue = self._load_issue()
            if not issue:
                self._send(404, {"error": "Issue not found"})
                return
            self._send(200, issue)
            return
        self._send(404, {"error": "Not found"})

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b""
        try:
            payload = json.loads(raw.decode("utf-8")) if raw else {}
        except json.JSONDecodeError:
            self._send(400, {"error": "Invalid JSON"})
            return

        if parsed.path == "/send-preview":
            try:
                self._save_issue(payload)
                run_python(self.server.newsletter_to_md, ["--issues-dir", str(self.server.issues_dir)], self.server.root_dir)
                run_python(
                    self.server.send_newsletter,
                    [
                        "--issue-date",
                        self.server.issue_date,
                        "--issues-dir",
                        str(self.server.issues_dir),
                        "--subscribers",
                        str(self.server.preview_list),
                        "--template-html",
                        str(self.server.template_html),
                        "--template-text",
                        str(self.server.template_text),
                    ],
                    self.server.root_dir,
                )
            except subprocess.CalledProcessError as exc:
                self._send(500, {"error": f"Preview send failed: {exc}"})
                return
            self._send(200, {"message": "Preview sent to your preview list."})
            return

        if parsed.path == "/approve-send":
            try:
                self._save_issue(payload)
                run_python(self.server.newsletter_to_md, ["--issues-dir", str(self.server.issues_dir)], self.server.root_dir)
                run_python(
                    self.server.send_newsletter,
                    [
                        "--issue-date",
                        self.server.issue_date,
                        "--issues-dir",
                        str(self.server.issues_dir),
                        "--subscribers",
                        str(self.server.subscribers_list),
                        "--template-html",
                        str(self.server.template_html),
                        "--template-text",
                        str(self.server.template_text),
                    ],
                    self.server.root_dir,
                )
                run_python(
                    self.server.social_post,
                    [
                        "--issue",
                        str(self.server.issue_path),
                    ],
                    self.server.root_dir,
                )
            except subprocess.CalledProcessError as exc:
                self._send(500, {"error": f"Send failed: {exc}"})
                return
            self._send(200, {"message": "Sent to all subscribers."})
            return

        self._send(404, {"error": "Not found"})


def ensure_issue(issue_date, root_dir, issues_dir, config_path):
    run_python(
        root_dir / "newsletter" / "generate_issue.py",
        ["--issue-date", issue_date, "--config", str(config_path), "--issues-dir", str(issues_dir)],
        root_dir,
    )


def main():
    parser = argparse.ArgumentParser(description="Local curation server")
    parser.add_argument("--issue-date", default="today")
    parser.add_argument("--port", type=int, default=5050)
    parser.add_argument("--timezone", default=DEFAULT_TIMEZONE)
    args = parser.parse_args()

    root_dir = Path(__file__).resolve().parent.parent
    newsletter_dir = root_dir / "newsletter"
    issues_dir = newsletter_dir / "issues"
    config_path = newsletter_dir / "generate_config.json"

    tz = ZoneInfo(args.timezone)
    if args.issue_date == "today":
        issue_date = datetime.now(tz).date().isoformat()
    else:
        issue_date = args.issue_date

    issues_dir.mkdir(parents=True, exist_ok=True)
    ensure_issue(issue_date, root_dir, issues_dir, config_path)

    issue_path = issues_dir / f"{issue_date}.json"
    server = HTTPServer(("127.0.0.1", args.port), CurationServer)
    server.root_dir = root_dir
    server.issue_date = issue_date
    server.issues_dir = issues_dir
    server.issue_path = issue_path
    server.html_path = newsletter_dir / "curate_issue.html"
    server.preview_list = newsletter_dir / "preview_subscribers.csv"
    server.subscribers_list = newsletter_dir / "subscribers.csv"
    server.template_html = newsletter_dir / "template.html"
    server.template_text = newsletter_dir / "template.txt"
    server.send_newsletter = newsletter_dir / "send_newsletter.py"
    server.newsletter_to_md = newsletter_dir / "newsletter_to_md.py"
    server.social_post = newsletter_dir / "social_post.py"

    print(f"Curation server running at http://127.0.0.1:{args.port}")
    print(f"Issue date: {issue_date}")
    server.serve_forever()


if __name__ == "__main__":
    main()
