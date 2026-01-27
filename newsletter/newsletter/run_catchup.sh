#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
LOCK_DIR="$ROOT_DIR/newsletter/run_catchup.lockdir"
LOCK_PID_FILE="$LOCK_DIR/pid"

acquire_lock() {
  if mkdir "$LOCK_DIR" 2>/dev/null; then
    echo "$$" > "$LOCK_PID_FILE"
    return 0
  fi
  local old_pid=""
  old_pid="$(cat "$LOCK_PID_FILE" 2>/dev/null || true)"
  if [ -n "$old_pid" ] && kill -0 "$old_pid" 2>/dev/null; then
    echo "Catchup already running (pid $old_pid); exiting."
    exit 0
  fi
  rm -f "$LOCK_PID_FILE" 2>/dev/null || true
  rmdir "$LOCK_DIR" 2>/dev/null || true
  if mkdir "$LOCK_DIR" 2>/dev/null; then
    echo "$$" > "$LOCK_PID_FILE"
    return 0
  fi
  echo "Catchup already running; exiting."
  exit 0
}

cleanup() {
  rm -f "$LOCK_PID_FILE" 2>/dev/null || true
  rmdir "$LOCK_DIR" 2>/dev/null || true
}

trap cleanup EXIT

# Load .env if present
if [ -f "$ROOT_DIR/newsletter/.env" ]; then
  set -a
  set +e
  # shellcheck disable=SC1090
  source "$ROOT_DIR/newsletter/.env"
  set -e
  set +a
fi

PYTHON_BIN="${NEWSLETTER_PYTHON:-python3}"

acquire_lock

ISSUE_DATE="$($PYTHON_BIN - <<'PY'
import json
from pathlib import Path
issues = Path('newsletter/newsletter/issues')
if not issues.exists():
    print('')
    raise SystemExit
sent = {p.stem for p in issues.glob('*.sent')}
approved = sorted(p.stem for p in issues.glob('*.approved'))
# pick latest approved without sent
pending = [d for d in approved if d not in sent]
print(pending[-1] if pending else '')
PY
)"

if [ -z "$ISSUE_DATE" ]; then
  echo "Catchup: no approved unsent issue found."
  exit 0
fi

APPROVAL_MARKER="$ROOT_DIR/newsletter/issues/${ISSUE_DATE}.approved"
if [ ! -f "$APPROVAL_MARKER" ]; then
  echo "Catchup: approval marker missing for $ISSUE_DATE."
  exit 0
fi

SENT_MARKER="$ROOT_DIR/newsletter/issues/${ISSUE_DATE}.sent"
if [ -f "$SENT_MARKER" ]; then
  echo "Catchup: issue $ISSUE_DATE already sent."
  exit 0
fi

NEWSLETTER_SEND_APPROVED=yes "$ROOT_DIR/newsletter/run_send_confirmed.sh" "$ISSUE_DATE"
