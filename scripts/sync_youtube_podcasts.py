#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import re
import sys
import xml.etree.ElementTree as ET

import requests
import yaml

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def fetch_channel_id(handle, session):
    url = f"https://www.youtube.com/@{handle}"
    resp = session.get(url, timeout=20)
    resp.raise_for_status()
    match = re.search(r'"channelId":"(UC[^"]+)"', resp.text)
    return match.group(1) if match else None


def fetch_feed(channel_id, session):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    resp = session.get(url, timeout=20)
    resp.raise_for_status()
    return resp.text


def format_duration(seconds):
    if seconds is None:
        return ""
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m"
    if minutes:
        return f"{minutes}m"
    return f"{sec}s"


def parse_feed(xml_text, limit):
    root = ET.fromstring(xml_text)
    entries = []
    for entry in root.findall("atom:entry", NS)[:limit]:
        title_el = entry.find("atom:title", NS)
        video_id_el = entry.find("yt:videoId", NS)
        published_el = entry.find("atom:published", NS)
        desc_el = entry.find("media:group/media:description", NS)
        duration_el = entry.find("media:group/yt:duration", NS)

        title = (title_el.text or "").strip() if title_el is not None else ""
        video_id = (video_id_el.text or "").strip() if video_id_el is not None else ""
        published = (published_el.text or "").strip() if published_el is not None else ""
        description = (desc_el.text or "").strip() if desc_el is not None else ""
        duration = ""

        if duration_el is not None:
            seconds = duration_el.attrib.get("seconds")
            if seconds and seconds.isdigit():
                duration = format_duration(int(seconds))

        if published:
            try:
                published_date = dt.datetime.fromisoformat(published.replace("Z", "+00:00")).date()
                published = published_date.isoformat()
            except ValueError:
                published = published[:10]

        if not title or not video_id:
            continue

        entries.append(
            {
                "title": title,
                "description": description or "New episode from the channel.",
                "youtube_url": f"https://www.youtube.com/watch?v={video_id}",
                "date": published or "",
                "duration": duration or "",
            }
        )
    return entries


def update_yaml(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not entries:
        print("No entries found; leaving existing podcasts unchanged.")
        return False
    data["podcasts"] = entries
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=False)
    return True


def main():
    parser = argparse.ArgumentParser(description="Sync podcast entries from YouTube RSS feed.")
    parser.add_argument("--handle", default="recepadyaman_proteins", help="YouTube channel handle (without @)")
    parser.add_argument("--limit", type=int, default=6, help="Number of episodes to sync")
    parser.add_argument("--output", default="data/cv.yaml", help="YAML file to update")
    args = parser.parse_args()

    session = requests.Session()
    channel_id = fetch_channel_id(args.handle, session)
    if not channel_id:
        channel_id = os.getenv("YOUTUBE_CHANNEL_ID")
    if not channel_id:
        print("Failed to resolve channel ID.", file=sys.stderr)
        return 1

    feed_xml = fetch_feed(channel_id, session)
    entries = parse_feed(feed_xml, args.limit)
    changed = update_yaml(args.output, entries)
    if changed:
        print(f"Updated {args.output} with {len(entries)} episodes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
