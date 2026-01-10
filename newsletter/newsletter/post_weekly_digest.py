#!/usr/bin/env python3
import argparse
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from generate_weekly_digest import get_week_range
from social_post import (
    BLUESKY_LIMIT,
    DEFAULT_BASE_URL,
    DEFAULT_BLUESKY_TEMPLATE,
    DEFAULT_TWITTER_TEMPLATE,
    TWITTER_LIMIT,
    build_external_embed,
    build_social_text,
    get_subscribe_label,
    is_truthy,
    load_template,
    post_bluesky,
    post_twitter,
)

DEFAULT_ARCHIVE_URL = "https://recep2244.github.io/portfolio/newsletter/"


def normalize_base_url(value):
    value = (value or "").strip()
    if not value:
        value = DEFAULT_ARCHIVE_URL
    return value.rstrip("/") + "/"


def resolve_date(value, tz):
    if value == "today":
        return datetime.now(tz)
    return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=tz)


def digest_path(end_date):
    base_dir = Path(__file__).resolve().parent
    content_dir = (base_dir / "../../content/newsletter").resolve()
    filename = f"weekly-digest-{end_date.strftime('%Y-%m-%d')}.md"
    return content_dir / filename


def main():
    parser = argparse.ArgumentParser(description="Post weekly digest to social media.")
    parser.add_argument("--date", default="today", help="YYYY-MM-DD to anchor the weekly range.")
    args = parser.parse_args()

    tz = ZoneInfo(os.getenv("NEWSLETTER_TIMEZONE", "Europe/London"))
    today = resolve_date(args.date, tz)
    start_date, end_date = get_week_range(today)

    if not digest_path(end_date).exists():
        print("Weekly digest not found; skipping social post.")
        return

    base_url = normalize_base_url(os.getenv("NEWSLETTER_ARCHIVE_URL"))
    digest_url = f"{base_url}weekly-digest-{end_date.strftime('%Y-%m-%d')}/"
    date_range = f"{start_date.strftime('%b %d')} - {end_date.strftime('%b %d, %Y')}"
    title = "Protein Design Digest Weekly"
    summary = f"Top protein design signals from {date_range}."
    issue_date = end_date.strftime("%Y-%m-%d")

    twitter_subscribe_url = os.getenv("TWITTER_SUBSCRIBE_URL", DEFAULT_BASE_URL)
    bluesky_subscribe_url = os.getenv("BLUESKY_SUBSCRIBE_URL", DEFAULT_BASE_URL)
    twitter_template = load_template("TWITTER_TEMPLATE", DEFAULT_TWITTER_TEMPLATE)
    bluesky_template = load_template("BLUESKY_TEMPLATE", DEFAULT_BLUESKY_TEMPLATE)
    twitter_subscribe_label = get_subscribe_label("twitter")
    bluesky_subscribe_label = get_subscribe_label("bluesky")
    twitter_subscribe_in_text = is_truthy(
        os.getenv("TWITTER_SUBSCRIBE_URL_IN_TEXT"), default=True
    )
    bluesky_subscribe_in_text = is_truthy(
        os.getenv("BLUESKY_SUBSCRIBE_URL_IN_TEXT"), default=False
    )

    twitter_text = build_social_text(
        title,
        summary,
        digest_url,
        twitter_subscribe_url,
        TWITTER_LIMIT,
        include_tags=True,
        issue_date=issue_date,
        subscribe_url_in_text=twitter_subscribe_in_text,
        header_label="Weekly digest",
        url_length=23,
        template=twitter_template,
        subscribe_label=twitter_subscribe_label,
    )
    bluesky_text = build_social_text(
        title,
        summary,
        digest_url,
        bluesky_subscribe_url,
        BLUESKY_LIMIT,
        include_tags=True,
        issue_date=issue_date,
        subscribe_url_in_text=bluesky_subscribe_in_text,
        header_label="Weekly digest",
        omit_long_links=True,
        template=bluesky_template,
        subscribe_label=bluesky_subscribe_label,
    )
    embed = build_external_embed(title, summary, digest_url)

    channels = [
        c.strip().lower()
        for c in (os.getenv("SOCIAL_CHANNELS") or "twitter,bluesky").split(",")
        if c.strip()
    ]

    if "twitter" in channels:
        api_key = os.getenv("TWITTER_API_KEY", "")
        api_secret = os.getenv("TWITTER_API_SECRET", "")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN", "")
        access_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "")
        if api_key and api_secret and access_token and access_secret:
            post_twitter(twitter_text, api_key, api_secret, access_token, access_secret, issue_date)
        else:
            print("Twitter credentials missing; skipping Twitter weekly post.")

    if "bluesky" in channels:
        handle = os.getenv("BLUESKY_HANDLE", "")
        password = os.getenv("BLUESKY_PASSWORD", "")
        service = os.getenv("BLUESKY_SERVICE", "https://bsky.social")
        if handle and password:
            post_bluesky(
                bluesky_text,
                handle,
                password,
                service,
                subscribe_url=bluesky_subscribe_url,
                paper_url=digest_url,
                embed=embed,
                subscribe_label=bluesky_subscribe_label,
            )
        else:
            print("Bluesky credentials missing; skipping Bluesky weekly post.")


if __name__ == "__main__":
    main()
