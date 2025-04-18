#!/usr/bin/env python3
import os
import json
from scholarly import scholarly, ProxyGenerator

# Use FreeProxies to avoid rate limits on Google Scholar
GS_USER_ID = os.getenv("GS_USER_ID", "RgO7ppoAAAAJ")
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

# Fetch author basics and citation count
author = scholarly.search_author_id(GS_USER_ID)
author = scholarly.fill(author, sections=["basics"])
total_citations = str(author.get("citedby", "0"))

# Prepare output JSON
data = {"citations": total_citations}
output_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets", "js", "citation-count.json"))
with open(output_path, "w") as f:
    json.dump(data, f)

print(f"Updated citation count to {total_citations}") 