#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ISSUE_DATE="${1:-today}"

# Load environment variables from .env if it exists
if [ -f "$ROOT_DIR/newsletter/.env" ]; then
  set -a
  source "$ROOT_DIR/newsletter/.env"
  set +a
fi

if [ "${NEWSLETTER_SEND_APPROVED:-}" != "yes" ] && [ "${NEWSLETTER_SEND_APPROVED:-}" != "true" ]; then
  echo "Error: approval missing. Set NEWSLETTER_SEND_APPROVED=yes to send."
  exit 1
fi

if [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
  echo "Error: Gmail credentials missing. Cannot send."
  exit 1
fi

python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
  --issue-date "$ISSUE_DATE" \
  --issues-dir "$ROOT_DIR/newsletter/issues" \
  --subscribers "$ROOT_DIR/newsletter/subscribers.csv" \
  --template-html "$ROOT_DIR/newsletter/template.html" \
  --template-text "$ROOT_DIR/newsletter/template.txt"

echo "📣 Publishing announcement to social media..."
python3 "$ROOT_DIR/newsletter/social_post.py" \
  --issue "$ROOT_DIR/newsletter/issues/$ISSUE_DATE.json" || echo "⚠️ Social publishing failed, skipping..."
