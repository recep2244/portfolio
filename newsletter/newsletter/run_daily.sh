#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

# Load environment variables from .env if it exists
if [ -f "$ROOT_DIR/newsletter/.env" ]; then
  set -a
  source "$ROOT_DIR/newsletter/.env"
  set +a
fi

if [ "${NEWSLETTER_SYNC_SUBSCRIBERS:-1}" = "1" ]; then
  python3 "$ROOT_DIR/newsletter/sync_subscribers_from_gmail.py" \
    --subscribers "$ROOT_DIR/newsletter/subscribers.csv" || echo "Warning: subscriber sync failed."
fi

python3 "$ROOT_DIR/newsletter/generate_issue.py" \
  --issue-date today \
  --config "$ROOT_DIR/newsletter/generate_config.json" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Convert to Hugo Content
python3 "$ROOT_DIR/newsletter/newsletter_to_md.py" \
  --issues-dir "$ROOT_DIR/newsletter/issues"

# Weekly Digest on Fridays
if [ "$(date +%u)" = "5" ]; then
  echo "📅 Friday detected: Generating Weekly Digest..."
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
    --frequency daily \
    --render-only
else
  python3 "$ROOT_DIR/newsletter/send_newsletter.py" \
    --issue-date today \
    --issues-dir "$ROOT_DIR/newsletter/issues" \
    --subscribers "$PREVIEW_LIST" \
    --template-html "$ROOT_DIR/newsletter/template.html" \
    --template-text "$ROOT_DIR/newsletter/template.txt" \
    --frequency daily || echo "Warning: preview send failed."
fi

if [ "${NEWSLETTER_SEND_CURATION_REMINDER:-}" = "1" ]; then
  CURATION_TZ="${NEWSLETTER_CURATION_TZ:-Europe/London}"
  CURATION_HOUR="${NEWSLETTER_CURATION_HOUR:-10}"
  CURATION_MINUTE="${NEWSLETTER_CURATION_MINUTE:-00}"
  CURRENT_HOUR="$(TZ="$CURATION_TZ" date +%H)"
  CURRENT_MINUTE="$(TZ="$CURATION_TZ" date +%M)"

  if [ "$CURRENT_HOUR" = "$CURATION_HOUR" ] && [ "$CURRENT_MINUTE" = "$CURATION_MINUTE" ]; then
    if [ -z "${NEWSLETTER_GMAIL_USER:-}" ] || [ -z "${NEWSLETTER_GMAIL_APP_PASSWORD:-}" ]; then
      echo "Warning: Missing Gmail credentials. Skipping curation reminder email."
    else
      python3 "$ROOT_DIR/newsletter/send_reminder.py" \
        --preview-list "$PREVIEW_LIST" \
        --subject "Protein Design Digest: Curation Ready [$(date +%Y-%m-%d)]" \
        --body "Your daily curation is ready." \
        --issue "$ROOT_DIR/newsletter/issues/$(date +%Y-%m-%d).json" || echo "Warning: curation reminder failed."
    fi

    echo "Curation reminder sent. Social posting will run after approval."
  else
    echo "Skipping curation reminder: runs only at ${CURATION_HOUR}:${CURATION_MINUTE} $CURATION_TZ."
  fi
fi

echo "Preview sent (or rendered). Run run_send_confirmed.sh after approval to email everyone."
