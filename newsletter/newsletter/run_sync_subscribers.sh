#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

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

write_csv_from_env() {
  local path="$1"
  local var_name="$2"
  local value="${!var_name:-}"
  if [ ! -f "$path" ] && [ -n "$value" ]; then
    printf "%s" "$value" > "$path"
  fi
}

write_csv_from_env "$ROOT_DIR/newsletter/subscribers.csv" "NEWSLETTER_SUBSCRIBERS_CSV"

"$PYTHON_BIN" "$ROOT_DIR/newsletter/sync_subscribers_from_gmail.py" \
  --subscribers "$ROOT_DIR/newsletter/subscribers.csv"
