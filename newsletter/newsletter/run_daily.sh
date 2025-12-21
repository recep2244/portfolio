#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

python3 "$ROOT_DIR/newsletter/generate_issue.py" \
  --issue-date today \
  --config "$ROOT_DIR/newsletter/generate_config.json" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Convert to Hugo Content
python3 "$ROOT_DIR/newsletter/newsletter_to_md.py" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Weekly Digest on Sundays
if [ "$(date +%u)" = "7" ]; then
  echo "📅 Sunday detected: Generating Weekly Digest..."
  python3 "$ROOT_DIR/newsletter/generate_weekly_digest.py" \
    --issues-dir "$ROOT_DIR/newsletter/issues"
fi

python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
  --issue-date today \
  --issues-dir "$ROOT_DIR/newsletter/issues" \
  --subscribers "$ROOT_DIR/newsletter/subscribers.csv"
