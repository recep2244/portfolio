#!/usr/bin/env bash
# Weekly newsletter (decided 25 Nov 2026: weekly only, approved on Friday, sent on Saturday).
#
# The week runs Monday to Friday. run_daily.sh generates a daily issue each weekday (no sends) and,
# on Friday, the weekly digest plus a curation email pointing at http://127.0.0.1:5050/weekly,
# where the digest is approved or withdrawn. This script then:
#   remind   Friday 12:00: emails the preview list if the week is not approved yet.
#   send     Saturday 09:00: if approved, publishes the digest page, emails every active
#            subscriber, records <friday>.weekly.sent, then posts to the social channels.
#            A week that is not approved is skipped; a week already sent is never sent again.
# Usage: run_weekly_send.sh remind | send [--dry-run]
# NEWSLETTER_WEEKLY_DATE=YYYY-MM-DD (the Friday) picks another week, for testing.
set -uo pipefail
ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
REPO_ROOT=$(cd "$ROOT_DIR/.." && pwd)
NL="$ROOT_DIR/newsletter"
MODE="${1:-}"
DRY_RUN="${2:-}"

if [ -f "$NL/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  . "$NL/.env"
  set +a
fi
PY="${NEWSLETTER_PYTHON:-python3}"
TZ_NAME="${NEWSLETTER_TIMEZONE:-Europe/London}"
PORT="${NEWSLETTER_CURATION_PORT:-5050}"
APPROVAL_URL="${NEWSLETTER_CURATION_URL:-http://127.0.0.1:${PORT}}/weekly"

FRIDAY="${NEWSLETTER_WEEKLY_DATE:-$("$PY" - "$TZ_NAME" <<'PY'
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
now = datetime.now(ZoneInfo(sys.argv[1]))
print((now.date() - timedelta(days=(now.weekday() - 4) % 7)).isoformat())
PY
)}"
APPROVED="$NL/issues/$FRIDAY.weekly.approved"
SENT="$NL/issues/$FRIDAY.weekly.sent"
DIGEST_PAGE="content/newsletter/weekly-digest-$FRIDAY.md"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') weekly $MODE (week ending $FRIDAY): $*"; }

ensure_curation_server() {
  if ! curl -s -o /dev/null --max-time 3 "http://127.0.0.1:${PORT}/weekly"; then
    nohup "$NL/run_curation_server.sh" "today" "$PORT" > "$NL/curation_server.log" 2>&1 &
    sleep 3
    log "started the curation server on port $PORT"
  fi
}

remind() {
  if [ -f "$SENT" ]; then log "already sent; no reminder"; return 0; fi
  if [ -f "$APPROVED" ]; then log "already approved; no reminder"; return 0; fi
  ensure_curation_server
  "$PY" "$NL/send_reminder.py" \
    --preview-list "$NL/preview_subscribers.csv" \
    --subject "Protein Design Digest: weekly issue waiting for approval [$FRIDAY]" \
    --body "This week's digest is not approved yet. Review it and approve it at $APPROVAL_URL before Saturday 09:00. Without approval it is not sent." \
    && log "reminder sent" || { log "REMINDER FAILED"; return 1; }
}

publish_page() {
  "$PY" "$NL/generate_weekly_digest.py" --issues-dir "$NL/issues" --date "$FRIDAY" || return 1
  git -C "$REPO_ROOT" add -- "$DIGEST_PAGE" || return 1
  if git -C "$REPO_ROOT" diff --cached --quiet -- "$DIGEST_PAGE"; then
    log "digest page already published"
    return 0
  fi
  git -C "$REPO_ROOT" commit -q -m "Weekly digest: week ending $FRIDAY" -- "$DIGEST_PAGE" || return 1
  for attempt in 1 2 3; do
    if git -C "$REPO_ROOT" pull -q --rebase --autostash origin main && git -C "$REPO_ROOT" push -q origin HEAD:main; then
      log "digest page published"
      return 0
    fi
    sleep 10
  done
  return 1
}

send() {
  if [ -f "$SENT" ]; then log "already sent; nothing to do"; return 0; fi
  if [ ! -f "$APPROVED" ]; then log "not approved, so this week is skipped"; return 0; fi
  local send_args=(--issues-dir "$NL/issues" --subscribers "$NL/subscribers.csv"
                   --config "$NL/generate_config.json" --timezone "$TZ_NAME" --frequency all --date "$FRIDAY")
  if [ "$DRY_RUN" = "--dry-run" ]; then
    NEWSLETTER_WEEKLY_APPROVAL_MARKER="$APPROVED" "$PY" "$NL/send_weekly_digest.py" "${send_args[@]}" --dry-run
    return $?
  fi
  publish_page || log "WARNING: the digest page was not published; sending the email anyway"
  local failure
  if ! failure=$(NEWSLETTER_WEEKLY_APPROVAL_MARKER="$APPROVED" "$PY" "$NL/send_weekly_digest.py" "${send_args[@]}" 2>&1); then
    echo "$failure"
    log "SEND FAILED; nothing marked as sent, so a rerun will try again"
    "$PY" "$NL/send_reminder.py" \
      --preview-list "$NL/preview_subscribers.csv" \
      --subject "Protein Design Digest: weekly issue NOT sent [$FRIDAY]" \
      --body "The weekly digest was not sent: $(echo "$failure" | tail -1). Check $APPROVAL_URL, then run: bash $NL/run_weekly_send.sh send" \
      || log "could not email the failure either"
    return 1
  fi
  echo "$failure"
  "$PY" - "$SENT" "$FRIDAY" "$TZ_NAME" <<'PY'
import json, sys
from datetime import datetime
from zoneinfo import ZoneInfo
path, week, tz = sys.argv[1:4]
open(path, "w").write(json.dumps({"issue_date": week, "sent_at": datetime.now(ZoneInfo(tz)).isoformat()}, indent=2) + "\n")
PY
  log "email sent"
  if [ "${NEWSLETTER_WEEKLY_SOCIAL:-1}" = "1" ]; then
    sleep 120
    "$PY" "$NL/post_weekly_digest.py" --date "$FRIDAY" && log "social posts done" || log "WARNING: social post failed"
  fi
}

case "$MODE" in
  remind) remind ;;
  send) send ;;
  *) echo "usage: $0 remind | send [--dry-run]" >&2; exit 2 ;;
esac
