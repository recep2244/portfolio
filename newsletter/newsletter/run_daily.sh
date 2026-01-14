#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

# Log rotation function - rotate logs if they exceed MAX_LOG_SIZE
rotate_logs() {
  local log_file="$1"
  local max_size="${2:-1048576}"  # 1MB default
  local max_backups="${3:-3}"

  if [ ! -f "$log_file" ]; then
    return
  fi

  local size
  size=$(stat -f%z "$log_file" 2>/dev/null || stat -c%s "$log_file" 2>/dev/null || echo "0")

  if [ "$size" -gt "$max_size" ]; then
    # Rotate existing backups
    for i in $(seq $((max_backups - 1)) -1 1); do
      if [ -f "${log_file}.${i}" ]; then
        mv "${log_file}.${i}" "${log_file}.$((i + 1))"
      fi
    done
    # Move current log to .1
    mv "$log_file" "${log_file}.1"
    # Remove oldest backup if it exists
    rm -f "${log_file}.$((max_backups + 1))"
    echo "Log rotated: $log_file"
  fi
}

# Rotate logs at startup
rotate_logs "$ROOT_DIR/newsletter/daily_cron.log" 1048576 3
rotate_logs "$ROOT_DIR/newsletter/curation_server.log" 524288 2

# Load environment variables from .env if it exists
if [ -f "$ROOT_DIR/newsletter/.env" ]; then
  set -a
  source "$ROOT_DIR/newsletter/.env"
  set +a
fi

PYTHON_BIN="${NEWSLETTER_PYTHON:-python3}"

DEFAULT_TZ="${NEWSLETTER_TIMEZONE:-Europe/London}"
TODAY_DATE="$($PYTHON_BIN - <<PY
from datetime import datetime
from zoneinfo import ZoneInfo
tz = ZoneInfo("${DEFAULT_TZ}")
print(datetime.now(tz).date().isoformat())
PY
)"

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
  "$PYTHON_BIN" "$ROOT_DIR/newsletter/sync_subscribers_from_gmail.py" \
    --subscribers "$ROOT_DIR/newsletter/subscribers.csv" || echo "Warning: subscriber sync failed."
fi

"$PYTHON_BIN" "$ROOT_DIR/newsletter/generate_issue.py" \
  --issue-date "$TODAY_DATE" \
  --config "$ROOT_DIR/newsletter/generate_config.json" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Convert to Hugo Content
if [ "${NEWSLETTER_SYNC_ARCHIVE_AT_CURATION:-0}" = "1" ]; then
  "$PYTHON_BIN" "$ROOT_DIR/newsletter/newsletter_to_md.py" \
    --issues-dir "$ROOT_DIR/newsletter/issues"
fi

# Weekly Digest on Fridays (UK timezone)
WEEKDAY="$($PYTHON_BIN - <<PY
from datetime import datetime
from zoneinfo import ZoneInfo
tz = ZoneInfo("${DEFAULT_TZ}")
print(datetime.now(tz).isoweekday())
PY
)"
if [ "$WEEKDAY" = "5" ]; then
  echo "📅 Friday detected: Generating Weekly Digest..."
  "$PYTHON_BIN" "$ROOT_DIR/newsletter/generate_weekly_digest.py" \
    --issues-dir "$ROOT_DIR/newsletter/issues"
fi

PREVIEW_LIST="$ROOT_DIR/newsletter/preview_subscribers.csv"

if [ "${NEWSLETTER_SEND_CURATION_REMINDER:-}" = "1" ]; then
  if [ ! -f "$PREVIEW_LIST" ]; then
    echo "Error: preview_subscribers.csv not found. Aborting curation reminder."
    PREVIEW_LIST=""
  fi
  CURATION_TZ="${NEWSLETTER_CURATION_TZ:-Europe/London}"
  CURATION_HOUR="${NEWSLETTER_CURATION_HOUR:-0}"
  CURATION_MINUTE="${NEWSLETTER_CURATION_MINUTE:-01}"
  CURATION_WINDOW_MINUTES="${NEWSLETTER_CURATION_WINDOW_MINUTES:-10}"
  SHOULD_SEND="$($PYTHON_BIN - <<PY
from datetime import datetime, time
from zoneinfo import ZoneInfo

tz = ZoneInfo("${CURATION_TZ}")
now = datetime.now(tz)
target = datetime.combine(now.date(), time(int("${CURATION_HOUR}"), int("${CURATION_MINUTE}")), tz)
delta_minutes = abs((now - target).total_seconds()) / 60
print("yes" if delta_minutes <= int("${CURATION_WINDOW_MINUTES}") else "no")
PY
)"

  START_CURATION_SERVER="${NEWSLETTER_START_CURATION_SERVER:-}"
  if [ -z "$START_CURATION_SERVER" ]; then
    if [ "${GITHUB_ACTIONS:-}" = "true" ]; then
      START_CURATION_SERVER="0"
    else
      START_CURATION_SERVER="1"
    fi
  fi

  if [ "$START_CURATION_SERVER" = "1" ]; then
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
      "$PYTHON_BIN" "$ROOT_DIR/newsletter/send_reminder.py" \
        --preview-list "$PREVIEW_LIST" \
        --subject "Protein Design Digest: Curation Ready [${TODAY_DATE}]" \
        --body "Your daily curation is ready. Open ${CURATION_URL} to curate and approve." \
        --issue "$ROOT_DIR/newsletter/issues/${TODAY_DATE}.json" || echo "Warning: curation reminder failed."
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

SEND_TZ="${NEWSLETTER_SEND_TZ:-Europe/London}"
SEND_HOUR="${NEWSLETTER_SEND_HOUR:-9}"
SEND_MINUTE="${NEWSLETTER_SEND_MINUTE:-00}"
SEND_WINDOW_MINUTES="${NEWSLETTER_SEND_WINDOW_MINUTES:-10}"
AUTO_SEND="${NEWSLETTER_AUTO_SEND:-0}"
WEEKLY_AUTO_SEND="${NEWSLETTER_AUTO_SEND_WEEKLY:-0}"
WEEKLY_SEND_DOW="${NEWSLETTER_WEEKLY_SEND_DOW:-5}"
SHOULD_SEND="$($PYTHON_BIN - <<PY
from datetime import datetime, time
from zoneinfo import ZoneInfo

tz = ZoneInfo("${SEND_TZ}")
now = datetime.now(tz)
target = datetime.combine(now.date(), time(int("${SEND_HOUR}"), int("${SEND_MINUTE}")), tz)
delta_minutes = abs((now - target).total_seconds()) / 60
print("yes" if delta_minutes <= int("${SEND_WINDOW_MINUTES}") else "no")
PY
)"

if [ "$AUTO_SEND" = "1" ] && [ "$SHOULD_SEND" = "yes" ]; then
  APPROVAL_MARKER="$ROOT_DIR/newsletter/issues/${TODAY_DATE}.approved"
  if [ "${NEWSLETTER_DELAY_SEND:-0}" = "1" ] && [ ! -f "$APPROVAL_MARKER" ]; then
    echo "Auto send skipped: approval not found for ${TODAY_DATE}."
  else
    NEWSLETTER_TIMEZONE="$DEFAULT_TZ" NEWSLETTER_SEND_FREQUENCY=daily NEWSLETTER_SEND_APPROVED=yes "$ROOT_DIR/newsletter/run_send_confirmed.sh" "today" || echo "Warning: auto send failed."
  fi
fi

if [ "${NEWSLETTER_SEND_APPROVAL_REMINDER:-}" = "1" ]; then
  APPROVAL_REMINDER_TZ="${NEWSLETTER_APPROVAL_REMINDER_TZ:-$SEND_TZ}"
  APPROVAL_REMINDER_HOUR="${NEWSLETTER_APPROVAL_REMINDER_HOUR:-9}"
  APPROVAL_REMINDER_MINUTE="${NEWSLETTER_APPROVAL_REMINDER_MINUTE:-30}"
  APPROVAL_REMINDER_WINDOW_MINUTES="${NEWSLETTER_APPROVAL_REMINDER_WINDOW_MINUTES:-10}"
  SHOULD_REMIND="$($PYTHON_BIN - <<PY
from datetime import datetime, time
from zoneinfo import ZoneInfo

tz = ZoneInfo("${APPROVAL_REMINDER_TZ}")
now = datetime.now(tz)
target = datetime.combine(now.date(), time(int("${APPROVAL_REMINDER_HOUR}"), int("${APPROVAL_REMINDER_MINUTE}")), tz)
delta_minutes = abs((now - target).total_seconds()) / 60
print("yes" if delta_minutes <= int("${APPROVAL_REMINDER_WINDOW_MINUTES}") else "no")
PY
)"
  APPROVAL_MARKER="$ROOT_DIR/newsletter/issues/${TODAY_DATE}.approved"
  SENT_MARKER="$ROOT_DIR/newsletter/issues/${TODAY_DATE}.sent"
  if [ "$SHOULD_REMIND" = "yes" ]; then
    if [ -f "$SENT_MARKER" ]; then
      echo "Skipping approval reminder: issue already sent."
    elif [ -f "$APPROVAL_MARKER" ]; then
      echo "Skipping approval reminder: approval already recorded."
    else
      if [ ! -f "$PREVIEW_LIST" ]; then
        echo "Error: preview_subscribers.csv not found. Aborting approval reminder."
      elif [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
        echo "Warning: Missing Gmail credentials. Skipping approval reminder email."
      else
        PORT="${NEWSLETTER_CURATION_PORT:-5050}"
        CURATION_URL="${NEWSLETTER_CURATION_URL:-http://127.0.0.1:${PORT}}"
        APPROVAL_SUBJECT="${NEWSLETTER_APPROVAL_REMINDER_SUBJECT:-Protein Design Digest: approval pending [${TODAY_DATE}]}"
        APPROVAL_BODY="${NEWSLETTER_APPROVAL_REMINDER_BODY:-Approval is still pending. Please review and approve at ${CURATION_URL} before send.}"
        "$PYTHON_BIN" "$ROOT_DIR/newsletter/send_reminder.py" \
          --preview-list "$PREVIEW_LIST" \
          --subject "$APPROVAL_SUBJECT" \
          --body "$APPROVAL_BODY" \
          --issue "$ROOT_DIR/newsletter/issues/${TODAY_DATE}.json" || echo "Warning: approval reminder failed."
      fi
    fi
  else
    echo "Skipping approval reminder: runs within ${APPROVAL_REMINDER_WINDOW_MINUTES} min of ${APPROVAL_REMINDER_HOUR}:${APPROVAL_REMINDER_MINUTE} $APPROVAL_REMINDER_TZ."
  fi
fi

if [ "${NEWSLETTER_SEND_WEEKLY_CURATION_REMINDER:-}" = "1" ]; then
  if [ "$WEEKDAY" != "5" ]; then
    echo "Skipping weekly curation reminder: not Friday."
  else
    WEEKLY_CURATION_TZ="${NEWSLETTER_WEEKLY_CURATION_TZ:-$DEFAULT_TZ}"
    WEEKLY_CURATION_HOUR="${NEWSLETTER_WEEKLY_CURATION_HOUR:-0}"
    WEEKLY_CURATION_MINUTE="${NEWSLETTER_WEEKLY_CURATION_MINUTE:-01}"
    WEEKLY_CURATION_WINDOW_MINUTES="${NEWSLETTER_WEEKLY_CURATION_WINDOW_MINUTES:-10}"
    SHOULD_WEEKLY_REMIND="$($PYTHON_BIN - <<PY
from datetime import datetime, time
from zoneinfo import ZoneInfo

tz = ZoneInfo("${WEEKLY_CURATION_TZ}")
now = datetime.now(tz)
target = datetime.combine(now.date(), time(int("${WEEKLY_CURATION_HOUR}"), int("${WEEKLY_CURATION_MINUTE}")), tz)
delta_minutes = abs((now - target).total_seconds()) / 60
print("yes" if delta_minutes <= int("${WEEKLY_CURATION_WINDOW_MINUTES}") else "no")
PY
)"
    if [ "$SHOULD_WEEKLY_REMIND" = "yes" ]; then
      START_CURATION_SERVER="${NEWSLETTER_START_CURATION_SERVER:-}"
      if [ -z "$START_CURATION_SERVER" ]; then
        if [ "${GITHUB_ACTIONS:-}" = "true" ]; then
          START_CURATION_SERVER="0"
        else
          START_CURATION_SERVER="1"
        fi
      fi

      if [ "$START_CURATION_SERVER" = "1" ]; then
        PORT="${NEWSLETTER_CURATION_PORT:-5050}"
        LOG_PATH="${ROOT_DIR}/newsletter/curation_server.log"
        nohup "$ROOT_DIR/newsletter/run_curation_server.sh" "today" "$PORT" > "$LOG_PATH" 2>&1 &
        sleep 2
      fi

      if [ ! -f "$PREVIEW_LIST" ]; then
        echo "Error: preview_subscribers.csv not found. Aborting weekly curation reminder."
      elif [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
        echo "Warning: Missing Gmail credentials. Skipping weekly curation reminder email."
      else
        PORT="${NEWSLETTER_CURATION_PORT:-5050}"
        CURATION_URL="${NEWSLETTER_CURATION_URL:-http://127.0.0.1:${PORT}}"
        WEEKLY_SUBJECT="${NEWSLETTER_WEEKLY_CURATION_SUBJECT:-Protein Design Digest: weekly curation ready [${TODAY_DATE}]}"
        WEEKLY_BODY="${NEWSLETTER_WEEKLY_CURATION_BODY:-Weekly curation is ready. Open ${CURATION_URL} to curate and approve the weekly digest.}"
        "$PYTHON_BIN" "$ROOT_DIR/newsletter/send_reminder.py" \
          --preview-list "$PREVIEW_LIST" \
          --subject "$WEEKLY_SUBJECT" \
          --body "$WEEKLY_BODY" \
          --issue "$ROOT_DIR/newsletter/issues/${TODAY_DATE}.json" || echo "Warning: weekly curation reminder failed."
      fi
    else
      echo "Skipping weekly curation reminder: runs within ${WEEKLY_CURATION_WINDOW_MINUTES} min of ${WEEKLY_CURATION_HOUR}:${WEEKLY_CURATION_MINUTE} $WEEKLY_CURATION_TZ."
    fi
  fi
fi

if [ "$WEEKLY_AUTO_SEND" = "1" ] && [ "$SHOULD_SEND" = "yes" ] && [ "$WEEKDAY" = "$WEEKLY_SEND_DOW" ]; then
  "$PYTHON_BIN" "$ROOT_DIR/newsletter/send_weekly_digest.py" \
    --issues-dir "$ROOT_DIR/newsletter/issues" \
    --subscribers "$ROOT_DIR/newsletter/subscribers.csv" \
    --config "$ROOT_DIR/newsletter/generate_config.json" || echo "Warning: weekly digest send failed."
  if [ "${NEWSLETTER_WEEKLY_SOCIAL:-1}" = "1" ]; then
    "$PYTHON_BIN" "$ROOT_DIR/newsletter/post_weekly_digest.py" \
      --date "$TODAY_DATE" || echo "Warning: weekly digest social post failed."
  fi
fi

echo "Daily run complete. Run run_send_confirmed.sh after approval to email everyone."
