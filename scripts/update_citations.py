#!/usr/bin/env python3
import os
import json
import requests
from bs4 import BeautifulSoup

# Fetch author basics and citation count via scraping Google Scholar
# Determine Google Scholar user ID, stripping any whitespace and falling back to the default ID if empty
env_user = os.getenv("GS_USER_ID", "").strip()
GS_USER_ID = env_user if env_user else "RgO7ppoAAAAJ"
url = f"https://scholar.google.com/citations?user={GS_USER_ID}&hl=en"
try:
    # Add headers to mimic a real browser and avoid blocking by Google Scholar
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://scholar.google.com"
    }
    res = requests.get(url, headers=headers, timeout=10)
    # Debug log: HTTP status code
    print(f"Fetched {url}, status code {res.status_code}")
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    stats = soup.find_all("td", class_="gsc_rsb_std")
    total_citations = stats[0].text if stats and len(stats) > 0 else "0"
except Exception as e:
    print(f"Error fetching citation count: {e}")
    total_citations = "0"

# Prepare output JSON
data = {"citations": total_citations}
output_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets", "js", "citation-count.json"))
with open(output_path, "w") as f:
    json.dump(data, f)

print(f"Updated citation count to {total_citations}") 