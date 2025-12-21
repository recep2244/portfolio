Daily Bioinformatics Newsletter (Gmail)

What this gives you
- Gmail friendly HTML and text templates
- A sender script that batches BCC recipients
- A daily issue JSON format

Files
- newsletter/template.html
- newsletter/template.txt
- newsletter/issue_template.json
- newsletter/generate_config.json
- newsletter/generate_issue.py
- newsletter/run_daily.sh
- newsletter/subscribers.csv
- newsletter/send_newsletter.py

Setup (Gmail)
1) Enable 2-step verification on your Gmail account.
2) Create an App Password for Mail.
3) Export env vars (do not commit secrets):
   export NEWSLETTER_GMAIL_USER="you@gmail.com"
   export NEWSLETTER_GMAIL_APP_PASSWORD="your_app_password"
   export NEWSLETTER_FROM_EMAIL="you@gmail.com"
   export NEWSLETTER_FROM_NAME="Genome Daily"

Create a daily issue file
- Option A: auto-generate from daily paper searches (arXiv, Europe PMC, bioRxiv, medRxiv, PubMed, RSS):
  python newsletter/generate_issue.py --issue-date today --dry-run
- Option B: copy the template and edit:
  cp newsletter/issue_template.json newsletter/issues/2025-01-01.json

Dry run
python newsletter/send_newsletter.py --issue newsletter/issues/2025-01-01.json --dry-run

Send
python newsletter/send_newsletter.py --issue newsletter/issues/2025-01-01.json

Auto-search + send (single command)
newsletter/run_daily.sh

Schedule for 04:00 UK time (cron)
- Use Europe/London timezone so BST/GMT is handled.
- Example crontab entry:
  TZ=Europe/London
  0 4 * * * /path/to/newsletter/run_daily.sh

Notes
- Free Gmail has a daily recipient limit around 500. If you hit the cap, upgrade to Workspace or use a dedicated email service.
- Maintain an unsubscribe link in each issue for compliance.
- You can mark a subscriber as unsubscribed in newsletter/subscribers.csv (status column).
- Edit newsletter/generate_config.json to tune keywords, pools, and links.
- For PubMed, set your email/tool in newsletter/generate_config.json for NCBI compliance.
- For Nature and other journals, add RSS feed URLs under sources.rss.feeds.
- For Google Alerts, open the alert, click the RSS icon, and paste that feed URL into sources.rss.feeds.
- For AI news, add RSS URLs under ai_news.feeds and tune ai_news.keywords if needed.
