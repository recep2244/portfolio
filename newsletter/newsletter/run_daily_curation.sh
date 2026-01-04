#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ISSUE_DATE="${1:-today}"
PORT="${2:-5050}"
LOG_PATH="${ROOT_DIR}/newsletter/curation_server.log"

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

STATUS=$(python3 - <<PY
import socket
host, port = "127.0.0.1", int("${PORT}")
sock = socket.socket()
sock.settimeout(1)
try:
    sock.connect((host, port))
    print("running")
except OSError:
    print("down")
finally:
    sock.close()
PY
)

if [ "$STATUS" = "running" ]; then
  if command -v lsof >/dev/null 2>&1; then
    lsof -ti tcp:"$PORT" | xargs -r kill || true
  elif command -v fuser >/dev/null 2>&1; then
    fuser -k "$PORT"/tcp || true
  else
    pkill -f "curation_server.py" || true
  fi
  sleep 1
fi

nohup "$ROOT_DIR/newsletter/run_curation_server.sh" "$ISSUE_DATE" "$PORT" > "$LOG_PATH" 2>&1 &
sleep 2

# Weekly Digest on Fridays
if [ "$(date +%u)" = "5" ]; then
  echo "📅 Friday detected: Generating Weekly Digest..."
  python3 "$ROOT_DIR/newsletter/generate_weekly_digest.py" \
    --issues-dir "$ROOT_DIR/newsletter/issues"
fi

python3 "$ROOT_DIR/newsletter/send_reminder.py" \
  --preview-list "$ROOT_DIR/newsletter/preview_subscribers.csv" \
  --subject "Protein Design Digest: curation ready" \
  --body "Your daily curation is ready. Open http://127.0.0.1:${PORT} to curate and approve."
