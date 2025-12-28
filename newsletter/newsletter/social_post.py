#!/usr/bin/env python3
import argparse
import json
import os
import sys
import textwrap

# Try importing libraries, but don't crash if missing (flow might be different)
try:
    import tweepy
except ImportError:
    tweepy = None

try:
    import requests
except ImportError:
    requests = None

try:
    from atproto import Client
except ImportError:
    Client = None


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def format_post(issue):
    signal = issue.get("signal", {})
    title = signal.get("title", "")
    link = signal.get("link", "")
    # Use summary or "why it matters"
    summary = signal.get("summary", "")
    
    if not title or not link:
        return None

    # Construct concise post
    post = f"⚡ Daily Signal: {title}\n\n"
    
    # Truncate summary to fit roughly in a tweet (leaving room for link/hashtags)
    # Twitter limit ~280. Link takes ~23. Hashtags ~30. 
    # Available for text ~220.
    limit = 200
    if len(summary) > limit:
        summary = textwrap.shorten(summary, width=limit, placeholder="...")
    
    post += f"{summary}\n\n"
    post += f"🔗 {link}\n\n"
    post += "#ProteinDesign #Bioinformatics #StructurePrediction"
    
    return post


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


def post_linkedin(content, access_token, member_id):
    if not requests:
        print("Requests not installed, skipping LinkedIn.")
        return

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    payload = {
        "author": f"urn:li:person:{member_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    try:
        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        print("Posted to LinkedIn")
    except Exception as e:
        print(f"Failed to post to LinkedIn: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response: {e.response.text}")


def post_bluesky(content, handle, password):
    if not Client:
        print("atproto not installed, skipping Bluesky.")
        return

    try:
        client = Client()
        client.login(handle, password)
        client.send_post(text=content)
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
    post_content = format_post(issue)
    
    if not post_content:
        print("No signal content to post.")
        sys.exit(0)

    print("--- Post Content ---")
    print(post_content)
    print("--------------------")

    # Twitter
    tw_key = os.getenv("TWITTER_API_KEY")
    tw_sec = os.getenv("TWITTER_API_SECRET")
    tw_tok = os.getenv("TWITTER_ACCESS_TOKEN")
    tw_tok_sec = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    if tw_key and tw_sec and tw_tok and tw_tok_sec:
        post_twitter(post_content, tw_key, tw_sec, tw_tok, tw_tok_sec)
    else:
        print("Skipping Twitter (credentials missing)")

    # LinkedIn
    li_tok = os.getenv("LINKEDIN_ACCESS_TOKEN")
    li_id = os.getenv("LINKEDIN_MEMBER_ID")
    if li_tok and li_id:
        post_linkedin(post_content, li_tok, li_id)
    else:
        print("Skipping LinkedIn (credentials missing)")

    # Bluesky
    bs_handle = os.getenv("BLUESKY_HANDLE")
    bs_pass = os.getenv("BLUESKY_PASSWORD")
    if bs_handle and bs_pass:
        post_bluesky(post_content, bs_handle, bs_pass)
    else:
        print("Skipping Bluesky (credentials missing)")


if __name__ == "__main__":
    main()
