#!/usr/bin/env python3
"""Update the website's citation count from the Google Scholar profile."""

import json
import os
import re
import sys
import time
from typing import Optional

import requests


OUTPUT_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "assets", "js", "citation-count.json")
)

GOOGLE_SCHOLAR_ID = "RgO7ppoAAAAJ"
GOOGLE_SCHOLAR_URL = (
    "https://scholar.google.com/citations"
    f"?user={GOOGLE_SCHOLAR_ID}&hl=en"
)
GOOGLE_SCHOLAR_READER_URL = (
    "https://r.jina.ai/http://scholar.google.com/citations"
    f"?user={GOOGLE_SCHOLAR_ID}&hl=en&cstart=0&pagesize=100"
)
MAX_RETRIES = 3


def read_existing_count() -> Optional[int]:
    """Return the citation count currently stored on disk, if valid."""
    try:
        with open(OUTPUT_PATH, encoding="utf-8") as citation_file:
            count = int(json.load(citation_file)["citations"])
            return count if count > 0 else None
    except (FileNotFoundError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return None


def parse_google_scholar_count(html: str) -> int:
    """Extract the all-time citation count from a Scholar profile page."""
    profile_match = re.search(
        r'<div[^>]+id=["\']gsc_prf_in["\'][^>]*>(.*?)</div>',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    citation_match = re.search(
        r'<td[^>]+class=["\'][^"\']*\bgsc_rsb_std\b[^"\']*["\'][^>]*>'
        r"\s*([\d,]+)\s*</td>",
        html,
        flags=re.IGNORECASE,
    )

    if not profile_match or not citation_match:
        raise ValueError("Google Scholar profile or citation table was not found")

    count = int(citation_match.group(1).replace(",", ""))
    if count <= 0:
        raise ValueError(f"Google Scholar returned an invalid citation count: {count}")
    return count


def parse_google_scholar_reader_count(markdown: str) -> int:
    """Sum per-paper Google Scholar citations from the reader response."""
    if (
        "Title: Zilin Huang" not in markdown
        or f"user={GOOGLE_SCHOLAR_ID}" not in markdown
    ):
        raise ValueError("The Google Scholar reader returned the wrong profile")

    citation_counts = re.findall(
        r"\[([\d,]+)\]\(https?://scholar\.google\.com/scholar\?oi=bibs[^)]*\)",
        markdown,
        flags=re.IGNORECASE,
    )
    if not citation_counts:
        raise ValueError("No per-paper Google Scholar citation counts were found")

    count = sum(int(value.replace(",", "")) for value in citation_counts)
    if count <= 0:
        raise ValueError(f"Google Scholar returned an invalid citation count: {count}")
    return count


def fetch_google_scholar() -> Optional[int]:
    """Fetch Google Scholar directly, then through a read-only web reader."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/131.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    sources = (
        ("direct", GOOGLE_SCHOLAR_URL, parse_google_scholar_count),
        (
            "reader",
            GOOGLE_SCHOLAR_READER_URL,
            parse_google_scholar_reader_count,
        ),
    )

    for source_name, url, parser in sources:
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = requests.get(url, headers=headers, timeout=30)
                print(
                    f"Google Scholar {source_name} attempt {attempt}: "
                    f"HTTP {response.status_code}"
                )
                response.raise_for_status()
                count = parser(response.text)
                print(
                    f"Google Scholar citation count via {source_name}: {count}"
                )
                return count
            except (requests.RequestException, ValueError) as error:
                print(
                    f"Google Scholar {source_name} attempt "
                    f"{attempt}/{MAX_RETRIES} failed: {error}",
                    file=sys.stderr,
                )
                if response_is_forbidden(error) or attempt == MAX_RETRIES:
                    break
                time.sleep(5 * attempt)

    return None


def response_is_forbidden(error: Exception) -> bool:
    """Return whether a request failed because Google blocked the runner."""
    return (
        isinstance(error, requests.HTTPError)
        and error.response is not None
        and error.response.status_code == 403
    )


def write_count(count: int) -> None:
    """Write deterministic JSON so an unchanged count creates no commit."""
    with open(OUTPUT_PATH, "w", encoding="utf-8") as citation_file:
        json.dump({"citations": str(count)}, citation_file)
        citation_file.write("\n")


def main() -> int:
    existing = read_existing_count()
    print(f"Existing citation count on disk: {existing}")

    count = fetch_google_scholar()
    if count is None:
        print(
            "Google Scholar could not be read; preserving the existing citation count.",
            file=sys.stderr,
        )
        return 1

    if count == existing:
        print("Citation count is already current; no file change needed.")
        return 0

    write_count(count)
    print(f"Updated citation count from {existing} to {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
