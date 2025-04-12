from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import os
from datetime import datetime
import time

def get_citation_count():
    # 你的Google Scholar ID
    SCHOLAR_ID = 'RgO7ppoAAAAJ'
    
    print("Setting up Chrome options...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无界面模式
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    try:
        print("Starting Chrome browser...")
        driver = webdriver.Chrome(options=chrome_options)
        
        url = f'https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en'
        print(f"Navigating to: {url}")
        driver.get(url)
        
        # 等待页面加载
        print("Waiting for page to load...")
        time.sleep(3)
        
        # 等待引用数元素出现
        print("Looking for citation count...")
        wait = WebDriverWait(driver, 10)
        citation_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "gsc_rsb_std"))
        )
        
        citations = citation_element.text.strip()
        print(f"Found citation text: {citations}")
        
        # 保存页面源代码以供调试
        with open('debug_page.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        
        driver.quit()
        
        try:
            return int(citations)
        except ValueError:
            print(f"Could not convert citation count '{citations}' to integer")
            return None
            
    except Exception as e:
        print(f"Error fetching citations: {e}")
        if 'driver' in locals():
            driver.quit()
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