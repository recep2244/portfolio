#!/bin/bash
# Weekly Analytics Report - Run every Sunday at 5 PM
# Add to crontab with: crontab -e
# 0 17 * * 0 /home/recep/Desktop/Machine_Learning/projects/hugo/newsletter/newsletter/analytics/weekly_report_cron.sh

cd /home/recep/Desktop/Machine_Learning/projects/hugo/newsletter/newsletter

# Load environment variables
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Check if tracker server is already running
if ! pgrep -f "analytics.tracker" > /dev/null; then
    echo "$(date): Starting analytics tracker server..." >> analytics/weekly_report.log
    # Start tracker server in background (will keep running after script ends)
    nohup python -m analytics.tracker --port 8080 >> analytics/tracker.log 2>&1 &
    # Wait a moment for server to start
    sleep 3
fi

# Send the weekly report
python -m analytics.send_report \
    --to "recepadiyaman2244@gmail.com" \
    --days 7 \
    --tracker-url "http://localhost:8080" \
    --db "analytics.db"

echo "$(date): Weekly analytics report sent" >> analytics/weekly_report.log
echo "$(date): Tracker server running at http://localhost:8080/dashboard" >> analytics/weekly_report.log
