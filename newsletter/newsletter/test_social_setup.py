#!/usr/bin/env python3
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded .env file")
except ImportError:
    pass

def check_env(name):
    val = os.getenv(name)
    if not val:
        print(f"❌ Missing environment variable: {name}")
        return False
    print(f"✅ Found {name}")
    return True

print("--- 🔍 Checking Dependencies ---")
try:
    import tweepy
    print("✅ tweepy installed")
except ImportError:
    print("❌ tweepy NOT installed (run: pip install tweepy)")

try:
    import requests
    print("✅ requests installed")
except ImportError:
    print("❌ requests NOT installed (run: pip install requests)")

try:
    from atproto import Client
    print("✅ atproto installed")
except ImportError:
    print("❌ atproto NOT installed (run: pip install atproto)")

print("\n--- 🐦 Checking Twitter Configuration ---")
has_twitter_vars = (
    check_env("TWITTER_API_KEY") and 
    check_env("TWITTER_API_SECRET") and 
    check_env("TWITTER_ACCESS_TOKEN") and 
    check_env("TWITTER_ACCESS_TOKEN_SECRET")
)

if has_twitter_vars:
    try:
        print("Attempting Twitter Authentication...")
        client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        me = client.get_me()
        if me.data:
            print(f"✅ Twitter Auth Successful: Logged in as @{me.data.username}")
        else:
             print("❌ Twitter Auth returned no data (Check if tokens are valid)")
    except Exception as e:
        print(f"❌ Twitter Auth Failed: {e}")
        print("💡 TIP: Ensure your App has 'Read and Write' permissions in the Twitter Developer Portal.")
        print("   If you changed permissions recently, you MUST Regenerate your Access Token and Secret.")
else:
    print("⚠️ Twitter credentials missing. Start execution with env vars or .env file.")

print("\n--- 🦋 Checking Bluesky Configuration ---")
has_bsky_vars = check_env("BLUESKY_HANDLE") and check_env("BLUESKY_PASSWORD")

if has_bsky_vars:
    try:
        print("Attempting Bluesky Authentication...")
        client = Client()
        client.login(os.getenv("BLUESKY_HANDLE"), os.getenv("BLUESKY_PASSWORD"))
        print(f"✅ Bluesky Auth Successful")
    except Exception as e:
        print(f"❌ Bluesky Auth Failed: {e}")
else:
    print("⚠️ Bluesky credentials missing.")

print("\n--- 💼 Checking LinkedIn Configuration ---")
has_li_vars = check_env("LINKEDIN_ACCESS_TOKEN") and check_env("LINKEDIN_MEMBER_ID")

if has_li_vars:
    print(f"✅ LinkedIn variables found (verification requires attempting a post, skipped)")
else:
    print("⚠️ LinkedIn credentials missing.")
