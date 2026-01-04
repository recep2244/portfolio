#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ISSUE_DATE="${1:-today}"

# Load environment variables from .env if it exists
if [ -f "$ROOT_DIR/newsletter/.env" ]; then
  set -a
  source "$ROOT_DIR/newsletter/.env"
  set +a
fi

write_csv_from_env() {
  local path="$1"
  local var_name="$2"
  local value="${!var_name:-}"
  if [ ! -f "$path" ] && [ -n "$value" ]; then
    printf "%s" "$value" > "$path"
  fi
}

write_csv_from_env "$ROOT_DIR/newsletter/preview_subscribers.csv" "NEWSLETTER_PREVIEW_SUBSCRIBERS_CSV"

python3 "$ROOT_DIR/newsletter/generate_issue.py" \
  --issue-date "$ISSUE_DATE" \
  --config "$ROOT_DIR/newsletter/generate_config.json" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

python3 "$ROOT_DIR/newsletter/newsletter_to_md.py" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Weekly Digest on Fridays
if [ "$(date +%u)" = "5" ]; then
  echo "📅 Friday detected: Generating Weekly Digest..."
  python3 "$ROOT_DIR/newsletter/generate_weekly_digest.py" \
    --issues-dir "$ROOT_DIR/newsletter/issues"
fi

PREVIEW_LIST="$ROOT_DIR/newsletter/preview_subscribers.csv"
if [ ! -f "$PREVIEW_LIST" ]; then
  echo "Error: preview_subscribers.csv not found. Aborting preview send."
  exit 1
fi

if [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
  echo "Warning: Missing Gmail credentials. Rendering preview only."
  python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
    --issue-date "$ISSUE_DATE" \
    --issues-dir "$ROOT_DIR/newsletter/issues" \
    --subscribers "$PREVIEW_LIST" \
    --template-html "$ROOT_DIR/newsletter/template.html" \
    --template-text "$ROOT_DIR/newsletter/template.txt" \
    --frequency daily \
    --render-only
else
  python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
    --issue-date "$ISSUE_DATE" \
    --issues-dir "$ROOT_DIR/newsletter/issues" \
    --subscribers "$PREVIEW_LIST" \
    --template-html "$ROOT_DIR/newsletter/template.html" \
    --template-text "$ROOT_DIR/newsletter/template.txt" \
    --frequency daily
fi

echo "Preview complete. After approval, run run_send_confirmed.sh."
