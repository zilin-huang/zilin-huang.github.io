import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
from urllib.request import Request, urlopen
import re

def format_citation_count(count):
    """Format large numbers into K, M, B format"""
    if count >= 1000000000:
        return f"{count/1000000000:.1f}B"
    elif count >= 1000000:
        return f"{count/1000000:.1f}M"
    elif count >= 1000:
        return f"{count/1000:.1f}K"
    return str(count)

def get_citation_count(scholar_id):
    url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
    headers = {
        'User-Agent': f'Mozilla/5.0 (compatible; Scholar/1.0; +http://example.org/bot)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    
    try:
        # Add random delay to avoid rate limiting
        time.sleep(random.uniform(2, 5))
        
        # First try with requests
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            html_content = response.text
        except:
            # If requests fails, try with urllib
            req = Request(url, headers=headers)
            html_content = urlopen(req, timeout=10).read().decode('utf-8')
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Try multiple methods to find citation count
        citation_count = 0
        
        # Method 1: Look for td with class gsc_rsb_std
        tables = soup.find_all('td', class_='gsc_rsb_std')
        if tables and len(tables) >= 1:
            try:
                citation_count = int(tables[0].text.replace(',', ''))
                return citation_count
            except:
                pass
        
        # Method 2: Look for meta description
        description_meta = soup.find('meta', {'name': 'description'})
        if description_meta:
            content = description_meta.get('content', '')
            matches = re.search(r'Cited by (\d+[,\d]*)', content)
            if matches:
                try:
                    citation_count = int(matches.group(1).replace(',', ''))
                    return citation_count
                except:
                    pass
        
        # Method 3: Look for specific div containing citations
        citation_div = soup.find('div', {'class': 'gsc_rsb_s'})
        if citation_div:
            citation_text = citation_div.get_text()
            matches = re.search(r'Citations\s*(\d+[,\d]*)', citation_text)
            if matches:
                try:
                    citation_count = int(matches.group(1).replace(',', ''))
                    return citation_count
                except:
                    pass
        
        return citation_count if citation_count > 0 else None
    
    except Exception as e:
        print(f"Error fetching citation count: {str(e)}")
        return None

def load_existing_count():
    """Load existing citation count from file"""
    try:
        with open('_data/citations.json', 'r') as f:
            data = json.load(f)
            return data.get('citations', 0)
    except:
        return 0

def main():
    # Your Google Scholar ID
    scholar_id = "RgO7ppoAAAAJ"
    
    # Get existing count
    existing_count = load_existing_count()
    
    # Get new citation count
    new_count = get_citation_count(scholar_id)
    
    # If failed to get new count, keep existing count
    citations = new_count if new_count is not None else existing_count
    
    # Create _data directory if it doesn't exist
    os.makedirs('_data', exist_ok=True)
    
    # Save to JSON file
    data = {'citations': citations}
    with open('_data/citations.json', 'w') as f:
        json.dump(data, f)
    
    if new_count is not None:
        print(f"Successfully updated citation count to: {citations}")
    else:
        print(f"Failed to fetch new count, keeping existing count: {citations}")

if __name__ == "__main__":
    main() 