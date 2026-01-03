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
    # Twitter limit ~280. Bluesky ~300.
    limit = 140
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

    # 2. Post to Company Page (Protein Design Daily - ID: 110446267)
    ORG_ID = "110446267"
    try:
        org_urn = f"urn:li:organization:{ORG_ID}"
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
    if li_tok:
        post_linkedin(post_content, li_tok)
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
