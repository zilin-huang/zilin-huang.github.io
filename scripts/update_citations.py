#!/usr/bin/env python3
"""
Fetch the latest Google Scholar citation count and write it to
assets/js/citation-count.json so the website can display it.

Priority:
  1. Google Scholar (via scholarly)
  2. Semantic Scholar public API (fallback)
  3. Keep the existing value on disk (safe fallback)
"""

import json
import os
import time
from typing import Optional

OUTPUT_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "assets", "js", "citation-count.json")
)

GOOGLE_SCHOLAR_ID = "RgO7ppoAAAAJ"
SS_AUTHOR_ID = os.getenv("SS_AUTHOR_ID", "2278457018")

MAX_RETRIES = 3


def read_existing_count() -> Optional[str]:
    """Return the citation string currently stored on disk, or None."""
    try:
        with open(OUTPUT_PATH) as f:
            return json.load(f).get("citations")
    except Exception:
        return None


def fetch_google_scholar() -> Optional[str]:
    """Scrape the citation count from Google Scholar using scholarly."""
    try:
        from scholarly import scholarly, ProxyGenerator

        # Use free proxies to avoid being blocked by Google
        try:
            pg = ProxyGenerator()
            pg.FreeProxies()
            scholarly.use_proxy(pg)
        except Exception as e:
            print(f"Proxy setup failed, trying direct: {e}")

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
                author = scholarly.fill(author, sections=["basics"])
                count = author.get("citedby", None)
                if count is not None:
                    print(f"Google Scholar citation count: {count}")
                    return str(count)
            except Exception as e:
                print(f"Google Scholar attempt {attempt}/{MAX_RETRIES} failed: {e}")
                if attempt < MAX_RETRIES:
                    time.sleep(5 * attempt)
    except ImportError:
        print("scholarly not installed, skipping Google Scholar")
    return None


def fetch_semantic_scholar() -> Optional[str]:
    """Fetch the citation count from the Semantic Scholar API."""
    try:
        import requests

        url = f"https://api.semanticscholar.org/graph/v1/author/{SS_AUTHOR_ID}?fields=citationCount"
        headers = {"User-Agent": "citation-update-bot/1.0"}
        res = requests.get(url, headers=headers, timeout=15)
        print(f"Semantic Scholar status: {res.status_code}")
        res.raise_for_status()
        count = res.json().get("citationCount", 0)
        if count:
            print(f"Semantic Scholar citation count: {count}")
            return str(count)
    except Exception as e:
        print(f"Semantic Scholar error: {e}")
    return None


def main():
    existing = read_existing_count()
    print(f"Existing citation count on disk: {existing}")

    count = fetch_google_scholar() or fetch_semantic_scholar()

    if count and count != "0":
        with open(OUTPUT_PATH, "w") as f:
            json.dump({"citations": count}, f)
        print(f"Updated citation count to {count}")
    elif existing:
        print(f"All sources failed; keeping existing value ({existing})")
    else:
        print("No citation data available and no existing value to keep")


if __name__ == "__main__":
    main()
