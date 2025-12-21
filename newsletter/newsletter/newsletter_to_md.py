import json
import os
import argparse
from datetime import datetime

HUGO_CONTENT_DIR = "../../content/newsletter"

def load_issue(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def format_markdown(issue):
    date_str = issue.get('issue_date')
    title = f"Issue #{issue.get('issue_number', '1')}: {issue.get('signal', {}).get('title', 'Daily Signal')}"
    
    safe_title = title.replace('"', '\\"')
    safe_description = issue.get('subject', '').replace('"', '\\"')
    
    # AI News Block
    md_ai = ""
    if issue.get('ai_news'):
        for item in issue.get('ai_news', []):
            md_ai += f"- **[{item.get('title', 'Untitled')}]({item.get('link', '#')})**: {item.get('abstract', '')}\n"
    else:
        md_ai = "No AI research updates today."

    # Industry News Block
    md_ind = ""
    if issue.get('industry_news'):
        for item in issue.get('industry_news', []):
            md_ind += f"- **[{item.get('title', 'Untitled')}]({item.get('link', '#')})**: {item.get('abstract', '')}\n"
    else:
        md_ind = "No industry updates today."

    # Frontmatter
    md = f"""---
title: "{safe_title}"
date: {date_str}
description: "{safe_description}"
author: "Protein Design Digest"
tags: ["bioinformatics", "newsletter", "research"]
---

{{{{< newsletter >}}}}

## 🚀 Today's Top Signal

### [{issue.get('signal', {}).get('title')}]({issue.get('signal', {}).get('link')})

#### 🧬 Abstract
{issue.get('signal', {}).get('summary')}

> **Why it matters:** {issue.get('signal', {}).get('why_it_matters')}

---

## 🧪 AI & Research News
{md_ai}

## 🏢 Industry Insight & Applications
{md_ind}

---

## ⚡ Quick Reads
"""
    
    for item in issue.get('quick_reads', []):
        md += f"\n### [{item.get('title', 'Untitled')}]({item.get('link', '#')})\n"
        md += f"{item.get('abstract', '')}\n"

    # Pipeline Tip
    if issue.get('pipeline_tip'):
        md += f"\n## 💡 Pipeline Tip\n"
        md += f"{issue.get('pipeline_tip')}\n"

    md += "\n---\n"
    
    # Community / Tools
    md += "## 🛠️ Resources\n"
    
    if issue.get('dataset'):
        bs = issue['dataset']
        md += f"- **Dataset**: [{bs.get('title')}]({bs.get('link')}) - {bs.get('summary', '')}\n"
    
    if issue.get('tool'):
        tl = issue['tool']
        md += f"- **Tool**: [{tl.get('title')}]({tl.get('link')}) - {tl.get('summary', '')} [View all tools &rarr;](https://recep2244.github.io/portfolio/#opensource)\n"
        
    if issue.get('community'):
        evt = issue['community'].get('event')
        job = issue['community'].get('job')
        if evt:
            md += f"- **Event**: [{evt.get('title')}]({evt.get('link')}) ({evt.get('date')})\n"
        if job:
            md += f"- **Job**: [{job.get('title')}]({job.get('link')}) at {job.get('org')}\n"

    if issue.get('quote'):
        q = issue['quote']
        md += f"\n> *{q.get('text')}* — {q.get('source')}\n"

    return md

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--issues-dir", default="issues")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, HUGO_CONTENT_DIR)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    issues_dir = os.path.join(base_dir, args.issues_dir)
    if not os.path.exists(issues_dir):
        return

    for filename in os.listdir(issues_dir):
        if filename.endswith(".json"):
            issue_data = load_issue(os.path.join(issues_dir, filename))
            md_content = format_markdown(issue_data)
            
            date_part = issue_data.get('issue_date', 'unknown')
            safe_name = f"{date_part}-issue-{issue_data.get('issue_number', '1')}.md"
            
            out_path = os.path.join(output_dir, safe_name)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            print(f"Converted {filename} -> {safe_name}")

if __name__ == "__main__":
    main()
