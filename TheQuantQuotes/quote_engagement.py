"""
Quote engagement tracking - manages likes and shares for quotes.
"""

import json
import os
from typing import Dict, Tuple

# Data storage path
from pathlib import Path

# Directory containing this Python file
BASE_DIR = Path(__file__).resolve().parent

# JSON file in the same directory as quote_engagement.py
ENGAGEMENT_FILE = BASE_DIR / "quote_engagement.json"



def load_engagement() -> Dict[str, Dict[str, int]]:
    """
    Load engagement data from JSON file.

    Returns:
        Dictionary with quote as key and {'likes': count, 'shares': count} as value
    """
    ensure_data_dir()

    if ENGAGEMENT_FILE.exists():
        try:
            with open(ENGAGEMENT_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_engagement(engagement: Dict[str, Dict[str, int]]):
    """
    Save engagement data to JSON file.

    Args:
        engagement: Dictionary with quote engagement data
    """
    
    with open(ENGAGEMENT_FILE, "w") as f:
        json.dump(engagement, f, indent=2)


def get_quote_engagement(quote: str) -> Tuple[int, int]:
    """
    Get likes and shares for a specific quote.

    Args:
        quote: The quote text

    Returns:
        Tuple of (likes, shares)
    """
    engagement = load_engagement()
    if quote in engagement:
        return engagement[quote].get("likes", 0), engagement[quote].get("shares", 0)
    return 0, 0


def add_like(quote: str) -> int:
    """
    Add a like to a quote.

    Args:
        quote: The quote text

    Returns:
        New like count
    """
    engagement = load_engagement()

    if quote not in engagement:
        engagement[quote] = {"likes": 0, "shares": 0}

    engagement[quote]["likes"] += 1
    save_engagement(engagement)

    return engagement[quote]["likes"]


def add_share(quote: str, platform: str = "general") -> int:
    """
    Add a share to a quote.

    Args:
        quote: The quote text
        platform: Social media platform (for analytics)

    Returns:
        New share count
    """
    engagement = load_engagement()

    if quote not in engagement:
        engagement[quote] = {"likes": 0, "shares": 0}

    engagement[quote]["shares"] += 1
    save_engagement(engagement)

    return engagement[quote]["shares"]


def get_top_quotes(limit: int = 10) -> list:
    """
    Get top quotes by engagement (likes + shares).

    Args:
        limit: Number of top quotes to return

    Returns:
        List of (quote, likes, shares, total_engagement) tuples
    """
    engagement = load_engagement()

    if not engagement:
        return []

    quotes_by_engagement = [
        (
            quote,
            data.get("likes", 0),
            data.get("shares", 0),
            data.get("likes", 0) + data.get("shares", 0),
        )
        for quote, data in engagement.items()
    ]

    quotes_by_engagement.sort(key=lambda x: x[3], reverse=True)

    return quotes_by_engagement[:limit]


def get_engagement_stats() -> Dict:
    """
    Get overall engagement statistics.

    Returns:
        Dictionary with total likes, shares, and quoted tracked
    """
    engagement = load_engagement()

    total_likes = sum(data.get("likes", 0) for data in engagement.values())
    total_shares = sum(data.get("shares", 0) for data in engagement.values())

    return {
        "total_likes": total_likes,
        "total_shares": total_shares,
        "quotes_tracked": len(engagement),
        "total_engagement": total_likes + total_shares,
    }
