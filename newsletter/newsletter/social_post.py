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

SOCIAL_TAGS = ["#ProteinDesign", "#StructuralBiology", "#Bioinformatics"]
TWITTER_LIMIT = 280
BLUESKY_LIMIT = 300
DEFAULT_BASE_URL = "https://recep2244.github.io/portfolio/newsletter/"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def shorten_text(text, max_len):
    if max_len <= 0:
        return ""
    if len(text) <= max_len:
        return text
    if max_len <= 3:
        return text[:max_len]
    return text[: max_len - 3].rstrip() + "..."


def build_social_text(
    title, summary, signal_link, sub_url, limit, include_tags=True
):
    header = "Paper of the day"
    title = title or "Daily signal"
    tags_line = " ".join(SOCIAL_TAGS) if include_tags else ""

    tail_lines = []
    if signal_link:
        tail_lines.append(f"{signal_link}")
    tail_lines.append(f"Subscribe to the newsletter: {sub_url}")

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


def post_twitter(content, api_key, api_secret, access_token, access_token_secret):
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


def post_bluesky(content, handle, password, service):
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
        facets = build_bluesky_facets(content)
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

    if not signal_title:
        print("No signal content to post.")
        sys.exit(0)

    base_url = DEFAULT_BASE_URL
    sub_url = base_url

    twitter_text = build_social_text(
        signal_title,
        summary,
        signal_link,
        sub_url,
        TWITTER_LIMIT,
        include_tags=True,
    )
    bluesky_text = build_social_text(
        signal_title,
        summary,
        signal_link,
        sub_url,
        BLUESKY_LIMIT,
        include_tags=True,
    )

    print("--- Twitter Post ---")
    print(twitter_text)
    print("--------------------")
    print("--- Bluesky Post ---")
    print(bluesky_text)
    print("--------------------")

    # Twitter
    tw_key = os.getenv("TWITTER_API_KEY")
    tw_sec = os.getenv("TWITTER_API_SECRET")
    tw_tok = os.getenv("TWITTER_ACCESS_TOKEN")
    tw_tok_sec = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    if tw_key and tw_sec and tw_tok and tw_tok_sec:
        post_twitter(twitter_text, tw_key, tw_sec, tw_tok, tw_tok_sec)
    else:
        print("Skipping Twitter (credentials missing)")

    # LinkedIn
    li_tok = os.getenv("LINKEDIN_ACCESS_TOKEN")
    if li_tok:
        post_linkedin(twitter_text, li_tok)
    else:
        print("Skipping LinkedIn (credentials missing)")

    # Bluesky
    bs_handle = os.getenv("BLUESKY_HANDLE")
    bs_pass = os.getenv("BLUESKY_APP_PASSWORD") or os.getenv("BLUESKY_PASSWORD")
    bs_service = os.getenv("BLUESKY_SERVICE", "https://bsky.social")
    if bs_handle and bs_pass:
        post_bluesky(bluesky_text, bs_handle, bs_pass, bs_service)
    else:
        print("Skipping Bluesky (credentials missing)")


if __name__ == "__main__":
    main()
