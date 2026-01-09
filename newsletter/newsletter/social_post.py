#!/usr/bin/env python3
import argparse
import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Load .env file if present (for local development)
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass  # dotenv not installed, will use system env vars

# Try importing libraries, but don't crash if missing (flow might be different)
try:
    import tweepy
except ImportError:
    tweepy = None

try:
    import requests
except ImportError:
    requests = None

SOCIAL_TAGS = ["#ProteinDesign", "#StructuralBiology", "#Bioinformatics", "#ProteinEngineering"]
SUBSCRIBE_LABEL = "Subnewsletter"
TWITTER_LIMIT = 280
BLUESKY_LIMIT = 300
DEFAULT_BASE_URL = "https://recep2244.github.io/portfolio/subscribe-form.html"
DEFAULT_TWITTER_TEMPLATE = "{header}\n{title}\n{extras}\n{summary}\n{subscribe}\n{link}\n{tags}"
DEFAULT_BLUESKY_TEMPLATE = "{header}\n{title}\n{extras}\n{summary}\n{link}\n{subscribe}\n{tags}"
DEFAULT_SECTION_TEMPLATE = "{header}\n{title}\n{summary}\n{link}\n{subscribe}\n{tags}"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def coerce_list(value):
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return [value]
    return []


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


def ensure_subscribe_label(text, limit, subscribe_label=SUBSCRIBE_LABEL):
    if not text:
        return text
    if subscribe_label in text:
        return text
    line = f"\n{subscribe_label}"
    if len(text) + len(line) <= limit:
        return text + line
    lines = text.splitlines()
    if lines and lines[-1].startswith("#"):
        lines.pop()
        text = "\n".join(lines)
        if subscribe_label in text:
            return text
        if len(text) + len(line) <= limit:
            return text + line
    return text


class SafeFormatDict(dict):
    def __missing__(self, key):
        return ""


def render_template(template, values):
    text = template.format_map(SafeFormatDict(values))
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def load_template(env_key, fallback):
    value = (os.getenv(env_key) or "").strip()
    return value or fallback


def get_subscribe_label(channel):
    override = os.getenv(f"{channel.upper()}_SUBSCRIBE_LABEL") or os.getenv(
        "SOCIAL_SUBSCRIBE_LABEL"
    )
    override = (override or "").strip()
    return override or SUBSCRIBE_LABEL


def is_truthy(value, default=False):
    if value is None or value == "":
        return default
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


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
    safe_title = shorten_text(title or "Paper of the day", 120)
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
    template=None,
    subscribe_label=SUBSCRIBE_LABEL,
):
    def measure_text(text):
        if not url_length:
            return len(text)
        return len(re.sub(r"https?://\S+", "x" * url_length, text))

    header = header_label or "Paper of the day"
    formatted_date = format_issue_date(issue_date)
    if formatted_date:
        header = f"{header} · {formatted_date}"
    title = title or "Daily signal"
    tags_line = " ".join(SOCIAL_TAGS) if include_tags else ""

    tail_lines = []
    subscribe_line = (
        f"{subscribe_label} {sub_url}" if subscribe_url_in_text else subscribe_label
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

    if template:
        return build_social_text_from_template(
            template,
            header,
            title,
            summary,
            extra_lines or [],
            subscribe_line,
            signal_link,
            tags_line,
            limit,
            url_length,
            omit_long_links,
        )

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
                template=template,
                subscribe_label=subscribe_label,
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
            template=template,
            subscribe_label=subscribe_label,
            omit_long_links=False,
        )
    return final_text


def build_social_text_from_template(
    template,
    header,
    title,
    summary,
    extra_lines,
    subscribe_line,
    signal_link,
    tags_line,
    limit,
    url_length,
    omit_long_links,
):
    def measure_text(text):
        if not url_length:
            return len(text)
        return len(re.sub(r"https?://\S+", "x" * url_length, text))

    extras_text = "\n".join([line for line in extra_lines if line])
    values = {
        "header": header,
        "title": title,
        "summary": summary or "",
        "extras": extras_text,
        "subscribe": subscribe_line,
        "link": signal_link or "",
        "tags": tags_line or "",
    }

    def render(values_map):
        return render_template(template, values_map)

    def fit_field(values_map, field):
        base_values = dict(values_map)
        base_values[field] = ""
        base_text = render(base_values)
        remaining = limit - measure_text(base_text)
        if remaining <= 0:
            return ""
        return shorten_text(values_map.get(field, ""), remaining)

    text = render(values)
    if measure_text(text) <= limit:
        return text

    if values.get("summary"):
        values["summary"] = fit_field(values, "summary")
        text = render(values)
        if measure_text(text) <= limit:
            return text

    if values.get("extras"):
        values["extras"] = fit_field(values, "extras")
        text = render(values)
        if measure_text(text) <= limit:
            return text

    if values.get("tags"):
        values["tags"] = ""
        text = render(values)
        if measure_text(text) <= limit:
            return text

    if values.get("title"):
        values["title"] = fit_field(values, "title") or "Signal"
        text = render(values)
        if measure_text(text) <= limit:
            return text

    if omit_long_links and values.get("link"):
        values["link"] = ""
        text = render(values)
        if measure_text(text) <= limit:
            return text

    return render(values)


def format_duplicate_suffix(issue_date):
    template = (os.getenv("TWITTER_DUPLICATE_SUFFIX") or "").strip()
    if template:
        return template.format(issue_date=issue_date or "").strip()
    return f"upd {datetime.now().strftime('%H%M')}"


def append_suffix(text, suffix, limit=TWITTER_LIMIT):
    suffix = (suffix or "").strip()
    if not suffix:
        return text
    if suffix in text:
        return text
    if len(text) + len(suffix) + 1 <= limit:
        return f"{text} {suffix}"
    trimmed = text[: max(0, limit - len(suffix) - 1)].rstrip()
    if not trimmed:
        return text[:limit]
    return f"{trimmed} {suffix}"


def post_twitter(content, api_key, api_secret, access_token, access_token_secret, issue_date=None):
    if not tweepy:
        print("Tweepy not installed, skipping Twitter.")
        return

    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        response = client.create_tweet(text=content)
        print(f"Posted to Twitter: {response.data['id']}")
    except Exception as e:
        msg = str(e).lower()
        if "duplicate" in msg or "403" in msg:
            suffix = format_duplicate_suffix(issue_date)
            retry_text = append_suffix(content, suffix, TWITTER_LIMIT)
            if retry_text != content:
                try:
                    response = client.create_tweet(text=retry_text)
                    print(f"Posted to Twitter (retry): {response.data['id']}")
                    return
                except Exception as retry_err:
                    print(f"Failed to post to Twitter (retry): {retry_err}")
                    return
        print(f"Failed to post to Twitter: {e}")


def post_linkedin(content, access_token):
    if not requests:
        print("Requests not installed, skipping LinkedIn.")
        return

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    # 1. Post to Personal Profile
    person_urn = None
    try:
        # Fetch current user's URN
        # Try /me first (legacy/r_liteprofile)
        profile_res = requests.get("https://api.linkedin.com/v2/me", headers=headers)
        if profile_res.status_code == 200:
            person_urn = f"urn:li:person:{profile_res.json()['id']}"
        else:
            # Try OIDC userinfo (openid/profile)
            oidc_headers = {"Authorization": f"Bearer {access_token}"}
            userinfo_res = requests.get("https://api.linkedin.com/v2/userinfo", headers=oidc_headers)
            if userinfo_res.status_code == 200:
                person_urn = f"urn:li:person:{userinfo_res.json()['sub']}"
            else:
                print(f"⚠️ Failed to fetch LinkedIn Profile dynamically (/me: {profile_res.status_code}, /userinfo: {userinfo_res.status_code})")
                # Fallback to known Member ID if available
                KNOWN_MEMBER_ID = "780710122"
                print(f"⚡ Using known fallback Member ID: {KNOWN_MEMBER_ID}")
                person_urn = f"urn:li:member:{KNOWN_MEMBER_ID}"

        if person_urn:
            payload_person = {
                "author": person_urn,
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": content},
                        "shareMediaCategory": "NONE"
                    }
                },
                "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
            }
            
            resp = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=payload_person)
            if resp.status_code in [200, 201]:
                print(f"✅ Posted to LinkedIn Profile ({person_urn})")
            else:
                print(f"❌ Failed to post to LinkedIn Profile: {resp.text}")

    except Exception as e:
        print(f"❌ LinkedIn Profile Error: {e}")

    org_id = os.getenv("LINKEDIN_ORG_ID")
    if not org_id:
        return
    try:
        org_urn = org_id
        if not org_urn.startswith("urn:li:"):
            org_urn = f"urn:li:organization:{org_id}"
        payload_org = {
            "author": org_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": content},
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
        }

        resp_org = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=payload_org)
        if resp_org.status_code in [200, 201]:
            print(f"✅ Posted to LinkedIn Company Page ({org_urn})")
        else:
            # This often fails if the token lacks 'w_organization_social'
            # We print a helpful message but don't crash.
            print(f"⚠️  Could not post to Company Page (might need 'w_organization_social' scope): {resp_org.status_code}")
            # print(resp_org.text) # Uncomment for debug
            
    except Exception as e:
        print(f"❌ LinkedIn Company Page Error: {e}")


def build_bluesky_facets(
    text, subscribe_url=None, paper_url=None, subscribe_label=SUBSCRIBE_LABEL
):
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
        label = subscribe_label
        idx = text.find(label)
        if idx != -1:
            add_facet(
                idx,
                idx + len(label),
                {"$type": "app.bsky.richtext.facet#link", "uri": subscribe_url},
            )

    return facets if facets else None


def post_bluesky(
    content,
    handle,
    password,
    service,
    subscribe_url=None,
    paper_url=None,
    embed=None,
    subscribe_label=SUBSCRIBE_LABEL,
):
    if not requests:
        print("Requests not installed, skipping Bluesky.")
        return
    try:
        session_resp = requests.post(
            f"{service}/xrpc/com.atproto.server.createSession",
            json={"identifier": handle, "password": password},
            timeout=30,
        )
        if session_resp.status_code != 200:
            print(f"Bluesky login failed: {session_resp.status_code} - {session_resp.text}")
            return
        session = session_resp.json()
        access = session.get("accessJwt")
        did = session.get("did")
        if not access or not did:
            print("Bluesky session missing fields.")
            return

        record = {
            "repo": did,
            "collection": "app.bsky.feed.post",
            "record": {
                "text": content,
                "createdAt": datetime.utcnow().isoformat() + "Z",
            },
        }
        if embed:
            record["record"]["embed"] = embed
        facets = build_bluesky_facets(
            content,
            subscribe_url=subscribe_url,
            paper_url=paper_url,
            subscribe_label=subscribe_label,
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
            return
        print("Posted to Bluesky")
    except Exception as e:
        print(f"Failed to post to Bluesky: {e}")


def main():
    parser = argparse.ArgumentParser(description="Post daily signal to social media")
    parser.add_argument("--issue", required=True, help="Path to issue JSON")
    args = parser.parse_args()

    if not os.path.exists(args.issue):
        print(f"Issue file not found: {args.issue}")
        sys.exit(1)

    issue = load_json(args.issue)
    signal = issue.get("signal", {})
    signal_title = (signal or {}).get("title", "")
    signal_link = (signal or {}).get("link", "")
    summary = (signal or {}).get("summary", "")
    summary = (summary or "").strip()
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

    if not signal_title:
        print("No signal content to post.")
        sys.exit(0)

    twitter_subscribe_url = os.getenv("TWITTER_SUBSCRIBE_URL", DEFAULT_BASE_URL)
    bluesky_subscribe_url = os.getenv("BLUESKY_SUBSCRIBE_URL", DEFAULT_BASE_URL)
    twitter_template = load_template("TWITTER_TEMPLATE", DEFAULT_TWITTER_TEMPLATE)
    bluesky_template = load_template("BLUESKY_TEMPLATE", DEFAULT_BLUESKY_TEMPLATE)
    twitter_section_template = load_template(
        "TWITTER_SECTION_TEMPLATE", DEFAULT_SECTION_TEMPLATE
    )
    bluesky_section_template = load_template(
        "BLUESKY_SECTION_TEMPLATE", DEFAULT_SECTION_TEMPLATE
    )
    twitter_subscribe_label = get_subscribe_label("twitter")
    bluesky_subscribe_label = get_subscribe_label("bluesky")
    twitter_subscribe_in_text = is_truthy(
        os.getenv("TWITTER_SUBSCRIBE_URL_IN_TEXT"), default=True
    )
    bluesky_subscribe_in_text = is_truthy(
        os.getenv("BLUESKY_SUBSCRIBE_URL_IN_TEXT"), default=False
    )

    issue_date = issue.get("issue_date", "")
    social_twitter = (social_cfg.get("twitter") or "").strip()
    social_bluesky = (social_cfg.get("bluesky") or "").strip()
    twitter_text = social_twitter or build_social_text(
        signal_title,
        summary,
        signal_link,
        twitter_subscribe_url,
        TWITTER_LIMIT,
        include_tags=True,
        issue_date=issue_date,
        subscribe_url_in_text=twitter_subscribe_in_text,
        extra_lines=extras,
        url_length=23,
        template=twitter_template,
        subscribe_label=twitter_subscribe_label,
    )
    bluesky_text = social_bluesky or build_social_text(
        signal_title,
        summary,
        signal_link,
        bluesky_subscribe_url,
        BLUESKY_LIMIT,
        include_tags=True,
        issue_date=issue_date,
        subscribe_url_in_text=bluesky_subscribe_in_text,
        extra_lines=extras,
        omit_long_links=True,
        template=bluesky_template,
        subscribe_label=bluesky_subscribe_label,
    )

    def build_section_post(item, header_label):
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
                twitter_subscribe_url,
                TWITTER_LIMIT,
                include_tags=True,
                issue_date=issue_date,
                subscribe_url_in_text=twitter_subscribe_in_text,
                extra_lines=None,
                header_label=header_label,
                url_length=23,
                template=twitter_section_template,
                subscribe_label=twitter_subscribe_label,
            ),
            "bluesky": build_social_text(
                title,
                summary_text,
                link,
                bluesky_subscribe_url,
                BLUESKY_LIMIT,
                include_tags=True,
                issue_date=issue_date,
                subscribe_url_in_text=bluesky_subscribe_in_text,
                extra_lines=None,
                header_label=header_label,
                omit_long_links=True,
                template=bluesky_section_template,
                subscribe_label=bluesky_subscribe_label,
            ),
        }

    ai_post = (
        build_section_post(ai_items[0] if ai_items else None, "AI news of the day")
        if ai_enabled
        else None
    )
    industry_post = (
        build_section_post(industry_items[0] if industry_items else None, "Industry news of the day")
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
            job_post = build_section_post(job_item, "Job of the day")

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
                subscribe_url_in_text=twitter_subscribe_in_text,
                extra_lines=None,
                header_label=header_label,
                url_length=23,
                template=twitter_section_template,
                subscribe_label=twitter_subscribe_label,
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
                subscribe_url_in_text=bluesky_subscribe_in_text,
                extra_lines=None,
                header_label=header_label,
                omit_long_links=True,
                template=bluesky_section_template,
                subscribe_label=bluesky_subscribe_label,
            )
        return post

    ai_post = ensure_channel(ai_post, "AI news of the day")
    industry_post = ensure_channel(industry_post, "Industry news of the day")
    job_post = ensure_channel(job_post, "Job of the day")

    print("--- Twitter Post ---")
    print(twitter_text)
    print("--------------------")
    print("--- Bluesky Post ---")
    print(bluesky_text)
    print("--------------------")
    if ai_post:
        print("--- AI News Post (Twitter) ---")
        print(ai_post["twitter"])
        print("------------------------------")
        print("--- AI News Post (Bluesky) ---")
        print(ai_post["bluesky"])
        print("------------------------------")
    if industry_post:
        print("--- Industry News Post (Twitter) ---")
        print(industry_post["twitter"])
        print("------------------------------------")
        print("--- Industry News Post (Bluesky) ---")
        print(industry_post["bluesky"])
        print("------------------------------------")
    if job_post:
        print("--- Job Post (Twitter) ---")
        print(job_post["twitter"])
        print("--------------------------")
        print("--- Job Post (Bluesky) ---")
        print(job_post["bluesky"])
        print("--------------------------")

    channels_env = (os.getenv("SOCIAL_CHANNELS") or "").strip().lower()
    if channels_env:
        channels = {c.strip() for c in channels_env.split(",") if c.strip()}
    else:
        channels = {"twitter", "linkedin", "bluesky"}

    # Twitter
    tw_key = os.getenv("TWITTER_API_KEY")
    tw_sec = os.getenv("TWITTER_API_SECRET")
    tw_tok = os.getenv("TWITTER_ACCESS_TOKEN")
    tw_tok_sec = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    if "twitter" in channels and tw_key and tw_sec and tw_tok and tw_tok_sec:
        post_twitter(twitter_text, tw_key, tw_sec, tw_tok, tw_tok_sec, issue_date)
        if ai_post:
            post_twitter(ai_post["twitter"], tw_key, tw_sec, tw_tok, tw_tok_sec, issue_date)
        if industry_post:
            post_twitter(industry_post["twitter"], tw_key, tw_sec, tw_tok, tw_tok_sec, issue_date)
        if job_post:
            post_twitter(job_post["twitter"], tw_key, tw_sec, tw_tok, tw_tok_sec, issue_date)
    elif "twitter" in channels:
        print("Skipping Twitter (credentials missing)")

    # LinkedIn
    li_tok = os.getenv("LINKEDIN_ACCESS_TOKEN")
    if "linkedin" in channels and li_tok:
        li_text = (social_cfg.get("linkedin") or "").strip() or twitter_text
        post_linkedin(li_text, li_tok)
    elif "linkedin" in channels:
        print("Skipping LinkedIn (credentials missing)")

    # Bluesky
    bs_handle = os.getenv("BLUESKY_HANDLE")
    bs_pass = os.getenv("BLUESKY_APP_PASSWORD") or os.getenv("BLUESKY_PASSWORD")
    bs_service = os.getenv("BLUESKY_SERVICE", "https://bsky.social")
    bs_subscribe = bluesky_subscribe_url
    if "bluesky" in channels and bs_handle and bs_pass:
        bluesky_text = ensure_subscribe_label(
            bluesky_text, BLUESKY_LIMIT, subscribe_label=bluesky_subscribe_label
        )
        main_link = signal_link or extract_first_url(twitter_text) or extract_first_url(bluesky_text)
        main_title = signal_title or extract_title_line(twitter_text or bluesky_text, "Paper of the day")
        embed = build_external_embed(main_title, summary, main_link)
        post_bluesky(
            bluesky_text,
            bs_handle,
            bs_pass,
            bs_service,
            subscribe_url=bs_subscribe,
            paper_url=main_link,
            embed=embed,
            subscribe_label=bluesky_subscribe_label,
        )
        for post in (ai_post, industry_post, job_post):
            if not post:
                continue
            post["bluesky"] = ensure_subscribe_label(
                post["bluesky"], BLUESKY_LIMIT, subscribe_label=bluesky_subscribe_label
            )
            embed = build_external_embed(post["title"], post.get("summary", ""), post.get("link", ""))
            post_bluesky(
                post["bluesky"],
                bs_handle,
                bs_pass,
                bs_service,
                subscribe_url=bs_subscribe,
                paper_url=post.get("link", ""),
                embed=embed,
                subscribe_label=bluesky_subscribe_label,
            )
    elif "bluesky" in channels:
        print("Skipping Bluesky (credentials missing)")


if __name__ == "__main__":
    main()
