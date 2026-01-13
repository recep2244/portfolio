#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
LOG_PATH="$ROOT_DIR/newsletter/daily_cron.log"

MARKER="# protein-design-digest"

ENTRY_CURATION="CRON_TZ=Europe/London
1 0 * * * NEWSLETTER_SEND_CURATION_REMINDER=1 NEWSLETTER_START_CURATION_SERVER=1 NEWSLETTER_SYNC_SUBSCRIBERS=1 \"$ROOT_DIR/newsletter/run_daily.sh\" >> \"$LOG_PATH\" 2>&1 $MARKER"
ENTRY_SEND="CRON_TZ=Europe/London
0 9 * * * NEWSLETTER_AUTO_SEND=1 NEWSLETTER_DELAY_SEND=1 NEWSLETTER_SYNC_SUBSCRIBERS=1 \"$ROOT_DIR/newsletter/run_daily.sh\" >> \"$LOG_PATH\" 2>&1 $MARKER"
ENTRY_APPROVAL_REMINDER="CRON_TZ=Europe/London
30 9 * * * NEWSLETTER_SEND_APPROVAL_REMINDER=1 NEWSLETTER_SYNC_SUBSCRIBERS=1 \"$ROOT_DIR/newsletter/run_daily.sh\" >> \"$LOG_PATH\" 2>&1 $MARKER"
ENTRY_WEEKLY_CURATION="CRON_TZ=Europe/London
2 0 * * 5 NEWSLETTER_SEND_WEEKLY_CURATION_REMINDER=1 NEWSLETTER_START_CURATION_SERVER=1 NEWSLETTER_SYNC_SUBSCRIBERS=1 \"$ROOT_DIR/newsletter/run_daily.sh\" >> \"$LOG_PATH\" 2>&1 $MARKER"
ENTRY_DAILY_SYNC="CRON_TZ=Europe/London
5 0 * * * \"$ROOT_DIR/newsletter/run_sync_subscribers.sh\" >> \"$LOG_PATH\" 2>&1 $MARKER"

CURRENT_CRON="$(crontab -l 2>/dev/null || true)"
FILTERED_CRON="$(printf "%s\n" "$CURRENT_CRON" | grep -v "$MARKER" || true)"

printf "%s\n%s\n%s\n%s\n%s\n%s\n" "$FILTERED_CRON" "$ENTRY_CURATION" "$ENTRY_SEND" "$ENTRY_APPROVAL_REMINDER" "$ENTRY_WEEKLY_CURATION" "$ENTRY_DAILY_SYNC" | crontab -

echo "Installed cron entries:"
crontab -l | grep "$MARKER"
