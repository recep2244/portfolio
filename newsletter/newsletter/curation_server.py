#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
from datetime import datetime
from html import unescape
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

DEFAULT_TIMEZONE = "Europe/London"

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


def run_python(script_path, args, cwd):
    cmd = [os.environ.get("PYTHON", "python3"), str(script_path)] + args
    subprocess.run(cmd, check=True, cwd=cwd)

def is_truthy(value):
    return str(value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def write_sent_marker(path, issue_date, timezone):
    payload = {
        "issue_date": issue_date,
        "sent_at": datetime.now(timezone).isoformat(),
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_approval_marker(path, issue_date, timezone):
    payload = {
        "issue_date": issue_date,
        "approved_at": datetime.now(timezone).isoformat(),
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def sync_archive(root_dir, issue_date):
    result = {"status": "skipped", "message": ""}
    if not is_truthy(os.getenv("NEWSLETTER_SYNC_ARCHIVE")):
        return result
    try:
        subprocess.run(
            ["git", "add", "content/newsletter"],
            cwd=root_dir,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=root_dir,
            check=False,
        )
        if diff.returncode == 0:
            result["status"] = "no_changes"
            return result
        commit_message = os.getenv("NEWSLETTER_SYNC_COMMIT_MESSAGE") or f"Sync newsletter archive ({issue_date})"
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=root_dir,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        result["status"] = "committed"
        if is_truthy(os.getenv("NEWSLETTER_SYNC_PUSH")):
            subprocess.run(
                ["git", "push"],
                cwd=root_dir,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            result["status"] = "pushed"
        return result
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        result["status"] = "failed"
        result["message"] = str(exc)
        return result


def _parse_int_env(key, default):
    value = os.getenv(key)
    if value is None or value == "":
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _send_timezone(default_tz):
    name = (os.getenv("NEWSLETTER_SEND_TZ") or os.getenv("NEWSLETTER_TIMEZONE") or "").strip()
    if not name:
        return default_tz
    try:
        return ZoneInfo(name)
    except Exception:
        return default_tz


def should_send_on_approval(default_tz):
    tz = _send_timezone(default_tz)
    now = datetime.now(tz)
    send_hour = _parse_int_env("NEWSLETTER_SEND_HOUR", 9)
    send_minute = _parse_int_env("NEWSLETTER_SEND_MINUTE", 0)
    target = now.replace(hour=send_hour, minute=send_minute, second=0, microsecond=0)
    return now >= target


class CurationServer(BaseHTTPRequestHandler):
    def _send(self, status, payload, content_type="application/json"):
        body = payload if isinstance(payload, (bytes, bytearray)) else json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _load_issue(self):
        if not self.server.issue_path.exists():
            return None
        with self.server.issue_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _fetch_title(self, url):
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=15) as resp:
            raw = resp.read(200000)
            encoding = resp.headers.get_content_charset() or "utf-8"
        text = raw.decode(encoding, errors="replace")
        meta_matches = re.findall(
            r'<meta[^>]+(?:property|name)=["\'](?:og:title|twitter:title)["\'][^>]*content=["\']([^"\']+)["\']',
            text,
            flags=re.IGNORECASE,
        )
        if meta_matches:
            return unescape(meta_matches[0]).strip()
        title_match = re.search(r"<title[^>]*>(.*?)</title>", text, flags=re.IGNORECASE | re.DOTALL)
        if title_match:
            return unescape(title_match.group(1)).strip()
        return ""

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
        if parsed.path == "/fetch-title":
            params = parse_qs(parsed.query or "")
            url = (params.get("url") or [""])[0].strip()
            if not url:
                self._send(400, {"error": "url is required"})
                return
            if not url.startswith(("http://", "https://")):
                self._send(400, {"error": "url must start with http:// or https://"})
                return
            try:
                title = self._fetch_title(url)
            except Exception as exc:
                self._send(200, {"title": "", "error": str(exc)})
                return
            self._send(200, {"title": title})
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
            if self.server.sent_marker.exists() and not is_truthy(
                os.getenv("NEWSLETTER_ALLOW_RESEND")
            ):
                sent_data = {}
                try:
                    sent_data = json.loads(self.server.sent_marker.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    pass
                self._send(
                    409,
                    {
                        "error": "Issue already sent.",
                        "sent_at": sent_data.get("sent_at", ""),
                    },
                )
                return
            try:
                self._save_issue(payload)
                rendered = False
                if is_truthy(os.getenv("NEWSLETTER_DELAY_SEND")):
                    write_approval_marker(
                        self.server.approval_marker,
                        self.server.issue_date,
                        self.server.timezone,
                    )
                    run_python(
                        self.server.newsletter_to_md,
                        ["--issues-dir", str(self.server.issues_dir)],
                        self.server.root_dir,
                    )
                    rendered = True
                    if not should_send_on_approval(self.server.timezone):
                        self._send(
                            200,
                            {"message": "Approved. Scheduled to send at the configured time."},
                        )
                        return
                run_python(
                    self.server.sync_subscribers,
                    [
                        "--subscribers",
                        str(self.server.subscribers_list),
                    ],
                    self.server.root_dir,
                )
                if not rendered:
                    run_python(
                        self.server.newsletter_to_md,
                        ["--issues-dir", str(self.server.issues_dir)],
                        self.server.root_dir,
                    )
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
                        "--frequency",
                        self.server.send_frequency,
                    ],
                    self.server.root_dir,
                )
                social_error = None
                try:
                    run_python(
                        self.server.social_post,
                        [
                            "--issue",
                            str(self.server.issue_path),
                        ],
                        self.server.root_dir,
                    )
                except subprocess.CalledProcessError as exc:
                    social_error = exc
                write_sent_marker(self.server.sent_marker, self.server.issue_date, self.server.timezone)
            except subprocess.CalledProcessError as exc:
                self._send(500, {"error": f"Send failed: {exc}"})
                return
            message = "Sent to all subscribers."
            if social_error:
                message = f"{message} Social post failed: {social_error}"
            sync_result = sync_archive(self.server.root_dir, self.server.issue_date)
            if sync_result["status"] == "failed":
                message = f"{message} Archive sync failed: {sync_result['message']}"
            elif sync_result["status"] == "committed":
                message = f"{message} Archive synced."
            elif sync_result["status"] == "pushed":
                message = f"{message} Archive synced and pushed."
            self._send(200, {"message": message})
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
    if load_dotenv:
        load_dotenv(dotenv_path=newsletter_dir / ".env", override=False)
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
    server.sent_marker = issues_dir / f"{issue_date}.sent"
    server.approval_marker = issues_dir / f"{issue_date}.approved"
    server.html_path = newsletter_dir / "curate_issue.html"
    server.preview_list = newsletter_dir / "preview_subscribers.csv"
    server.subscribers_list = newsletter_dir / "subscribers.csv"
    server.template_html = newsletter_dir / "template.html"
    server.template_text = newsletter_dir / "template.txt"
    server.send_newsletter = newsletter_dir / "send_newsletter.py"
    server.newsletter_to_md = newsletter_dir / "newsletter_to_md.py"
    server.social_post = newsletter_dir / "social_post.py"
    server.sync_subscribers = newsletter_dir / "sync_subscribers_from_gmail.py"
    server.timezone = tz
    send_frequency = (os.getenv("NEWSLETTER_SEND_FREQUENCY") or "daily").strip().lower()
    server.send_frequency = send_frequency if send_frequency in {"daily", "weekly"} else "daily"

    print(f"Curation server running at http://127.0.0.1:{args.port}")
    print(f"Issue date: {issue_date}")
    server.serve_forever()


if __name__ == "__main__":
    main()
