#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ISSUE_DATE="${1:-today}"
PORT="${2:-5050}"
PID_FILE="$ROOT_DIR/newsletter/curation_server.pid"

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

PYTHON_BIN="${NEWSLETTER_PYTHON:-python3}"

# Kill any existing curation server
kill_existing_server() {
  # Kill by PID file if exists
  if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE" 2>/dev/null || echo "")
    if [ -n "$OLD_PID" ] && kill -0 "$OLD_PID" 2>/dev/null; then
      echo "Killing existing curation server (PID: $OLD_PID)..."
      kill "$OLD_PID" 2>/dev/null || true
      sleep 1
    fi
    rm -f "$PID_FILE"
  fi

  # Also kill any process using the port
  PIDS=$(lsof -t -i:"$PORT" 2>/dev/null || true)
  if [ -n "$PIDS" ]; then
    echo "Killing processes on port $PORT: $PIDS"
    echo "$PIDS" | xargs -r kill 2>/dev/null || true
    sleep 1
  fi
}

kill_existing_server

# Start server and save PID
"$PYTHON_BIN" "$ROOT_DIR/newsletter/curation_server.py" \
  --issue-date "$ISSUE_DATE" \
  --port "$PORT" &

SERVER_PID=$!
echo "$SERVER_PID" > "$PID_FILE"
echo "Curation server started (PID: $SERVER_PID, Port: $PORT)"

# Wait for server process
wait "$SERVER_PID"
