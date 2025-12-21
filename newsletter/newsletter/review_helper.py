#!/usr/bin/env python3
"""
Paper Review Helper
Integrates the review interface into the newsletter workflow
"""
import json
import sys
from pathlib import Path


def create_curated_issue(original_issue_path, selected_papers_path, output_path):
    """
    Create a new issue JSON with only selected papers
    
    Args:
        original_issue_path: Path to the original generated issue JSON
        selected_papers_path: Path to the JSON from review interface
        output_path: Where to save the curated issue
    """
    # Load original issue
    with open(original_issue_path, 'r') as f:
        original = json.load(f)
    
    # Load selected papers
    with open(selected_papers_path, 'r') as f:
        selected = json.load(f)
    
    # Create curated issue
    curated = original.copy()
    
    # Separate selected papers by section
    quick_reads = [p for p in selected if p.get('section') == 'Quick Reads']
    ai_news = [p for p in selected if p.get('section') == 'AI News']
    industry_news = [p for p in selected if p.get('section') == 'Industry News']
    
    # Remove section markers from papers
    for papers in [quick_reads, ai_news, industry_news]:
        for p in papers:
            p.pop('section', None)
    
    # Update the curated issue
    curated['quick_reads'] = quick_reads if quick_reads else original.get('quick_reads', [])
    curated['ai_news'] = ai_news if ai_news else original.get('ai_news', [])
    curated['industry_news'] = industry_news if industry_news else original.get('industry_news', [])
    
    # Save curated issue
    with open(output_path, 'w') as f:
        json.dump(curated, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Curated issue created: {output_path}")
    print(f"   • Quick Reads: {len(curated['quick_reads'])}")
    print(f"   • AI News: {len(curated['ai_news'])}")
    print(f"   • Industry News: {len(curated['industry_news'])}")
    
    return output_path


def main():
    if len(sys.argv) < 3:
        print("Usage: python review_helper.py <original_issue.json> <selected_papers.json> [output.json]")
        print("\nExample:")
        print("  python review_helper.py issues/2025-01-15.json selected-papers-2025-01-15.json issues/2025-01-15-curated.json")
        sys.exit(1)
    
    original_path = sys.argv[1]
    selected_path = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else original_path.replace('.json', '-curated.json')
    
    if not Path(original_path).exists():
        print(f"❌ Original issue not found: {original_path}")
        sys.exit(1)
    
    if not Path(selected_path).exists():
        print(f"❌ Selected papers file not found: {selected_path}")
        sys.exit(1)
    
    create_curated_issue(original_path, selected_path, output_path)


if __name__ == '__main__':
    main()
