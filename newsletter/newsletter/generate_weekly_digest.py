import json
import os
import argparse
from datetime import datetime, timedelta


def coerce_list(value):
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return [value]
    return []


def truncate_text(text, max_len=240):
    if not text:
        return ""
    text = str(text).strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."

# Configuration
ISSUES_DIR = "issues"
HUGO_CONTENT_DIR = "../../content/newsletter"
WEEKLY_FILE_PREFIX = "weekly-digest-"

def load_issue(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Skipping {filepath}: {e}")
        return None

def get_week_range(today=None):
    if today is None:
        today = datetime.now()
    # Always target the most recent Monday-Friday window.
    weekday = today.weekday()  # Monday=0, Sunday=6
    days_since_friday = (weekday - 4) % 7
    end_date = today.date() - timedelta(days=days_since_friday)
    start_date = end_date - timedelta(days=4)
    return start_date, end_date

def generate_digest_md(issues, start_date, end_date):
    # Sort issues by date
    issues.sort(key=lambda x: x.get('issue_date', ''))
    
    date_range_str = f"{start_date.strftime('%b %d')} - {end_date.strftime('%b %d, %Y')}"
    title = f"Weekly Digest: {date_range_str}"
    description = f"A curated summary of the top protein engineering and structure prediction signals from {date_range_str}."
    
    md = f"""---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d')}
description: "{description}"
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{{{< newsletter >}}}}

# 🧬 Weekly Recap
**{date_range_str}**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

"""

    # 1. Top List: The curated 'Signal' paper from each day
    for issue in issues:
        signal = issue.get("signal") or {}
        if isinstance(signal, list):
            signal = signal[0] if signal else {}
        day_date = datetime.strptime(issue.get("issue_date"), "%Y-%m-%d")
        day_name = day_date.strftime("%A, %b %d")
        title = (signal.get("title") or "Signal").strip()
        link = (signal.get("link") or "").strip()
        summary = (signal.get("summary") or signal.get("abstract") or "").strip()
        why = (signal.get("why_it_matters") or "").strip()

        md += f"## 🗓️ {day_name}\n\n"
        if link:
            md += f"### [{title}]({link})\n"
        else:
            md += f"### {title}\n"
        if summary:
            md += "#### 🧬 Abstract\n"
            md += f"{summary}\n\n"
        if why:
            md += f"> **Why it matters:** {why}\n\n"

    md += "---\n\n## 📚 All Papers & Quick Reads\n\n"

    # 2. All Quick Reads per day
    for issue in issues:
        q_reads = coerce_list(issue.get("quick_reads"))
        if not q_reads:
            continue
        day_date = datetime.strptime(issue.get("issue_date"), "%Y-%m-%d")
        day_name = day_date.strftime("%A, %b %d")
        md += f"### 🗓️ {day_name}\n\n"
        for paper in q_reads:
            title = (paper.get("title") or "Untitled").strip()
            link = (paper.get("link") or "").strip()
            abstract = truncate_text(paper.get("abstract") or "", 260)
            if link:
                line = f"- **[{title}]({link})**"
            else:
                line = f"- **{title}**"
            if abstract:
                line += f": {abstract}"
            md += f"{line}\n"
        md += "\n"

    md += "---\n\n## 🛠️ Tools & Datasets\n\n"

    # 3. Aggregated Tools/Datasets
    seen_tools = set()
    seen_datasets = set()
    for issue in issues:
        tools = coerce_list(issue.get("tool"))
        datasets = coerce_list(issue.get("dataset"))

        for tool in tools:
            if tool and tool.get("title") not in ["Add a tool", "Add a tool you like"]:
                key = (tool.get("title") or "").strip().lower()
                if key and key not in seen_tools:
                    summary = (tool.get("summary") or "").strip()
                    md += f"- 🛠 **Tool**: [{tool.get('title')}]({tool.get('link')}) - {summary}\n"
                    seen_tools.add(key)

        for dataset in datasets:
            if dataset and dataset.get("title") not in ["Add a dataset", "Add a dataset you like"]:
                key = (dataset.get("title") or "").strip().lower()
                if key and key not in seen_datasets:
                    summary = (dataset.get("summary") or "").strip()
                    md += f"- 💾 **Dataset**: [{dataset.get('title')}]({dataset.get('link')}) - {summary}\n"
                    seen_datasets.add(key)

    # 4. AI & Research News
    ai_news_items = []
    for issue in issues:
        ai_news_items.extend(coerce_list(issue.get("ai_news")))

    if ai_news_items:
        md += "\n---\n\n## 🤖 AI in Research Recap\n\n"
        seen_ai = set()
        for item in ai_news_items:
            title = (item.get("title") or "").strip()
            if title and title not in seen_ai:
                md += f"- **[{title}]({item.get('link')})**: {item.get('abstract')}\n"
                seen_ai.add(title)

    # 5. Industry Insights
    ind_news_items = []
    for issue in issues:
        ind_news_items.extend(coerce_list(issue.get("industry_news")))

    if ind_news_items:
        md += "\n---\n\n## 🏢 Industry & Real-World Applications\n\n"
        seen_ind = set()
        for item in ind_news_items:
            title = (item.get("title") or "").strip()
            if title and title not in seen_ind:
                md += f"- **[{title}]({item.get('link')})**: {item.get('abstract')}\n"
                seen_ind.add(title)

    jobs = []
    events = []
    for issue in issues:
        community = issue.get("community") or {}
        jobs.extend(coerce_list(community.get("job")))
        events.extend(coerce_list(community.get("event")))

    if jobs:
        md += "\n---\n\n## 💼 Jobs & Opportunities\n\n"
        seen_jobs = set()
        for item in jobs:
            title = (item.get("title") or "").strip()
            if not title or title in seen_jobs:
                continue
            org = (item.get("org") or "").strip()
            link = (item.get("link") or "").strip()
            label = f"{title} ({org})" if org else title
            if link:
                md += f"- **[{label}]({link})**\n"
            else:
                md += f"- **{label}**\n"
            seen_jobs.add(title)

    if events:
        md += "\n---\n\n## 📅 Events\n\n"
        seen_events = set()
        for item in events:
            title = (item.get("title") or "").strip()
            if not title or title in seen_events:
                continue
            link = (item.get("link") or "").strip()
            if link:
                md += f"- **[{title}]({link})**\n"
            else:
                md += f"- **{title}**\n"
            seen_events.add(title)

    md += "\n---\n\n_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._\n"
    
    return md

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--issues-dir", default=ISSUES_DIR)
    parser.add_argument("--date", default=None, help="YYYY-MM-DD to use as 'today' endpoint")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    issues_dir = os.path.join(base_dir, args.issues_dir)
    output_dir = os.path.join(base_dir, HUGO_CONTENT_DIR)

    if args.date:
        today = datetime.strptime(args.date, '%Y-%m-%d')
    else:
        today = datetime.now()

    start_date, end_date = get_week_range(today)
    print(f"Generating digest for period: {start_date} to {end_date}")

    collected_issues = []
    
    for filename in os.listdir(issues_dir):
        if not filename.endswith(".json"):
            continue
            
        # Parse date from filename: YYYY-MM-DD.json
        try:
            file_date_str = filename.replace(".json", "")
            file_date = datetime.strptime(file_date_str, '%Y-%m-%d').date()
            
            # Check if in range [start_date, end_date]
            if start_date <= file_date <= end_date:
                data = load_issue(os.path.join(issues_dir, filename))
                if data:
                    collected_issues.append(data)
        except ValueError as e:
            continue

    if collected_issues:
        md_content = generate_digest_md(collected_issues, start_date, end_date)
        
        # Filename: weekly-digest-2025-12-21.md
        filename = f"{WEEKLY_FILE_PREFIX}{end_date.strftime('%Y-%m-%d')}.md"
        out_path = os.path.join(output_dir, filename)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Successfully generated weekly digest: {out_path}")
    else:
        print("No issues found in the latest Monday-Friday window.")

if __name__ == "__main__":
    main()
