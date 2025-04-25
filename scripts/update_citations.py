#!/usr/bin/env python3
import os
import json
import requests
from bs4 import BeautifulSoup

# Fetch author basics and citation count via scraping Google Scholar
GS_USER_ID = os.getenv("GS_USER_ID", "RgO7ppoAAAAJ")
url = f"https://scholar.google.com/citations?user={GS_USER_ID}&hl=en"
try:
    res = requests.get(url, timeout=10)
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