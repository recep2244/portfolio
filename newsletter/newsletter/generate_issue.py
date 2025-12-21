#!/usr/bin/env python3
import argparse
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

DEFAULT_TIMEZONE = "Europe/London"


@dataclass
class Paper:
    title: str
    summary: str
    link: str
    published: datetime
    source: str


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def fetch_url(url, user_agent):
    req = Request(url, headers={"User-Agent": user_agent})
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def ensure_timezone(dt, timezone):
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone)
    return dt


def parse_date(value, timezone):
    if not value:
        return None
    value = value.strip()
    try:
        if value.endswith("Z"):
            return ensure_timezone(
                datetime.fromisoformat(value.replace("Z", "+00:00")), timezone
            )
        return ensure_timezone(datetime.fromisoformat(value), timezone)
    except ValueError:
        try:
            return ensure_timezone(datetime.strptime(value, "%Y-%m-%d"), timezone)
        except ValueError:
            return None


def parse_rss_date(value, timezone):
    if not value:
        return None
    try:
        return ensure_timezone(parsedate_to_datetime(value.strip()), timezone)
    except (TypeError, ValueError):
        return parse_date(value, timezone)


def clean_text(text):
    if not text:
        return ""
    # Strip HTML tags
    clean = re.sub(r'<[^>]*>', ' ', text)
    # Normalize whitespace
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean

def first_sentence(text, limit=320):
    cleaned = clean_text(text)
    if not cleaned:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", cleaned)
    sentence = parts[0] if parts else cleaned
    if len(sentence) > limit:
        sentence = sentence[: limit - 3].rstrip() + "..."
    return sentence


def normalize_title(title):
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def build_arxiv_query(keywords):
    keyword_expr = " OR ".join([f'all:"{kw}"' for kw in keywords])
    return f"({keyword_expr})"


def fetch_arxiv(keywords, max_results, user_agent, timezone):
    query = build_arxiv_query(keywords)
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = "http://export.arxiv.org/api/query?" + urlencode(params)
    data = fetch_url(url, user_agent).decode("utf-8")

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(data)
    papers = []
    for entry in root.findall("atom:entry", ns):
        title = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip()
        summary = (
            entry.findtext("atom:summary", default="", namespaces=ns) or ""
        ).strip()
        link = entry.findtext("atom:id", default="", namespaces=ns)
        published_raw = entry.findtext("atom:published", default="", namespaces=ns)
        published = parse_date(published_raw, timezone)
        if not title or not link or not published:
            continue
        papers.append(
            Paper(
                title=title,
                summary=summary,
                link=link,
                published=published,
                source="arXiv",
            )
        )
    return papers


def build_epmc_query(keywords, start_date, end_date):
    keyword_expr = " OR ".join([f'TITLE_ABS:"{kw}"' for kw in keywords])
    date_expr = f"FIRST_PDATE:[{start_date} TO {end_date}]"
    return f"({keyword_expr}) AND {date_expr}"


def epmc_link(result):
    doi = (result.get("doi") or "").strip()
    if doi:
        return f"https://doi.org/{doi}"
    source = (result.get("source") or "").strip()
    result_id = (result.get("id") or "").strip()
    if source and result_id:
        return f"https://europepmc.org/article/{source}/{result_id}"
    title = (result.get("title") or "").strip()
    if title:
        return f"https://europepmc.org/search?query={quote(title)}"
    return "https://europepmc.org/"


def fetch_europe_pmc(keywords, start_date, end_date, page_size, user_agent, timezone):
    query = build_epmc_query(keywords, start_date, end_date)
    params = {
        "query": query,
        "format": "json",
        "pageSize": page_size,
        "resultType": "core",
    }
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(params)
    data = json.loads(fetch_url(url, user_agent).decode("utf-8"))
    results = data.get("resultList", {}).get("result", [])
    papers = []
    for result in results:
        title = (result.get("title") or "").strip()
        summary = (result.get("abstractText") or "").strip()
        published_raw = (result.get("firstPublicationDate") or "").strip()
        if not published_raw:
            published_raw = (result.get("pubYear") or "").strip()
        published = parse_date(published_raw, timezone)
        link = epmc_link(result)
        if not title or not link or not published:
            continue
        papers.append(
            Paper(
                title=title,
                summary=summary,
                link=link,
                published=published,
                source="Europe PMC",
            )
        )
    return papers


def build_pubmed_query(keywords):
    keyword_expr = " OR ".join([f'"{kw}"[Title/Abstract]' for kw in keywords])
    return f"({keyword_expr})"


def parse_pubmed_month(value):
    if not value:
        return 1
    value = value.strip()
    if value.isdigit():
        month = int(value)
        return month if 1 <= month <= 12 else 1
    lookup = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }
    short = value[:3].title()
    return lookup.get(short, 1)


def element_text(node):
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def parse_pubmed_date_node(node, timezone):
    if node is None:
        return None
    year_text = element_text(node.find("./Year"))
    month_text = element_text(node.find("./Month"))
    day_text = element_text(node.find("./Day"))
    medline = element_text(node.find("./MedlineDate"))

    year = None
    if year_text.isdigit():
        year = int(year_text)
    elif medline:
        match = re.search(r"(\d{4})", medline)
        if match:
            year = int(match.group(1))

    if not year:
        return None
    month = parse_pubmed_month(month_text or medline)
    day = int(day_text) if day_text.isdigit() else 1
    return datetime(year, month, day, tzinfo=timezone)


def chunk_list(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def fetch_pubmed(keywords, start_date, end_date, max_results, user_agent, timezone, email=None, tool=None, api_key=None):
    query = build_pubmed_query(keywords)
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
        "mindate": start_date,
        "maxdate": end_date,
        "datetype": "pdat",
    }
    if email:
        params["email"] = email
    if tool:
        params["tool"] = tool
    if api_key:
        params["api_key"] = api_key

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urlencode(params)
    data = json.loads(fetch_url(url, user_agent).decode("utf-8"))
    id_list = data.get("esearchresult", {}).get("idlist", [])
    if not id_list:
        return []

    papers = []
    for batch in chunk_list(id_list, 200):
        fetch_params = {
            "db": "pubmed",
            "id": ",".join(batch),
            "retmode": "xml",
        }
        if email:
            fetch_params["email"] = email
        if tool:
            fetch_params["tool"] = tool
        if api_key:
            fetch_params["api_key"] = api_key
        fetch_url_str = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
            + urlencode(fetch_params)
        )
        xml_data = fetch_url(fetch_url_str, user_agent)
        root = ET.fromstring(xml_data)
        for article in root.findall(".//PubmedArticle"):
            title = element_text(article.find(".//ArticleTitle"))
            abstract_nodes = article.findall(".//AbstractText")
            summary = " ".join([element_text(node) for node in abstract_nodes]).strip()
            pmid = element_text(article.find(".//PMID"))
            pubdate = parse_pubmed_date_node(
                article.find(".//JournalIssue/PubDate"), timezone
            )
            if not pubdate:
                pubdate = parse_pubmed_date_node(article.find(".//ArticleDate"), timezone)
            if not title or not pmid or not pubdate:
                continue
            papers.append(
                Paper(
                    title=title,
                    summary=summary,
                    link=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    published=pubdate,
                    source="PubMed",
                )
            )
    return papers


def biorxiv_link(item):
    doi = (item.get("doi") or "").strip()
    if doi:
        return f"https://doi.org/{doi}"
    biorxiv_url = (item.get("biorxiv_url") or "").strip()
    if biorxiv_url:
        return biorxiv_url
    if doi:
        return f"https://www.biorxiv.org/content/{doi}"
    return "https://www.biorxiv.org/"


def fetch_biorxiv(keywords, start_date, end_date, max_results, user_agent, timezone, server="biorxiv"):
    if server == "biorxiv":
        source_name = "bioRxiv"
    elif server == "medrxiv":
        source_name = "medRxiv"
    else:
        source_name = server
    papers = []
    cursor = 0
    page_size = 100
    while len(papers) < max_results:
        url = (
            f"https://api.biorxiv.org/details/{server}/"
            f"{start_date}/{end_date}/{cursor}"
        )
        data = json.loads(fetch_url(url, user_agent).decode("utf-8"))
        collection = data.get("collection", [])
        if not collection:
            break
        for item in collection:
            title = (item.get("title") or "").strip()
            summary = (item.get("abstract") or "").strip()
            published_raw = (item.get("date") or "").strip()
            published = parse_date(published_raw, timezone)
            link = biorxiv_link(item)
            if not title or not published:
                continue
            papers.append(
                Paper(
                    title=title,
                    summary=summary,
                    link=link,
                    published=published,
                    source=source_name,
                )
            )
            if len(papers) >= max_results:
                break
        cursor += page_size
    return papers


def find_first_text(element, tags):
    for tag in tags:
        node = element.find(f".//{{*}}{tag}")
        if node is not None:
            text = element_text(node)
            if text:
                return text
    return ""



def fetch_semantic_scholar(keywords, start_date, end_date, max_results, user_agent, timezone):
    # Combine keywords carefully. Semantic Scholar search logic is broad.
    # We'll search for the first few keywords to keep it relevant.
    query = " OR ".join(keywords[:5]) 
    fields = "title,abstract,url,publicationDate,venue"
    params = {
        "query": query,
        "limit": max_results,
        "fields": fields,
        "year": f"{start_date.split('-')[0]}-", # Search from start year onwards
    }
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urlencode(params)
    
    try:
        raw_data = fetch_url(url, user_agent).decode("utf-8")
        data = json.loads(raw_data)
    except Exception as e:
        print(f"Warning: Semantic Scholar fetch failed: {e}")
        return []

    if "data" not in data:
        return []

    papers = []
    for item in data["data"]:
        title = (item.get("title") or "").strip()
        summary = (item.get("abstract") or "").strip()
        link = (item.get("url") or "").strip()
        pub_date_str = item.get("publicationDate")
        
        # Parse date
        published = parse_date(pub_date_str, timezone)
        
        # Filter strictly by our date range (API 'year' param is loose)
        if published:
            pub_dt_str = published.date().isoformat()
            if not (start_date <= pub_dt_str <= end_date):
               continue

        if not title or not link or not published:
            continue

        papers.append(
            Paper(
                title=title,
                summary=summary,
                link=link,
                published=published,
                source="Semantic Scholar",
            )
        )
    return papers


def fetch_rss_feed(feed, keywords, max_results, user_agent, timezone):
    url = (feed.get("url") or "").strip()
    name = (feed.get("name") or "RSS").strip()
    if not url or "INSERT_YOUR" in url:
        return []
    try:
        data = fetch_url(url, user_agent)
        root = ET.fromstring(data)
    except Exception:
        print(f"Warning: Failed to parse RSS feed: {url}")
        return []
        
    papers = []

    if root.tag.endswith("feed"):
        entries = root.findall(".//{*}entry")
        for entry in entries:
            title = find_first_text(entry, ["title"])
            summary = find_first_text(entry, ["summary", "content"])
            link = ""
            for link_node in entry.findall(".//{*}link"):
                rel = link_node.attrib.get("rel", "alternate")
                href = link_node.attrib.get("href", "")
                if rel == "alternate" and href:
                    link = href
                    break
                if not link and href:
                    link = href
            published_raw = find_first_text(entry, ["published", "updated"])
            published = parse_rss_date(published_raw, timezone)
            if not title or not link or not published:
                continue
            papers.append(
                Paper(
                    title=title,
                    summary=summary,
                    link=link,
                    published=published,
                    source=name,
                )
            )
            if len(papers) >= max_results:
                break
    else:
        items = root.findall(".//item")
        if not items:
            items = root.findall(".//{*}item")
        for item in items:
            title = find_first_text(item, ["title"])
            summary = find_first_text(item, ["description", "encoded", "content"])
            link = find_first_text(item, ["link"])
            published_raw = find_first_text(item, ["pubDate", "date", "updated"])
            published = parse_rss_date(published_raw, timezone)
            if not title or not link or not published:
                continue
            papers.append(
                Paper(
                    title=title,
                    summary=summary,
                    link=link,
                    published=published,
                    source=name,
                )
            )
            if len(papers) >= max_results:
                break

    return papers


def keyword_score(text, keywords, weight):
    score = 0
    text = text.lower()
    for kw in keywords:
        if kw in text:
            score += weight
    return score


def score_paper(paper, keywords):
    title_score = keyword_score(paper.title, keywords, 3)
    summary_score = keyword_score(paper.summary, keywords, 1)
    return title_score + summary_score


def summarize_paper(paper):
    summary = clean_text(paper.summary)
    if not summary:
        summary = "No abstract available."
    return summary


def why_it_matters(paper):
    text = f"{paper.title} {paper.summary}".lower()
    if "structure" in text and "prediction" in text:
        return "Critical for improving fold accuracy and reducing structural uncertainty in de novo design."
    if "de novo" in text or "design" in text:
        return "Expands the searchable sequence space for novel folds and high-affinity binders."
    if "engineering" in text or "enzyme" in text:
        return "Provides actionable mutations to enhance catalytic efficiency or thermostability."
    if "benchmark" in text or "dataset" in text:
        return "Essential ground-truth data for validating next-gen foundation models like Boltz or Chai."
    if "docking" in text or "ligand" in text:
        return "Enhances small-molecule or peptide docking accuracy for targeted drug discovery."
    return "A high-confidence signal for modern protein engineering and structural biology pipelines."


def dedupe_papers(papers):
    seen = {}
    for paper in papers:
        key = normalize_title(paper.title)
        if key in seen:
            continue
        seen[key] = paper
    return list(seen.values())


def filter_by_date(papers, start_dt, end_dt, timezone):
    filtered = []
    for paper in papers:
        if not paper.published:
            continue
        published = ensure_timezone(paper.published, timezone)
        if start_dt <= published <= end_dt:
            filtered.append(paper)
    return filtered


def format_item(paper):
    return {
        "title": paper.title,
        "note": f"{paper.source} - {paper.published.date().isoformat()}",
        "link": paper.link,
        "abstract": clean_text(paper.summary),
    }


def pick_pool_item(items, index, fallback):
    if not items:
        return fallback
    return items[index % len(items)]


def build_issue_number(issues_dir):
    if not os.path.isdir(issues_dir):
        return 1
    count = 0
    for name in os.listdir(issues_dir):
        if name.endswith(".json"):
            count += 1
    return count + 1


def build_issue(config, issue_date, timezone):
    user_agent = config.get("user_agent", "GenomeDaily/1.0")
    lookback_days = int(config.get("lookback_days", 7))
    max_results = int(config.get("max_results_per_source", 50))
    keywords = [kw.lower() for kw in config.get("keywords", [])]
    if not keywords:
        raise ValueError("No keywords configured")

    start_date = issue_date - timedelta(days=lookback_days)
    end_date = issue_date
    start_dt = datetime.combine(start_date, datetime.min.time(), tzinfo=timezone)
    end_dt = datetime.combine(end_date, datetime.max.time(), tzinfo=timezone)

    papers = []
    sources = config.get("sources", {})

    if sources.get("arxiv", {}).get("enabled", True):
        arxiv_max = int(sources.get("arxiv", {}).get("max_results", max_results))
        papers.extend(fetch_arxiv(keywords, arxiv_max, user_agent, timezone))

    if sources.get("europe_pmc", {}).get("enabled", True):
        page_size = int(sources.get("europe_pmc", {}).get("page_size", max_results))
        papers.extend(
            fetch_europe_pmc(
                keywords,
                start_date.isoformat(),
                end_date.isoformat(),
                page_size,
                user_agent,
                timezone,
            )
        )

    if sources.get("biorxiv", {}).get("enabled", False):
        biorxiv_max = int(sources.get("biorxiv", {}).get("max_results", max_results))
        papers.extend(
            fetch_biorxiv(
                keywords,
                start_date.isoformat(),
                end_date.isoformat(),
                biorxiv_max,
                user_agent,
                timezone,
                server="biorxiv",
            )
        )

    if sources.get("medrxiv", {}).get("enabled", False):
        medrxiv_max = int(sources.get("medrxiv", {}).get("max_results", max_results))
        papers.extend(
            fetch_biorxiv(
                keywords,
                start_date.isoformat(),
                end_date.isoformat(),
                medrxiv_max,
                user_agent,
                timezone,
                server="medrxiv",
            )
        )

    if sources.get("pubmed", {}).get("enabled", False):
        pubmed_max = int(sources.get("pubmed", {}).get("max_results", max_results))
        pubmed_email = sources.get("pubmed", {}).get("email")
        pubmed_tool = sources.get("pubmed", {}).get("tool")
        pubmed_key = sources.get("pubmed", {}).get("api_key")
        papers.extend(
            fetch_pubmed(
                keywords,
                start_date.isoformat(),
                end_date.isoformat(),
                pubmed_max,
                user_agent,
                timezone,
                email=pubmed_email,
                tool=pubmed_tool,
                api_key=pubmed_key,
            )
        )
    
    if sources.get("semantic_scholar", {}).get("enabled", True):
        ss_max = int(sources.get("semantic_scholar", {}).get("max_results", max_results))
        papers.extend(
            fetch_semantic_scholar(
                keywords,
                start_date.isoformat(),
                end_date.isoformat(),
                ss_max,
                user_agent,
                timezone
            )
        )

    if sources.get("rss", {}).get("enabled", False):
        feed_max = int(sources.get("rss", {}).get("max_results", max_results))
        feeds = sources.get("rss", {}).get("feeds", [])
        for feed in feeds:
            papers.extend(fetch_rss_feed(feed, keywords, feed_max, user_agent, timezone))

    papers = dedupe_papers(papers)
    papers = filter_by_date(papers, start_dt, end_dt, timezone)

    scored = []
    for paper in papers:
        score = score_paper(paper, keywords)
        if score > 0:
            scored.append((score, paper))

    scored.sort(key=lambda item: (item[0], item[1].published), reverse=True)

    if len(scored) < 4:
        raise ValueError("Not enough papers found. Increase lookback_days or adjust keywords.")

    signal_paper = scored[0][1]
    quick_papers = [item[1] for item in scored[1:4]]

    issue_number = build_issue_number(config.get("issues_dir", "newsletter/issues"))

    dataset_pool = config.get("dataset_pool", [])
    tool_pool = config.get("tool_pool", [])
    quotes = config.get("quotes", [])
    community = config.get("community", {})
    events = community.get("events", [])
    jobs = community.get("jobs", [])

    day_index = issue_date.toordinal()
    dataset = pick_pool_item(
        dataset_pool,
        day_index,
        {"title": "Add a dataset", "summary": "", "link": "https://example.com"},
    )
    tool = pick_pool_item(
        tool_pool,
        day_index + 1,
        {"title": "Add a tool", "summary": "", "link": "https://example.com"},
    )
    event = pick_pool_item(
        events,
        day_index,
        {"title": "Submit your event", "date": issue_date.isoformat(), "link": "mailto:you@example.com"},
    )
    job = pick_pool_item(
        jobs,
        day_index + 1,
        {"title": "Hiring? Send your role", "org": "Your org", "link": "mailto:you@example.com"},
    )
    quote = pick_pool_item(
        quotes,
        day_index,
        {"text": "Data is the signal, models are the instruments.", "source": "Genome Daily"},
    )

    signal_summary = signal_paper.summary

    ai_news = []
    ai_cfg = config.get("ai_news", {})
    if ai_cfg.get("enabled", False):
        ai_feeds = ai_cfg.get("feeds", [])
        ai_keywords = [kw.lower() for kw in ai_cfg.get("keywords", [])]
        ai_max = int(ai_cfg.get("max_items", 3))
        ai_items = []
        for feed in ai_feeds:
            ai_items.extend(fetch_rss_feed(feed, ai_keywords, ai_max, user_agent, timezone))
        if ai_items:
            ai_items = dedupe_papers(ai_items)
            # Relaxed filter: if no news in last 7 days, take the latest ones regardless of date
            strict_items = filter_by_date(ai_items, start_dt, end_dt, timezone)
            if not strict_items:
                ai_items.sort(key=lambda item: item.published, reverse=True)
                strict_items = ai_items[:ai_max]
            
            if ai_keywords and not strict_items:
                 ai_items.sort(key=lambda item: (score_paper(item, ai_keywords), item.published), reverse=True)
                 strict_items = ai_items[:ai_max]
            elif ai_keywords:
                scored_ai = []
                for item in strict_items:
                    score = score_paper(item, ai_keywords)
                    scored_ai.append((score, item))
                scored_ai.sort(key=lambda item: (item[0], item[1].published), reverse=True)
                strict_items = [item[1] for item in scored_ai]
            
            ai_news = [format_item(item) for item in strict_items[:ai_max]]

    issue = {
        "newsletter_name": config.get("newsletter_name", "Genome Daily"),
        "newsletter_tagline": config.get("newsletter_tagline", "Bioinformatics signals, every morning"),
        "issue_date": issue_date.isoformat(),
        "issue_number": issue_number,
        "edition_time": config.get("edition_time", "04:00 UK"),
        "subject": f"{config.get('subject_prefix', 'Genome Daily')} - {issue_date.isoformat()} - {signal_paper.title}",
        "preheader_text": config.get(
            "preheader_text", "Top signal, quick reads, and a pipeline tip in under 4 minutes."
        ),
        "signal": {
            "title": signal_paper.title,
            "summary": clean_text(signal_paper.summary),
            "why_it_matters": why_it_matters(signal_paper),
            "link": signal_paper.link,
        },
        "quick_reads": [
            format_item(paper) for paper in quick_papers
        ],
        "ai_news": ai_news,
        "dataset": dataset,
        "tool": tool,
        "pipeline_tip": pick_pool_item(
            config.get("pipeline_tips", [
                "Pin reference genomes by checksum to avoid version drift.",
                "Use local MSA generation to bypass speed bottlenecks in structure prediction."
            ]),
            day_index,
            "Use versioned containers for reproducible protein design."
        ),
        "community": {
            "event": event,
            "job": job,
        },
        "quote": quote,
        "manage_prefs_link": config.get("manage_prefs_link", ""),
        "unsubscribe_link": config.get("unsubscribe_link", ""),
        "sender_address": config.get("sender_address", ""),
    }

    return issue


def main():
    parser = argparse.ArgumentParser(description="Generate a daily bioinformatics issue")
    parser.add_argument("--config", default="newsletter/generate_config.json")
    parser.add_argument("--issue-date", default="today")
    parser.add_argument("--issues-dir", default="newsletter/issues")
    parser.add_argument("--timezone", default=DEFAULT_TIMEZONE)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    timezone = ZoneInfo(args.timezone)
    if args.issue_date.lower() == "today":
        issue_date = datetime.now(timezone).date()
    else:
        issue_date = datetime.strptime(args.issue_date, "%Y-%m-%d").date()

    config = load_json(args.config)
    config["issues_dir"] = args.issues_dir

    issue = build_issue(config, issue_date, timezone)

    os.makedirs(args.issues_dir, exist_ok=True)
    issue_path = os.path.join(args.issues_dir, f"{issue_date.isoformat()}.json")
    save_json(issue_path, issue)

    if args.dry_run:
        print(f"Generated issue: {issue_path}")
        return

    print(f"Generated issue: {issue_path}")


if __name__ == "__main__":
    main()
