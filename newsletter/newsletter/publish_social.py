import os
import json
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

def post_to_twitter(text, link):
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
            response = client.create_tweet(text=f"{text}\n\nRead more: {link}")
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
    password = os.getenv("BLUESKY_APP_PASSWORD")
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
            response = client.create_tweet(text=f"{text}\n\nRead more: {link}")
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

    if not access_token or not linkedin_id:
        print("LinkedIn credentials/ID missing. Skipping.")
        return False

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    post_data = {
        "author": linkedin_id,
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

    signal_title = issue.get("signal", {}).get("title", "Protein Design Update")
    issue_number = issue.get("issue_number", "1")
    
    # Constructing a relative URL since we don't know the exact deployment path yet, 
    # but based on baseURL in hugo.yaml:
    base_url = "https://recep2244.github.io/portfolio/newsletter/"
    issue_url = f"{base_url}{issue_date}-issue-{issue_number}/"
    sub_url = base_url

    social = issue.get("social", {}) if isinstance(issue, dict) else {}
    summary = (issue.get("signal", {}) or {}).get("summary", "")
    summary = (summary or "").strip()
    if len(summary) > 160:
        summary = summary[:157].rstrip() + "..."

    tweet_text = social.get("twitter") or (
        f"🧬 Protein Design Digest #{issue_number}\n"
        f"{signal_title}\n"
        f"{summary}\n"
        f"Paper: {issue.get('signal', {}).get('link', '')}\n"
        f"Daily digest: {issue_url}\n"
        f"#ProteinDesign #StructuralBiology #Bioinformatics"
    )
    
    li_text = social.get("linkedin") or (
        f"Protein Design Digest #{issue_number}\n\n"
        f"{signal_title}\n\n"
        f"Summary: {summary}\n\n"
        f"Paper: {issue.get('signal', {}).get('link', '')}\n"
        f"Daily digest: {issue_url}\n\n"
        f"#ProteinDesign #StructuralBiology #Bioinformatics"
    )

    wa_text = (
        f"🧬 *Protein Design Digest LIVE!*\n\n"
        f"Today's Signal: {signal_title}\n"
        f"🔗 *Read Today:* {issue_url}\n"
        f"✍️ *Subscribe:* {sub_url}\n\n"
        f"_(Forward this message to your WhatsApp Status!)_"
    )
    bluesky_text = social.get("bluesky") or tweet_text

    print(f"Publishing Social for {issue_date}...")
    post_to_twitter(tweet_text, issue_url)
    post_to_linkedin(li_text, issue_url)
    post_to_whatsapp(wa_text, issue_url)
    post_to_bluesky(bluesky_text)

if __name__ == "__main__":
    main()
