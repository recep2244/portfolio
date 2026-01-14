"""Shared utility functions for the newsletter system."""

import json
from pathlib import Path
from typing import Any, Union


def load_json(path: Union[str, Path]) -> dict[str, Any]:
    """Load and parse a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Union[str, Path], data: dict[str, Any]) -> None:
    """Save data to a JSON file with pretty formatting."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def coerce_list(value: Any) -> list:
    """
    Convert a value to a list.

    - None -> []
    - str -> [str]
    - list -> list (unchanged)
    - other iterables -> list(value)
    """
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return value
    try:
        return list(value)
    except TypeError:
        return [value]


def normalize_email(email: str) -> str:
    """Normalize an email address for comparison."""
    if not email:
        return ""
    return email.strip().lower()


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length, adding suffix if truncated."""
    if not text or len(text) <= max_length:
        return text or ""
    return text[:max_length - len(suffix)].rsplit(" ", 1)[0] + suffix
