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
    urls = [
        f"https://www.youtube.com/@{handle}",
        f"https://www.youtube.com/@{handle}/about",
    ]
    headers = {"User-Agent": "Mozilla/5.0 (compatible; PodcastSync/1.0)"}
    for url in urls:
        resp = session.get(url, headers=headers, timeout=20)
        if resp.status_code != 200:
            continue
        match = re.search(r'"channelId":"(UC[^"]+)"', resp.text)
        if match:
            return match.group(1)
    return None


def fetch_feed(channel_id, session):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    try:
        resp = session.get(url, timeout=20)
        if resp.status_code != 200:
            print(f"Warning: YouTube feed returned {resp.status_code} for channel {channel_id}; skipping feed.", file=sys.stderr)
            return None
        return resp.text
    except Exception as exc:
        print(f"Warning: failed to fetch YouTube feed: {exc}", file=sys.stderr)
        return None


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
    manual = data.get("podcasts_manual") or []
    manual_entries = normalize_manual_entries(manual)
    combined = manual_entries + entries
    if not combined:
        print("No entries found; leaving existing podcasts unchanged.")
        return False
    data["podcasts"] = combined
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
    return True


def fetch_oembed_info(youtube_url, session):
    url = "https://www.youtube.com/oembed"
    resp = session.get(url, params={"url": youtube_url, "format": "json"}, timeout=20)
    if resp.status_code != 200:
        return {}
    try:
        return resp.json()
    except ValueError:
        return {}


def normalize_manual_entries(items):
    if not items:
        return []
    session = requests.Session()
    normalized = []
    for item in items:
        url = (item.get("youtube_url") or "").strip()
        if not url:
            continue
        title = (item.get("title") or "").strip()
        description = (item.get("description") or "").strip()
        date = (item.get("date") or "").strip()
        duration = (item.get("duration") or "").strip()
        if not title or not description:
            info = fetch_oembed_info(url, session)
            if not title:
                title = info.get("title", "").strip()
            if not description:
                author = info.get("author_name", "").strip()
                description = f"Featured talk from {author}." if author else "Featured talk from a partner channel."
        normalized.append(
            {
                "title": title or "Featured talk",
                "description": description or "Featured talk from a partner channel.",
                "youtube_url": url,
                "date": date,
                "duration": duration,
            }
        )
    return normalized


def main():
    parser = argparse.ArgumentParser(description="Sync podcast entries from YouTube RSS feed.")
    parser.add_argument("--handle", default="recepadyaman_proteins", help="YouTube channel handle (without @)")
    parser.add_argument("--limit", type=int, default=6, help="Number of episodes to sync")
    parser.add_argument("--output", default="data/cv.yaml", help="YAML file to update")
    args = parser.parse_args()

    session = requests.Session()
    channel_id = fetch_channel_id(args.handle, session) or os.getenv("YOUTUBE_CHANNEL_ID")
    entries = []
    if channel_id:
        feed_xml = fetch_feed(channel_id, session)
        if feed_xml:
            entries = parse_feed(feed_xml, args.limit)
        else:
            print("Warning: YouTube feed unavailable; syncing manual entries only.", file=sys.stderr)
    else:
        print("Warning: channel ID not resolved; syncing manual entries only.", file=sys.stderr)
    changed = update_yaml(args.output, entries)
    if changed:
        print(f"Updated {args.output} with {len(entries)} episodes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
