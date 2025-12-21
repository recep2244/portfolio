#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

echo "Broadcasting today's issue to ALL subscribers..."
python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
  --issue-date today \
  --issues-dir "$ROOT_DIR/newsletter/issues" \
  --subscribers "$ROOT_DIR/newsletter/subscribers.csv"

echo "Newsletter sent to all subscribers."
