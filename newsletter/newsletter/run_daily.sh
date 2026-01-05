#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

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

write_csv_from_env "$ROOT_DIR/newsletter/subscribers.csv" "NEWSLETTER_SUBSCRIBERS_CSV"
write_csv_from_env "$ROOT_DIR/newsletter/preview_subscribers.csv" "NEWSLETTER_PREVIEW_SUBSCRIBERS_CSV"

if [ "${NEWSLETTER_SYNC_SUBSCRIBERS:-1}" = "1" ]; then
  python3 "$ROOT_DIR/newsletter/sync_subscribers_from_gmail.py" \
    --subscribers "$ROOT_DIR/newsletter/subscribers.csv" || echo "Warning: subscriber sync failed."
fi

python3 "$ROOT_DIR/newsletter/generate_issue.py" \
  --issue-date today \
  --config "$ROOT_DIR/newsletter/generate_config.json" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Convert to Hugo Content
python3 "$ROOT_DIR/newsletter/newsletter_to_md.py" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Weekly Digest on Fridays
if [ "$(date +%u)" = "5" ]; then
  echo "📅 Friday detected: Generating Weekly Digest..."
  python3 "$ROOT_DIR/newsletter/generate_weekly_digest.py" \
    --issues-dir "$ROOT_DIR/newsletter/issues"
fi

PREVIEW_LIST="$ROOT_DIR/newsletter/preview_subscribers.csv"

if [ "${NEWSLETTER_SEND_CURATION_REMINDER:-}" = "1" ]; then
  if [ ! -f "$PREVIEW_LIST" ]; then
    echo "Error: preview_subscribers.csv not found. Aborting curation reminder."
    PREVIEW_LIST=""
  fi
  CURATION_TZ="${NEWSLETTER_CURATION_TZ:-Europe/London}"
  CURATION_HOUR="${NEWSLETTER_CURATION_HOUR:-10}"
  CURATION_MINUTE="${NEWSLETTER_CURATION_MINUTE:-00}"
  CURATION_WINDOW_MINUTES="${NEWSLETTER_CURATION_WINDOW_MINUTES:-10}"
  SHOULD_SEND="$(python3 - <<PY
from datetime import datetime, time
from zoneinfo import ZoneInfo

tz = ZoneInfo("${CURATION_TZ}")
now = datetime.now(tz)
target = datetime.combine(now.date(), time(int("${CURATION_HOUR}"), int("${CURATION_MINUTE}")), tz)
delta_minutes = abs((now - target).total_seconds()) / 60
print("yes" if delta_minutes <= int("${CURATION_WINDOW_MINUTES}") else "no")
PY
)"

  if [ "${NEWSLETTER_START_CURATION_SERVER:-0}" = "1" ]; then
    PORT="${NEWSLETTER_CURATION_PORT:-5050}"
    LOG_PATH="${ROOT_DIR}/newsletter/curation_server.log"
    nohup "$ROOT_DIR/newsletter/run_curation_server.sh" "today" "$PORT" > "$LOG_PATH" 2>&1 &
    sleep 2
  fi

  if [ "$SHOULD_SEND" = "yes" ]; then
    if [ -z "$PREVIEW_LIST" ]; then
      echo "Warning: Missing preview list. Skipping curation reminder email."
    elif [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
      echo "Warning: Missing Gmail credentials. Skipping curation reminder email."
    else
      PORT="${NEWSLETTER_CURATION_PORT:-5050}"
      CURATION_URL="${NEWSLETTER_CURATION_URL:-http://127.0.0.1:${PORT}}"
      python3 "$ROOT_DIR/newsletter/send_reminder.py" \
        --preview-list "$PREVIEW_LIST" \
        --subject "Protein Design Digest: Curation Ready [$(date +%Y-%m-%d)]" \
        --body "Your daily curation is ready. Open ${CURATION_URL} to curate and approve." \
        --issue "$ROOT_DIR/newsletter/issues/$(date +%Y-%m-%d).json" || echo "Warning: curation reminder failed."
    fi

    echo "Curation reminder sent. Social posting will run after approval."
  else
    echo "Skipping curation reminder: runs within ${CURATION_WINDOW_MINUTES} min of ${CURATION_HOUR}:${CURATION_MINUTE} $CURATION_TZ."
  fi
fi

if [ "${NEWSLETTER_SEND_PREVIEW:-0}" = "1" ]; then
  PREVIEW_LIST="$ROOT_DIR/newsletter/preview_subscribers.csv"
  if [ ! -f "$PREVIEW_LIST" ]; then
    echo "Error: preview_subscribers.csv not found. Aborting preview send."
    exit 1
  fi

  if [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
    echo "Warning: Missing Gmail credentials. Rendering preview only."
    python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
      --issue-date today \
      --issues-dir "$ROOT_DIR/newsletter/issues" \
      --subscribers "$PREVIEW_LIST" \
      --template-html "$ROOT_DIR/newsletter/template.html" \
      --template-text "$ROOT_DIR/newsletter/template.txt" \
      --frequency daily \
      --render-only
  else
    python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
      --issue-date today \
      --issues-dir "$ROOT_DIR/newsletter/issues" \
      --subscribers "$PREVIEW_LIST" \
      --template-html "$ROOT_DIR/newsletter/template.html" \
      --template-text "$ROOT_DIR/newsletter/template.txt" \
      --frequency daily || echo "Warning: preview send failed."
  fi
else
  echo "Preview send disabled. Set NEWSLETTER_SEND_PREVIEW=1 to send previews."
fi

echo "Daily run complete. Run run_send_confirmed.sh after approval to email everyone."
