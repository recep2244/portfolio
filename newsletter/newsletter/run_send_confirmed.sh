#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
REPO_ROOT=$(cd "$ROOT_DIR/.." && pwd)
ISSUE_DATE="${1:-today}"
PYTHON_BIN="${NEWSLETTER_PYTHON:-python3}"

resolve_issue_date() {
  if [ "$ISSUE_DATE" = "today" ]; then
  "$PYTHON_BIN" - <<PY
from datetime import datetime
from zoneinfo import ZoneInfo
import os
tz = ZoneInfo(os.environ.get("NEWSLETTER_TIMEZONE", "Europe/London"))
print(datetime.now(tz).date().isoformat())
PY
  else
    printf "%s" "$ISSUE_DATE"
  fi
}

ISSUE_DATE_RESOLVED="$(resolve_issue_date)"
SENT_MARKER="$ROOT_DIR/newsletter/issues/${ISSUE_DATE_RESOLVED}.sent"
SEND_FREQUENCY="${NEWSLETTER_SEND_FREQUENCY:-daily}"
APPROVAL_MARKER="${NEWSLETTER_APPROVAL_MARKER:-$ROOT_DIR/newsletter/issues/${ISSUE_DATE_RESOLVED}.approved}"

load_env() {
  local env_file="$ROOT_DIR/newsletter/.env"
  if [ -f "$env_file" ]; then
    set -a
    set +e
    # shellcheck disable=SC1090
    source "$env_file"
    local env_status=$?
    set -e
    set +a
    if [ "$env_status" -ne 0 ]; then
      echo "Warning: Failed to load $env_file. Quote values with spaces." >&2
    fi
  fi
}

load_env

write_csv_from_env() {
  local path="$1"
  local var_name="$2"
  local value="${!var_name:-}"
  if [ ! -f "$path" ] && [ -n "$value" ]; then
    printf "%s" "$value" > "$path"
  fi
}

git_push_with_rebase() {
  local repo_dir="$1"
  if git -C "$repo_dir" push; then
    return 0
  fi
  echo "Warning: git push failed; attempting pull --rebase and retry."
  if git -C "$repo_dir" pull --rebase --autostash; then
    git -C "$repo_dir" push || {
      echo "Warning: git push failed after rebase."
      return 1
    }
    return 0
  fi
  echo "Warning: git pull --rebase failed; skipping push."
  git -C "$repo_dir" rebase --abort 2>/dev/null || true
  return 1
}

write_csv_from_env "$ROOT_DIR/newsletter/subscribers.csv" "NEWSLETTER_SUBSCRIBERS_CSV"

if [ "${NEWSLETTER_SYNC_SUBSCRIBERS:-1}" = "1" ]; then
  "$PYTHON_BIN" "$ROOT_DIR/newsletter/sync_subscribers_from_gmail.py" \
    --subscribers "$ROOT_DIR/newsletter/subscribers.csv" || echo "Warning: subscriber sync failed."
fi

ALLOW_RESEND="$(printf "%s" "${NEWSLETTER_ALLOW_RESEND:-}" | tr '[:upper:]' '[:lower:]')"
if [ -f "$SENT_MARKER" ] && [ "$ALLOW_RESEND" != "1" ] && [ "$ALLOW_RESEND" != "true" ] && [ "$ALLOW_RESEND" != "yes" ] && [ "$ALLOW_RESEND" != "y" ] && [ "$ALLOW_RESEND" != "on" ]; then
  echo "Error: issue already sent ($ISSUE_DATE_RESOLVED). Set NEWSLETTER_ALLOW_RESEND=1 to resend."
  exit 1
fi

if [ "${NEWSLETTER_SEND_APPROVED:-}" != "yes" ] && [ "${NEWSLETTER_SEND_APPROVED:-}" != "true" ]; then
  echo "Error: approval missing. Set NEWSLETTER_SEND_APPROVED=yes to send."
  exit 1
fi

if [ ! -f "$APPROVAL_MARKER" ]; then
  echo "Error: approval marker missing ($APPROVAL_MARKER)."
  exit 1
fi

if [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
  echo "Error: Gmail credentials missing. Cannot send."
  exit 1
fi

"$PYTHON_BIN" "$ROOT_DIR/newsletter/newsletter_to_md.py" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

"$PYTHON_BIN" "$ROOT_DIR/newsletter/send_newsletter.py" \
  --issue-date "$ISSUE_DATE" \
  --issues-dir "$ROOT_DIR/newsletter/issues" \
  --subscribers "$ROOT_DIR/newsletter/subscribers.csv" \
  --template-html "$ROOT_DIR/newsletter/template.html" \
  --template-text "$ROOT_DIR/newsletter/template.txt" \
  --frequency "$SEND_FREQUENCY"

SENT_MARKER_PATH="$SENT_MARKER" ISSUE_DATE_RESOLVED="$ISSUE_DATE_RESOLVED" "$PYTHON_BIN" - <<'PY'
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

path = os.environ["SENT_MARKER_PATH"]
issue_date = os.environ["ISSUE_DATE_RESOLVED"]
tz = ZoneInfo(os.environ.get("NEWSLETTER_TIMEZONE", "Europe/London"))
payload = {
    "issue_date": issue_date,
    "sent_at": datetime.now(tz).isoformat(),
}
with open(path, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, sort_keys=True)
    f.write("\n")
PY

if [ "${NEWSLETTER_SYNC_ARCHIVE:-0}" = "1" ]; then
  ARCHIVE_PATH="$REPO_ROOT/content/newsletter"
  if [ -d "$ARCHIVE_PATH" ]; then
    git -C "$REPO_ROOT" add "$ARCHIVE_PATH"
    if ! git -C "$REPO_ROOT" diff --cached --quiet; then
      COMMIT_MSG="${NEWSLETTER_SYNC_COMMIT_MESSAGE:-Sync newsletter archive (${ISSUE_DATE_RESOLVED})}"
      git -C "$REPO_ROOT" commit -m "$COMMIT_MSG"
      if [ "${NEWSLETTER_SYNC_PUSH:-0}" = "1" ]; then
        git_push_with_rebase "$REPO_ROOT" || true
      fi
    fi
  else
    echo "Warning: archive path missing ($ARCHIVE_PATH). Skipping git sync."
  fi
fi

echo "📣 Publishing announcement to social media..."
"$PYTHON_BIN" "$ROOT_DIR/newsletter/social_post.py" \
  --issue "$ROOT_DIR/newsletter/issues/$ISSUE_DATE_RESOLVED.json" || echo "⚠️ Social publishing failed, skipping..."
