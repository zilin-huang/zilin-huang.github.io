import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import time

def get_citation_count():
    # 你的Google Scholar ID
    SCHOLAR_ID = 'RgO7ppoAAAAJ'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    
    url = f'https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en'
    print(f"Attempting to fetch citations from: {url}")
    
    try:
        # 添加重试机制
        max_retries = 3
        for attempt in range(max_retries):
            try:
                print(f"Attempt {attempt + 1} of {max_retries}")
                response = requests.get(url, headers=headers, timeout=30)  # 增加超时时间
                response.raise_for_status()  # 检查是否有HTTP错误
                print(f"Response status code: {response.status_code}")
                break
            except (requests.RequestException, requests.Timeout) as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:  # 最后一次尝试
                    print(f"Failed after {max_retries} attempts: {e}")
                    return None
                print("Waiting before retry...")
                time.sleep(5)  # 增加重试等待时间
        
        # 保存响应内容以供调试
        with open('debug_response.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("Saved response content to debug_response.html")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 尝试不同的选择器
        citation_element = None
        selectors = [
            ('td', {'class_': 'gsc_rsb_std'}),
            ('div', {'class_': 'gsc_rsb_std'}),
            ('td', {'class_': 'gsc_rsb_sc1'})
        ]
        
        for tag, attrs in selectors:
            citation_element = soup.find(tag, attrs)
            if citation_element:
                print(f"Found citation element using selector: {tag}, {attrs}")
                break
        
        if citation_element and citation_element.text:
            citations = citation_element.text.strip()
            print(f"Found citation text: {citations}")
            try:
                return int(citations)
            except ValueError:
                print(f"Could not convert citation count '{citations}' to integer")
                return None
        else:
            print("Citation element not found in the page")
            return None
            
    except Exception as e:
        print(f"Error fetching citations: {e}")
        return None

def update_citation_file():
    print("Starting citation update process...")
    citations = get_citation_count()
    
    if citations is not None:
        print(f"Retrieved citation count: {citations}")
        # 确保_data目录存在
        os.makedirs('_data', exist_ok=True)
        print("Created _data directory if it didn't exist")
        
        # 准备数据
        data = {
            'citations': citations,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 写入数据到JSON文件
        try:
            with open('_data/citations.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Successfully wrote citations data to _data/citations.json")
            return True
        except Exception as e:
            print(f"Error writing to citations.json: {e}")
            return False
    else:
        print("No citation count available to update")
        return False

if __name__ == "__main__":
    print("Starting citation update script...")
    success = update_citation_file()
    if not success:
        print("Failed to update citations")
        exit(1)  # 非零退出码表示失败
    else:
        print("Citation update completed successfully")
        exit(0) 