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

python3 "$ROOT_DIR/newsletter/sync_subscribers_from_gmail.py" \
  --subscribers "$ROOT_DIR/newsletter/subscribers.csv"
