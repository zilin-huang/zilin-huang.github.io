import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def get_citation_count():
    # 你的Google Scholar ID
    SCHOLAR_ID = 'RgO7ppoAAAAJ'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    url = f'https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en'
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到引用数的元素
        citation_element = soup.find('td', class_='gsc_rsb_std')
        if citation_element:
            citations = citation_element.text
            return int(citations)
    except Exception as e:
        print(f"Error fetching citations: {e}")
        return None
    
    return None

def update_citation_file():
    citations = get_citation_count()
    if citations is not None:
        data = {
            'citations': citations,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 确保_data目录存在
        os.makedirs('_data', exist_ok=True)
        
        # 写入数据到JSON文件
        with open('_data/citations.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully updated citations: {citations}")
        return True
    
    return False

if __name__ == "__main__":
    update_citation_file() 