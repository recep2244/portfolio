#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

# Load environment variables from .env if it exists
if [ -f "$ROOT_DIR/newsletter/.env" ]; then
  set -a
  source "$ROOT_DIR/newsletter/.env"
  set +a
fi

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

PREVIEW_LIST="$ROOT_DIR/newsletter/preview_subscribers.csv"
if [ ! -f "$PREVIEW_LIST" ]; then
  echo "Error: preview_subscribers.csv not found. Aborting preview send."
  exit 1
fi

if [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
  echo "Warning: Missing Gmail credentials. Rendering preview only."
  python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
    --issue-date today \
    --issues-dir "$ROOT_DIR/newsletter/issues" \
    --subscribers "$PREVIEW_LIST" \
    --template-html "$ROOT_DIR/newsletter/template.html" \
    --template-text "$ROOT_DIR/newsletter/template.txt" \
    --render-only
else
  python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
    --issue-date today \
    --issues-dir "$ROOT_DIR/newsletter/issues" \
    --subscribers "$PREVIEW_LIST" \
    --template-html "$ROOT_DIR/newsletter/template.html" \
    --template-text "$ROOT_DIR/newsletter/template.txt" || echo "Warning: preview send failed."
fi

if [ "${NEWSLETTER_SEND_CURATION_REMINDER:-}" = "1" ]; then
  if [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
    echo "Warning: Missing Gmail credentials. Skipping curation reminder."
  else
    python3 "$ROOT_DIR/newsletter/send_reminder.py" \
      --preview-list "$PREVIEW_LIST" \
      --subject "Protein Design Digest: Curation Ready [$(date +%Y-%m-%d)]" \
      --body "Your daily curation is ready." \
      --issue "$ROOT_DIR/newsletter/issues/$(date +%Y-%m-%d).json" || echo "Warning: curation reminder failed."

    # Post to Social Media (if credentials exist)
    python3 "$ROOT_DIR/newsletter/social_post.py" \
      --issue "$ROOT_DIR/newsletter/issues/$(date +%Y-%m-%d).json" || echo "Warning: Social posting failed."
  fi
fi

echo "Preview sent (or rendered). Run run_send_confirmed.sh after approval to email everyone."
