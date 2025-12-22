#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ISSUE_DATE="${1:-today}"
PORT="${2:-5050}"

# Load environment variables from .env if it exists
if [ -f "$ROOT_DIR/newsletter/.env" ]; then
  set -a
  source "$ROOT_DIR/newsletter/.env"
  set +a
fi

python3 "$ROOT_DIR/newsletter/curation_server.py" \
  --issue-date "$ISSUE_DATE" \
  --port "$PORT"
