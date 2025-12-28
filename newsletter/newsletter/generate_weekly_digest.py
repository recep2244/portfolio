import json
import os
import argparse
from datetime import datetime, timedelta

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
    # If we run this on Sunday (6), we want the preceding Monday-Sunday or just last 7 days.
    # Let's just do "Last 7 Days" rolling window for simplicity, or strictly previous week?
    # User said "combine the dailies for last 7 days".
    start_date = today - timedelta(days=7)
    return start_date.date(), today.date()

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

Missed a day? Here are the top research signals and tools from the past week, summarized for your Sunday reading.

---

## 🏆 Top Signals of the Week

"""
    
    # 1. Top List: The 'Signal' paper from each day
    for issue in issues:
        signal = issue.get('signal', {})
        day_date = datetime.strptime(issue.get('issue_date'), '%Y-%m-%d')
        day_name = day_date.strftime('%A, %b %d')
        
        md += f"## 🗓️ {day_name}\n\n"
        md += f"### [{signal.get('title')}]({signal.get('link')})\n"
        md += f"#### 🧬 Abstract\n"
        md += f"{signal.get('summary')}\n\n"
        md += f"> **Why it matters:** {signal.get('why_it_matters')}\n\n"

    md += "---\n\n## ⚡ Selected Quick Reads\n\n"
    
    # 2. Aggregated Quick Reads (Limit to top 1-2 per day to avoid huge post)
    for issue in issues:
        q_reads = issue.get('quick_reads', [])
        if q_reads:
            # Take the first one
            paper = q_reads[0]
            md += f"- **[{paper.get('title')}]({paper.get('link')})**: {paper.get('abstract')}\n"

    md += "\n---\n\n## 🛠️ Tools & Datasets\n\n"
    
    # 3. Aggregated Tools/Datasets
    for issue in issues:
        tools = issue.get('tool')
        datasets = issue.get('dataset')
        
        # Handle if tool is a list (new format) or dict (old format)
        if tools:
            if isinstance(tools, dict):
                tools = [tools]
            for tool in tools:
                if tool and tool.get('title') not in ["Add a tool", "Add a tool you like"]:
                     md += f"- 🛠 **Tool**: [{tool.get('title')}]({tool.get('link')}) - {tool.get('summary')}\n"

        # Handle if dataset is a list (new format) or dict (old format)
        if datasets:
            if isinstance(datasets, dict):
                datasets = [datasets]
            for dataset in datasets:
                if dataset and dataset.get('title') not in ["Add a dataset", "Add a dataset you like"]:
                     md += f"- 💾 **Dataset**: [{dataset.get('title')}]({dataset.get('link')}) - {dataset.get('summary')}\n"

    # 4. AI & Research News
    ai_news_items = []
    for issue in issues:
        ai_news_items.extend(issue.get('ai_news', []))
    
    if ai_news_items:
        md += "\n---\n\n## 🤖 AI in Research Recap\n\n"
        seen_ai = set()
        count = 0
        for item in ai_news_items:
            if item.get('title') not in seen_ai and count < 8:
                md += f"- **[{item.get('title')}]({item.get('link')})**: {item.get('abstract')}\n"
                seen_ai.add(item.get('title'))
                count += 1

    # 5. Industry Insights
    ind_news_items = []
    for issue in issues:
        ind_news_items.extend(issue.get('industry_news', []))
    
    if ind_news_items:
        md += "\n---\n\n## 🏢 Industry & Real-World Applications\n\n"
        seen_ind = set()
        count = 0
        for item in ind_news_items:
            if item.get('title') not in seen_ind and count < 8:
                md += f"- **[{item.get('title')}]({item.get('link')})**: {item.get('abstract')}\n"
                seen_ind.add(item.get('title'))
                count += 1

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
        print("No issues found in the last 7 days.")

if __name__ == "__main__":
    main()
