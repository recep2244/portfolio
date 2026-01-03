import os
import json
import re
import requests
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Optional: Using tweepy for Twitter if available, otherwise we can use direct requests
try:
    import tweepy
except ImportError:
    tweepy = None

SOCIAL_TAGS = ["#ProteinDesign", "#StructuralBiology", "#Bioinformatics"]
TWITTER_LIMIT = 280
BLUESKY_LIMIT = 300
DEFAULT_BASE_URL = "https://recep2244.github.io/portfolio/newsletter/"

def load_issue(issue_date, issues_dir):
    filename = f"{issue_date}.json"
    filepath = os.path.join(issues_dir, filename)
    if not os.path.exists(filepath):
        print(f"Issue file not found: {filepath}")
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

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


def build_social_text(
    title, summary, signal_link, sub_url, limit, issue_date=None, include_tags=True
):
    header = "Paper of the day"
    if issue_date:
        header = f"{header} · {issue_date}"
    header = f"{header} · Recep Adiyaman"
    title = title or "Daily signal"
    tags_line = " ".join(SOCIAL_TAGS) if include_tags else ""

    tail_lines = []
    if signal_link:
        tail_lines.append(f"{signal_link}")
    tail_lines.append(f"Subscribe: {sub_url}")

    def assemble(title_line, summary_line=None):
        lines = [header]
        if title_line:
            lines.append(title_line)
        if summary_line:
            lines.append(summary_line)
        lines += tail_lines
        if tags_line:
            lines.append(tags_line)
        return "\n".join(lines)

    base_without_title = assemble("", None)
    allowed = max(0, limit - len(base_without_title) - 1)
    title_line = shorten_text(title, allowed)
    if not title_line:
        title_line = "Signal"
    base_text = assemble(title_line, None)

    if summary:
        remaining = limit - len(base_text) - 1
        if remaining > 0:
            summary_text = shorten_text(summary, remaining)
            base_text = assemble(title_line, summary_text)

    if len(base_text) > limit:
        base_text = assemble(title_line, None)

    return base_text


def build_bluesky_facets(text):
    facets = []

    def add_facet(start, end, feature):
        facets.append(
            {
                "index": {
                    "byteStart": len(text[:start].encode("utf-8")),
                    "byteEnd": len(text[:end].encode("utf-8")),
                },
                "features": [feature],
            }
        )

    for match in re.finditer(r"https?://\\S+", text):
        add_facet(
            match.start(),
            match.end(),
            {"$type": "app.bsky.richtext.facet#link", "uri": match.group(0)},
        )

    for match in re.finditer(r"(?<!\\w)#([A-Za-z0-9_]+)", text):
        tag = match.group(1)
        add_facet(
            match.start(),
            match.end(),
            {"$type": "app.bsky.richtext.facet#tag", "tag": tag},
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

def post_to_bluesky(text):
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
        facets = build_bluesky_facets(text)
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
        issue_date,
        include_tags=True,
    )

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

    tweet_text = build_twitter_text(
        signal_title, summary, signal_link, sub_url, issue_date
    )

    li_text = build_social_text(
        signal_title,
        summary,
        signal_link,
        sub_url,
        BLUESKY_LIMIT,
        issue_date,
        include_tags=False,
    )

    wa_text = (
        f"🧬 *Protein Design Digest LIVE!*\n\n"
        f"Today's Signal: {signal_title}\n"
        f"🔗 *Read Today:* {issue_url}\n"
        f"✍️ *Subscribe:* {sub_url}\n\n"
        f"_(Forward this message to your WhatsApp Status!)_"
    )
    bluesky_text = build_social_text(
        signal_title,
        summary,
        signal_link,
        sub_url,
        BLUESKY_LIMIT,
        issue_date,
        include_tags=True,
    )

    print(f"Publishing Social for {issue_date}...")
    post_to_twitter(tweet_text)
    post_to_linkedin(li_text, issue_url)
    post_to_whatsapp(wa_text, issue_url)
    post_to_bluesky(bluesky_text)

if __name__ == "__main__":
    main()
