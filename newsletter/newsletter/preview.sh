#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

echo "Generating today's issue..."
python3 "$ROOT_DIR/newsletter/generate_issue.py" \
  --issue-date today \
  --config "$ROOT_DIR/newsletter/generate_config.json" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

echo "Use 'cat newsletter/issues/$(date +%Y-%m-%d).json' to check the content content manually."
echo "Sending preview to me@example.com (configure in newsletter/preview_subscribers.csv)..."

python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
  --issue-date today \
  --issues-dir "$ROOT_DIR/newsletter/issues" \
  --subscribers "$ROOT_DIR/newsletter/preview_subscribers.csv" \
  --subject-prefix "[PREVIEW] "

echo "Preview sent! Check your inbox."
