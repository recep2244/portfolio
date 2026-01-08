#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
LOG_PATH="$ROOT_DIR/newsletter/daily_cron.log"

MARKER="# protein-design-digest"

ENTRY_CURATION="CRON_TZ=Europe/London
1 0 * * * NEWSLETTER_SEND_CURATION_REMINDER=1 NEWSLETTER_START_CURATION_SERVER=1 \"$ROOT_DIR/newsletter/run_daily.sh\" >> \"$LOG_PATH\" 2>&1 $MARKER"
ENTRY_SEND="CRON_TZ=Europe/London
0 9 * * * NEWSLETTER_AUTO_SEND=1 NEWSLETTER_DELAY_SEND=1 \"$ROOT_DIR/newsletter/run_daily.sh\" >> \"$LOG_PATH\" 2>&1 $MARKER"

CURRENT_CRON="$(crontab -l 2>/dev/null || true)"
FILTERED_CRON="$(printf "%s\n" "$CURRENT_CRON" | grep -v "$MARKER" || true)"

printf "%s\n%s\n%s\n" "$FILTERED_CRON" "$ENTRY_CURATION" "$ENTRY_SEND" | crontab -

echo "Installed cron entries:"
crontab -l | grep "$MARKER"
