import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random

def get_citation_count(scholar_id):
    url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Add random delay to avoid rate limiting
        time.sleep(random.uniform(1, 3))
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the citation count from the table
        citation_count = 0
        tables = soup.find_all('td', class_='gsc_rsb_std')
        if tables and len(tables) >= 1:
            citation_count = int(tables[0].text)
        
        return citation_count
    
    except Exception as e:
        print(f"Error fetching citation count: {str(e)}")
        return None

def main():
    # Your Google Scholar ID
    scholar_id = "RgO7ppoAAAAJ"
    
    # Get citation count
    citations = get_citation_count(scholar_id)
    
    if citations is not None:
        # Create _data directory if it doesn't exist
        os.makedirs('_data', exist_ok=True)
        
        # Save to JSON file
        data = {'citations': citations}
        with open('_data/citations.json', 'w') as f:
            json.dump(data, f)
        print(f"Successfully updated citation count to: {citations}")
    else:
        print("Failed to update citation count")

if __name__ == "__main__":
    main() 