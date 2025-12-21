import os
import json
import requests
import argparse
from datetime import datetime
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

def post_to_twitter(text, link):
    load_dotenv()
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

def post_to_linkedin(text, link):
    load_dotenv()
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

    tweet_text = f"🧬 Protein Design Digest #{issue_number}\n\nToday's Signal: {signal_title}\n\n#ProteinDesign #StructuralBiology #Bioinformatics"
    
    # LinkedIn text can be longer
    li_text = (
        f"🧬 Protein Design Digest Edition #{issue_number} is out!\n\n"
        f"Today's Highlight: {signal_title}\n\n"
        f"Read the full methodology and industry insights here: {issue_url}\n\n"
        f"#ProteinDesign #StructuralBiology #AI #DrugDiscovery #Bioinformatics #LinkedIn"
    )

    print(f"Publishing Social for {issue_date}...")
    post_to_twitter(tweet_text, issue_url)
    post_to_linkedin(li_text, issue_url)

if __name__ == "__main__":
    main()
