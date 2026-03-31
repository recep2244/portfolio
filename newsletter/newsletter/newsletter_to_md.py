import json
import os
import argparse
from datetime import datetime

HUGO_CONTENT_DIR = "../../content/newsletter"

def load_issue(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def _estimate_read_minutes(issue):
    """Rough word-count estimate of the issue reading time."""
    parts = [
        (issue.get('signal') or {}).get('summary', ''),
        (issue.get('signal') or {}).get('why_it_matters', ''),
    ]
    for item in issue.get('ai_news') or []:
        parts.append(item.get('abstract', ''))
    for item in issue.get('industry_news') or []:
        parts.append(item.get('abstract', ''))
    for item in issue.get('quick_reads') or []:
        parts.append(item.get('abstract', ''))
    words = sum(len(p.split()) for p in parts if p)
    minutes = max(3, round(words / 200))
    return minutes


def format_markdown(issue):
    date_str = issue.get('issue_date')
    title = f"Issue #{issue.get('issue_number', '1')}: {issue.get('signal', {}).get('title', 'Daily Signal')}"

    safe_title = title.replace('"', '\\"')
    safe_description = issue.get('subject', '').replace('"', '\\"')
    read_minutes = _estimate_read_minutes(issue)

    def coerce_list(value):
        if isinstance(value, list):
            return value
        if isinstance(value, dict):
            return [value]
        return []
    
    def _first_sentence(text):
        """Return the first sentence of text, trimmed to a hook length."""
        text = (text or '').strip()
        first = text.split('. ')[0].rstrip('.')
        return first + '.' if first else text

    # AI News Block
    md_ai = ""
    if issue.get('ai_news'):
        for item in issue.get('ai_news', []):
            hook = _first_sentence(item.get('abstract', ''))
            md_ai += f"- **[{item.get('title', 'Untitled')}]({item.get('link', '#')})** — {hook}\n"
    else:
        md_ai = "Nothing jumped out today — check back tomorrow.\n"

    # Industry News Block
    md_ind = ""
    if issue.get('industry_news'):
        for item in issue.get('industry_news', []):
            hook = _first_sentence(item.get('abstract', ''))
            md_ind += f"- **[{item.get('title', 'Untitled')}]({item.get('link', '#')})** — {hook}\n"
    else:
        md_ind = "Quiet day in the industry — nothing material to report.\n"

    # Frontmatter
    md = f"""---
title: "{safe_title}"
date: {date_str}
description: "{safe_description}"
author: "Recep Adiyaman"
tags: ["bioinformatics", "newsletter", "research"]
readingTime: {read_minutes}
---

{{{{< newsletter >}}}}

## Signal of the Day

### [{issue.get('signal', {}).get('title')}]({issue.get('signal', {}).get('link')})

{issue.get('signal', {}).get('summary')}

> **Why this matters:** {issue.get('signal', {}).get('why_it_matters')}

---
"""

    # Optional Additional Signals
    extras = issue.get('signal_extras') or []
    if extras:
        md += "\n## Also Worth Reading\n"
        for item in extras:
            md += f"\n### [{item.get('title', 'Untitled')}]({item.get('link', '#')})\n"
            md += f"{item.get('abstract', '')}\n"
        md += "\n---\n"

    md += f"""

## Research & AI Updates
{md_ai}

## From the Industry
{md_ind}

---

## Quick Reads
"""
    
    for item in issue.get('quick_reads', []):
        md += f"\n### [{item.get('title', 'Untitled')}]({item.get('link', '#')})\n"
        abstract = (item.get('abstract') or '').strip()
        # Show just the first sentence as a hook — keeps the section scannable
        first_sentence = abstract.split('. ')[0].rstrip('.')
        if first_sentence and len(first_sentence) < len(abstract):
            md += f"{first_sentence}. [Read more →]({item.get('link', '#')})\n"
        elif abstract:
            md += f"{abstract}\n"

    # Pipeline Tip
    if issue.get('pipeline_tip'):
        md += f"\n## Pipeline Tip\n"
        md += f"{issue.get('pipeline_tip')}\n"

    md += "\n---\n"

    # Community / Tools
    md += "## Resources & Tools\n"
    
    datasets = coerce_list(issue.get('dataset'))
    tools = coerce_list(issue.get('tool'))

    for idx, bs in enumerate(datasets):
        md += f"- **Dataset**: [{bs.get('title')}]({bs.get('link')}) - {bs.get('summary', '')}\n"
    
    for tl in tools:
        md += f"- **Tool**: [{tl.get('title')}]({tl.get('link')}) - {tl.get('summary', '')} [View all tools &rarr;](https://recep2244.github.io/portfolio/#opensource)\n"
        
    if issue.get('community'):
        evt_list = coerce_list(issue['community'].get('event'))
        job_list = coerce_list(issue['community'].get('job'))
        for evt in evt_list:
            md += f"- **Event**: [{evt.get('title')}]({evt.get('link')}) ({evt.get('date')})\n"
        for job in job_list:
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
