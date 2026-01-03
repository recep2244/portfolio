#!/usr/bin/env python3
import argparse
import requests
import sys

def main():
    parser = argparse.ArgumentParser(description="Fetch LinkedIn Member URN using Access Token")
    parser.add_argument("--token", required=True, help="LinkedIn Access Token")
    args = parser.parse_args()

    url = "https://api.linkedin.com/v2/userinfo"
    headers = {
        "Authorization": f"Bearer {args.token}",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    print(f"🔍 Fetching profile info...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # The 'sub' field usually contains the URN ID in OpenID context, 
        # but for w_member_social we usually need urn:li:person:<ID>
        # Let's see what we get.
        
        print("\n✅ Success!")
        print("--- Response Data ---")
        print(data)
        print("---------------------")
        
        # Extract ID
        if 'sub' in data:
             member_id = data['sub']
             print(f"\n🔑 Your LinkedIn Member ID (for Secrets): {member_id}")
             print(f"   (Use this as LINKEDIN_MEMBER_ID)")
        else:
             print("\n⚠️ 'sub' field not found. Look for the ID in the response above.")
             
    except Exception as e:
        print(f"❌ Failed to fetch profile: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response: {e.response.text}")

if __name__ == "__main__":
    main()
