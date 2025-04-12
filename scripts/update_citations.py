import json
import os
from datetime import datetime
from scholarly import scholarly, ProxyGenerator

def get_citation_count():
    try:
        # 设置代理生成器来避免被封禁
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        
        # 你的Google Scholar ID
        AUTHOR_ID = 'RgO7ppoAAAAJ'
        print(f"Fetching citations for author ID: {AUTHOR_ID}")
        
        # 获取作者资料
        author = scholarly.search_author_id(AUTHOR_ID)
        if author:
            # 获取完整的作者信息
            author = scholarly.fill(author)
            citations = author['citedby']
            print(f"Found citations: {citations}")
            return citations
        else:
            print("Author not found")
            return None
            
    except Exception as e:
        print(f"Error fetching citations: {e}")
        return None

def update_citation_file():
    citations = get_citation_count()
    print(f"Retrieved citation count: {citations}")
    
    if citations is not None:
        data = {
            'citations': citations,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 确保_data目录存在
        os.makedirs('_data', exist_ok=True)
        file_path = '_data/citations.json'
        
        # 写入数据到JSON文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully updated citations file at: {file_path}")
        print(f"File contents: {json.dumps(data, ensure_ascii=False, indent=2)}")
        return True
    
    return False

if __name__ == "__main__":
    print("Starting citation update script...")
    success = update_citation_file()
    print(f"Script completed with success: {success}") 