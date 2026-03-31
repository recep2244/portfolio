import os
import re
import requests
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from utils import load_json, coerce_list

# Optional: Using tweepy for Twitter if available, otherwise we can use direct requests
try:
    import tweepy
except ImportError:
    tweepy = None

SOCIAL_TAGS = ["#ProteinDesign", "#StructuralBiology", "#Bioinformatics", "#ProteinEngineering"]
SUBSCRIBE_LABEL = "Subnewsletter"
TWITTER_LIMIT = 280
BLUESKY_LIMIT = 300
DEFAULT_BASE_URL = "https://recep2244.github.io/portfolio/#newsletter"
DEFAULT_TWITTER_TEMPLATE = "{header}\n{title}\n{summary}\n{subscribe}\n{link}\n{tags}"
DEFAULT_BLUESKY_TEMPLATE = "{header}\n{title}\n{summary}\n{engagement}\n{link}\n{subscribe}\n{tags}"
DEFAULT_TWITTER_THREAD_TEMPLATE = "{header}\n{title}\n{summary}\n{engagement}\n{tags}"

_HUMAN_OPENERS = [
    "This one caught my eye today:",
    "Worth your time if you work on proteins:",
    "Came across this and had to share:",
    "Today's most interesting result:",
    "Something I keep thinking about:",
    "This paper changed how I see the problem:",
    "A result worth reading slowly:",
    "From today's preprints — genuinely interesting:",
    "Sharing what's on my desk today:",
    "If you only read one paper today, make it this:",
    "Hard to summarise briefly, but here's the gist:",
    "This is the kind of work I find exciting:",
    "Today's signal from the literature:",
    "Filed this under: things I wish I'd seen sooner:",
    "An underappreciated approach getting renewed attention:",
]


def pick_human_opener(seed_text=None):
    import hashlib
    if seed_text:
        idx = int(hashlib.md5(seed_text.encode()).hexdigest(), 16) % len(_HUMAN_OPENERS)
    else:
        idx = datetime.now().day % len(_HUMAN_OPENERS)
    return _HUMAN_OPENERS[idx]


_ENGAGEMENT_HOOKS = [
    "What's your take? 👇",
    "Have you tried something similar?",
    "Curious what the community thinks.",
    "Worth testing in your pipeline?",
    "Does this match what you're seeing?",
    "Anyone working on something related?",
    "Thoughts? Reply and let me know.",
    "Would love to hear your experience with this.",
    "What would you do differently?",
    "Drop a 🧬 if this is relevant to your work.",
    "Is this gap something you've run into?",
    "Would this change your approach?",
    "What are the limits you'd push next?",
    "Have you benchmarked anything like this?",
    "What's missing from this picture?",
]


def pick_engagement_hook(seed_text=None):
    import hashlib
    if seed_text:
        h = int(hashlib.md5((seed_text + "_eng").encode()).hexdigest(), 16)
        idx = h % len(_ENGAGEMENT_HOOKS)
    else:
        idx = (datetime.now().day + 7) % len(_ENGAGEMENT_HOOKS)
    return _ENGAGEMENT_HOOKS[idx]

def load_issue(issue_date, issues_dir):
    filename = f"{issue_date}.json"
    filepath = os.path.join(issues_dir, filename)
    if not os.path.exists(filepath):
        print(f"Issue file not found: {filepath}")
        return None
    return load_json(filepath)

def load_env():
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(dotenv_path=env_path, override=False)


def shorten_text(text, max_len):
    if max_len <= 0:
        return ""
    if len(text) <= max_len:
        return text
    if max_len <= 3:
        return text[:max_len]
    return text[: max_len - 3].rstrip() + "..."


def extract_first_url(text):
    match = re.search(r"https?://\S+", text or "")
    return match.group(0) if match else ""


def extract_title_line(text, fallback):
    lines = [line.strip() for line in (text or "").splitlines() if line.strip()]
    if len(lines) >= 2:
        return lines[1]
    return fallback


def ensure_subscribe_label(text, limit):
    if not text:
        return text
    if SUBSCRIBE_LABEL in text:
        return text
    line = f"\n{SUBSCRIBE_LABEL}"
    if len(text) + len(line) <= limit:
        return text + line
    lines = text.splitlines()
    if lines and lines[-1].startswith("#"):
        lines.pop()
        text = "\n".join(lines)
        if SUBSCRIBE_LABEL in text:
            return text
        if len(text) + len(line) <= limit:
            return text + line
    return text


def normalize_text_for_compare(value):
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def is_redundant_summary(title, summary):
    if not title or not summary:
        return False
    title_norm = normalize_text_for_compare(title)
    summary_norm = normalize_text_for_compare(summary)
    if not title_norm or not summary_norm:
        return False
    return (
        summary_norm == title_norm
        or summary_norm.startswith(title_norm)
        or title_norm.startswith(summary_norm)
    )


def build_external_embed(title, summary, url):
    if not url:
        return None
    safe_title = shorten_text(title or pick_human_opener(), 120)
    safe_summary = shorten_text(summary or "", 200)
    return {
        "$type": "app.bsky.embed.external",
        "external": {
            "uri": url,
            "title": safe_title,
            "description": safe_summary,
        },
    }


def format_issue_date(value):
    if not value:
        return ""
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return ""
    return parsed.strftime("%d.%m.%y")


def build_social_text(
    title,
    summary,
    signal_link,
    sub_url,
    limit,
    include_tags=True,
    issue_date=None,
    subscribe_url_in_text=False,
    extra_lines=None,
    header_label=None,
    url_length=None,
    omit_long_links=False,
):
    def measure_text(text):
        if not url_length:
            return len(text)
        return len(re.sub(r"https?://\S+", "x" * url_length, text))

    header = header_label or pick_human_opener(title)
    formatted_date = format_issue_date(issue_date)
    if formatted_date and header_label:
        header = f"{header} · {formatted_date}"
    title = title or "Daily signal"
    tags_line = " ".join(SOCIAL_TAGS) if include_tags else ""

    tail_lines = []
    subscribe_line = (
        f"{SUBSCRIBE_LABEL} {sub_url}" if subscribe_url_in_text else SUBSCRIBE_LABEL
    )
    if subscribe_url_in_text and signal_link:
        tail_lines.append(subscribe_line)
        tail_lines.append(f"{signal_link}")
    else:
        if signal_link:
            tail_lines.append(f"{signal_link}")
        tail_lines.append(subscribe_line)

    if extra_lines is None:
        extra_lines = []

    base_lines = [header] + tail_lines
    if tags_line:
        base_lines.append(tags_line)
    base_without_title = "\n".join(base_lines)
    min_title = "Signal"
    base_len = measure_text(base_without_title) + measure_text(min_title) + 1
    remaining_for_extras = max(0, limit - base_len - 1)
    per_extra = 0
    if extra_lines:
        per_extra = max(0, remaining_for_extras // len(extra_lines))
    reserve_extras = len(extra_lines) * (per_extra + 1)
    allowed = max(0, limit - measure_text(base_without_title) - reserve_extras - 1)
    title_line = shorten_text(title, allowed)
    if not title_line:
        title_line = "Signal"

    lines = [header, title_line] + tail_lines
    if tags_line:
        lines.append(tags_line)

    def try_add_line(text, index):
        current = "\n".join(lines)
        remaining = limit - measure_text(current) - 1
        if remaining <= 0:
            return False
        line_text = shorten_text(text, remaining)
        if not line_text:
            return False
        lines.insert(index, line_text)
        return True

    insert_idx = 2
    for extra in extra_lines:
        extra_text = shorten_text(extra, per_extra) if per_extra else extra
        if extra_text and try_add_line(extra_text, insert_idx):
            insert_idx += 1
    if summary:
        if try_add_line(summary, insert_idx):
            insert_idx += 1
    engagement_hook = pick_engagement_hook(title)
    if engagement_hook:
        try_add_line(engagement_hook, insert_idx)

    def measure(values):
        return measure_text("\n".join(values))

    safe_lines = list(lines)
    if tags_line and measure(safe_lines) > limit:
        safe_lines.pop()
    tail_start = len(safe_lines) - len(tail_lines)
    while measure(safe_lines) > limit and tail_start > 2:
        del safe_lines[tail_start - 1]
        tail_start -= 1
    if measure(safe_lines) > limit:
        fixed_lines = [header] + tail_lines
        fixed_len = len("\n".join(fixed_lines))
        max_title = max(0, limit - fixed_len - 1)
        short_title = shorten_text(title, max_title) or shorten_text("Signal", max_title)
        rebuilt = [header, short_title] + tail_lines
        if tags_line and measure(rebuilt + [tags_line]) <= limit:
            rebuilt.append(tags_line)
        rebuilt_text = "\n".join(rebuilt)
        if omit_long_links and signal_link and len(rebuilt_text) > limit:
            return build_social_text(
                title,
                summary,
                "",
                sub_url,
                limit,
                include_tags=include_tags,
                issue_date=issue_date,
                subscribe_url_in_text=subscribe_url_in_text,
                extra_lines=extra_lines,
                header_label=header_label,
                url_length=url_length,
                omit_long_links=False,
            )
        return rebuilt_text

    final_text = "\n".join(safe_lines)
    if omit_long_links and signal_link and len(final_text) > limit:
        return build_social_text(
            title,
            summary,
            "",
            sub_url,
            limit,
            include_tags=include_tags,
            issue_date=issue_date,
            subscribe_url_in_text=subscribe_url_in_text,
            extra_lines=extra_lines,
            header_label=header_label,
            url_length=url_length,
            omit_long_links=False,
        )
    return final_text


def build_bluesky_facets(text, subscribe_url=None, paper_url=None):
    facets = []
    seen = set()

    def add_facet(start, end, feature):
        byte_start = len(text[:start].encode("utf-8"))
        byte_end = len(text[:end].encode("utf-8"))
        key = (
            byte_start,
            byte_end,
            feature.get("$type"),
            feature.get("uri"),
            feature.get("tag"),
        )
        if key in seen:
            return
        seen.add(key)
        facets.append(
            {
                "index": {
                    "byteStart": byte_start,
                    "byteEnd": byte_end,
                },
                "features": [feature],
            }
        )

    if paper_url:
        idx = text.find(paper_url)
        if idx != -1:
            add_facet(
                idx,
                idx + len(paper_url),
                {"$type": "app.bsky.richtext.facet#link", "uri": paper_url},
            )

    for match in re.finditer(r"https?://\S+", text):
        add_facet(
            match.start(),
            match.end(),
            {"$type": "app.bsky.richtext.facet#link", "uri": match.group(0)},
        )

    for match in re.finditer(r"(?<!\w)#([A-Za-z0-9_]+)", text):
        tag = match.group(1)
        add_facet(
            match.start(),
            match.end(),
            {"$type": "app.bsky.richtext.facet#tag", "tag": tag},
        )

    if subscribe_url:
        label = SUBSCRIBE_LABEL
        idx = text.find(label)
        if idx != -1:
            add_facet(
                idx,
                idx + len(label),
                {"$type": "app.bsky.richtext.facet#link", "uri": subscribe_url},
            )

    return facets if facets else None

def post_to_twitter(text):
    load_env()
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret, access_token, access_token_secret]):
        print("Twitter credentials missing. Skipping.")
        return False

    if tweepy:
        try:
            client = tweepy.Client(
                consumer_key=api_key, consumer_secret=api_secret,
                access_token=access_token, access_token_secret=access_token_secret
            )
            response = client.create_tweet(text=text)
            print(f"Tweeted successfully: {response.data['id']}")
            return True
        except Exception as e:
            print(f"Error tweeting: {e}")
            return False
    else:
        print("Tweepy not installed. Cannot tweet.")
        return False

def post_to_bluesky(text, subscribe_url=None, paper_url=None, embed=None):
    load_env()
    handle = os.getenv("BLUESKY_HANDLE")
    password = os.getenv("BLUESKY_APP_PASSWORD") or os.getenv("BLUESKY_PASSWORD")
    service = os.getenv("BLUESKY_SERVICE", "https://bsky.social")

    if not handle or not password:
        print("Bluesky credentials missing. Skipping.")
        return False

    try:
        session_resp = requests.post(
            f"{service}/xrpc/com.atproto.server.createSession",
            json={"identifier": handle, "password": password},
            timeout=30,
        )
        if session_resp.status_code != 200:
            print(f"Bluesky login failed: {session_resp.status_code} - {session_resp.text}")
            return False
        session = session_resp.json()
        access = session.get("accessJwt")
        did = session.get("did")
        if not access or not did:
            print("Bluesky session missing fields.")
            return False

        record = {
            "repo": did,
            "collection": "app.bsky.feed.post",
            "record": {
                "text": text,
                "createdAt": datetime.utcnow().isoformat() + "Z",
            },
        }
        if embed:
            record["record"]["embed"] = embed
        facets = build_bluesky_facets(
            text, subscribe_url=subscribe_url, paper_url=paper_url
        )
        if facets:
            record["record"]["facets"] = facets
        post_resp = requests.post(
            f"{service}/xrpc/com.atproto.repo.createRecord",
            headers={"Authorization": f"Bearer {access}"},
            json=record,
            timeout=30,
        )
        if post_resp.status_code != 200:
            print(f"Bluesky post failed: {post_resp.status_code} - {post_resp.text}")
            return False
        print("Bluesky post successful.")
        return True
    except Exception as e:
        print(f"Error connecting to Bluesky API: {e}")
        return False

    if tweepy:
        try:
            client = tweepy.Client(
                consumer_key=api_key, consumer_secret=api_secret,
                access_token=access_token, access_token_secret=access_token_secret
            )
            response = client.create_tweet(text=text)
            print(f"Tweeted successfully: {response.data['id']}")
            return True
        except Exception as e:
            print(f"Error tweeting: {e}")
            return False
    else:
        print("Tweepy not installed. Cannot tweet.")
        return False

def post_to_linkedin(text, link):
    load_env()
    access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    linkedin_id = os.getenv("LINKEDIN_MEMBER_ID") # e.g., urn:li:person:abcdef
    org_id = os.getenv("LINKEDIN_ORG_ID")

    if not access_token or (not linkedin_id and not org_id):
        print("LinkedIn credentials/ID missing. Skipping.")
        return False

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    author = None
    if org_id:
        author = org_id
        if not author.startswith("urn:li:"):
            author = f"urn:li:organization:{org_id}"
    elif linkedin_id:
        author = linkedin_id
        if not author.startswith("urn:li:"):
            author = f"urn:li:person:{linkedin_id}"

    post_data = {
        "author": author,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "ARTICLE",
                "media": [
                    {
                        "status": "READY",
                        "description": {
                            "text": "Latest daily signal in protein design and structural biology."
                        },
                        "originalUrl": link,
                        "title": {
                            "text": "Protein Design Digest"
                        }
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    try:
        response = requests.post(url, headers=headers, json=post_data)
        if response.status_code == 201:
            print("LinkedIn post successful.")
            return True
        else:
            print(f"Error posting to LinkedIn: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Error connecting to LinkedIn API: {e}")
        return False

def post_to_whatsapp(text, link):
    load_env()
    phone = os.getenv("WHATSAPP_PHONE")
    api_key = os.getenv("WHATSAPP_API_KEY")

    if not phone or not api_key:
        print("WhatsApp (CallMeBot) credentials missing. Skipping notification.")
        return False

    # CallMeBot uses a simple GET request
    # URL format: https://api.callmebot.com/whatsapp.php?phone=[phone]&text=[text]&apikey=[apikey]
    message = f"{text}\n\nDirect Link: {link}\n\n(Forward this to your WhatsApp Status!)"
    url = "https://api.callmebot.com/whatsapp.php"
    params = {
        "phone": phone,
        "text": message,
        "apikey": api_key
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("WhatsApp notification sent successfully.")
            return True
        else:
            print(f"Error sending WhatsApp: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Error connecting to CallMeBot: {e}")
        return False

def build_twitter_text(signal_title, summary, signal_link, sub_url, issue_date=None):
    return build_social_text(
        signal_title,
        summary,
        signal_link,
        sub_url,
        TWITTER_LIMIT,
        include_tags=True,
        issue_date=issue_date,
        subscribe_url_in_text=True,
        extra_lines=None,
        url_length=23,
    )

def build_section_post(item, header_label, sub_url, issue_date):
    if not item:
        return None
    title = (item.get("title") or "").strip()
    if not title:
        return None
    summary_text = (item.get("abstract") or item.get("note") or "").strip()
    summary_text = shorten_text(summary_text, 140) if summary_text else ""
    if summary_text and is_redundant_summary(title, summary_text):
        summary_text = ""
    link = (item.get("link") or "").strip()
    return {
        "title": title,
        "summary": summary_text,
        "link": link,
        "twitter": build_social_text(
            title,
            summary_text,
            link,
            sub_url,
            TWITTER_LIMIT,
            include_tags=True,
            issue_date=issue_date,
            subscribe_url_in_text=True,
            extra_lines=None,
            header_label=header_label,
            url_length=23,
        ),
        "bluesky": build_social_text(
            title,
            summary_text,
            link,
            sub_url,
            BLUESKY_LIMIT,
            include_tags=True,
            issue_date=issue_date,
            subscribe_url_in_text=False,
            extra_lines=None,
            header_label=header_label,
            omit_long_links=True,
        ),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue-date", default="today")
    parser.add_argument("--issues-dir", default="issues")
    args = parser.parse_args()

    issue_date = args.issue_date
    if issue_date == "today":
        issue_date = datetime.now().strftime("%Y-%m-%d")

    issue = load_issue(issue_date, args.issues_dir)
    if not issue:
        return

    signal = issue.get("signal", {}) or {}
    signal_title = signal.get("title", "Protein Design Update")
    signal_link = signal.get("link", "")
    issue_number = issue.get("issue_number", "1")
    
    # Constructing a relative URL since we don't know the exact deployment path yet, 
    # but based on baseURL in hugo.yaml:
    base_url = DEFAULT_BASE_URL
    issue_url = f"{base_url}{issue_date}-issue-{issue_number}/"
    sub_url = base_url

    summary = (signal or {}).get("summary", "")
    summary = (summary or "").strip()
    if len(summary) > 140:
        summary = summary[:137].rstrip() + "..."

    ai_items = coerce_list(issue.get("ai_news"))
    industry_items = coerce_list(issue.get("industry_news"))
    job_items = coerce_list((issue.get("community") or {}).get("job"))
    social_cfg = issue.get("social", {}) or {}
    ai_cfg = social_cfg.get("ai") or {}
    industry_cfg = social_cfg.get("industry") or {}
    job_cfg = social_cfg.get("job") or {}
    ai_enabled = ai_cfg.get("enabled", True)
    industry_enabled = industry_cfg.get("enabled", True)
    job_enabled = job_cfg.get("enabled", True)

    extras = []
    if ai_items and not ai_enabled:
        ai_title = (ai_items[0] or {}).get("title", "")
        if ai_title:
            extras.append(f"AI: {ai_title}")
    if industry_items and not industry_enabled:
        ind_title = (industry_items[0] or {}).get("title", "")
        if ind_title:
            extras.append(f"Industry: {ind_title}")
    if job_items and not job_enabled:
        job_title = (job_items[0] or {}).get("title", "")
        job_org = (job_items[0] or {}).get("org", "")
        if job_title:
            if job_org:
                extras.append(f"Job: {job_title} ({job_org})")
            else:
                extras.append(f"Job: {job_title}")

    social_twitter = (social_cfg.get("twitter") or "").strip()
    social_bluesky = (social_cfg.get("bluesky") or "").strip()
    tweet_text = social_twitter or build_twitter_text(
        signal_title, summary, signal_link, sub_url, issue_date
    )

    social_linkedin = (social_cfg.get("linkedin") or "").strip()
    li_text = social_linkedin or build_social_text(
        signal_title,
        summary,
        signal_link,
        sub_url,
        BLUESKY_LIMIT,
        include_tags=False,
        issue_date=issue_date,
        subscribe_url_in_text=False,
        extra_lines=extras,
    )

    wa_text = (
        f"🧬 *Protein Design Digest LIVE!*\n\n"
        f"Today's Signal: {signal_title}\n"
        f"🔗 *Read Today:* {issue_url}\n"
        f"✍️ *Subscribe:* {sub_url}\n\n"
        f"_(Forward this message to your WhatsApp Status!)_"
    )
    bluesky_text = social_bluesky or build_social_text(
        signal_title,
        summary,
        signal_link,
        sub_url,
        BLUESKY_LIMIT,
        include_tags=True,
        issue_date=issue_date,
        subscribe_url_in_text=False,
        extra_lines=extras,
        omit_long_links=True,
    )

    ai_post = (
        build_section_post(ai_items[0] if ai_items else None, "AI news of the day", sub_url, issue_date)
        if ai_enabled
        else None
    )
    industry_post = (
        build_section_post(
            industry_items[0] if industry_items else None, "Industry news of the day", sub_url, issue_date
        )
        if industry_enabled
        else None
    )
    job_post = None
    if job_items and job_enabled:
        job_item = job_items[0] or {}
        job_title = (job_item.get("title") or "").strip()
        job_org = (job_item.get("org") or "").strip()
        if job_title:
            if job_org:
                job_title = f"{job_title} ({job_org})"
            job_item = dict(job_item)
            job_item["title"] = job_title
            job_post = build_section_post(job_item, "Job of the day", sub_url, issue_date)

    def apply_social_override(post, text, header_label, channel):
        if not text:
            return post
        if post is None:
            post = {
                "title": extract_title_line(text, header_label),
                "summary": "",
                "link": extract_first_url(text),
                "twitter": "",
                "bluesky": "",
            }
        if not post.get("link"):
            post["link"] = extract_first_url(text)
        if not post.get("title"):
            post["title"] = extract_title_line(text, header_label)
        post[channel] = text
        return post

    ai_post = apply_social_override(
        ai_post, (ai_cfg.get("twitter") or "").strip(), "AI news of the day", "twitter"
    )
    ai_post = apply_social_override(
        ai_post, (ai_cfg.get("bluesky") or "").strip(), "AI news of the day", "bluesky"
    )
    industry_post = apply_social_override(
        industry_post,
        (industry_cfg.get("twitter") or "").strip(),
        "Industry news of the day",
        "twitter",
    )
    industry_post = apply_social_override(
        industry_post,
        (industry_cfg.get("bluesky") or "").strip(),
        "Industry news of the day",
        "bluesky",
    )
    job_post = apply_social_override(
        job_post, (job_cfg.get("twitter") or "").strip(), "Job of the day", "twitter"
    )
    job_post = apply_social_override(
        job_post, (job_cfg.get("bluesky") or "").strip(), "Job of the day", "bluesky"
    )

    def ensure_channel(post, header_label):
        if not post:
            return post
        title = post.get("title") or header_label
        summary_text = post.get("summary") or ""
        link = post.get("link") or ""
        if not post.get("twitter"):
            post["twitter"] = build_social_text(
                title,
                summary_text,
                link,
                sub_url,
                TWITTER_LIMIT,
                include_tags=True,
                issue_date=issue_date,
                subscribe_url_in_text=True,
                extra_lines=None,
                header_label=header_label,
                url_length=23,
            )
        if not post.get("bluesky"):
            post["bluesky"] = build_social_text(
                title,
                summary_text,
                link,
                sub_url,
                BLUESKY_LIMIT,
                include_tags=True,
                issue_date=issue_date,
                subscribe_url_in_text=False,
                extra_lines=None,
                header_label=header_label,
                omit_long_links=True,
            )
        return post

    ai_post = ensure_channel(ai_post, "AI news of the day")
    industry_post = ensure_channel(industry_post, "Industry news of the day")
    job_post = ensure_channel(job_post, "Job of the day")

    print(f"Publishing Social for {issue_date}...")
    post_to_twitter(tweet_text)
    for post in (ai_post, industry_post, job_post):
        if post:
            post_to_twitter(post["twitter"])
    post_to_linkedin(li_text, issue_url)
    post_to_whatsapp(wa_text, issue_url)
    bs_subscribe = os.getenv("BLUESKY_SUBSCRIBE_URL", DEFAULT_BASE_URL)
    bluesky_text = ensure_subscribe_label(bluesky_text, BLUESKY_LIMIT)
    main_link = signal_link or extract_first_url(tweet_text) or extract_first_url(bluesky_text)
    main_title = signal_title or extract_title_line(tweet_text or bluesky_text, pick_human_opener())
    embed = build_external_embed(main_title, summary, main_link)
    post_to_bluesky(
        bluesky_text,
        subscribe_url=bs_subscribe,
        paper_url=main_link,
        embed=embed,
    )
    for post in (ai_post, industry_post, job_post):
        if not post:
            continue
        post["bluesky"] = ensure_subscribe_label(post["bluesky"], BLUESKY_LIMIT)
        embed = build_external_embed(post["title"], post.get("summary", ""), post.get("link", ""))
        post_to_bluesky(
            post["bluesky"],
            subscribe_url=bs_subscribe,
            paper_url=post.get("link", ""),
            embed=embed,
        )

if __name__ == "__main__":
    main()
