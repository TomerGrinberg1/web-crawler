# main.py
from web_crawler import WebCrawler

if __name__ == "__main__":
    desire_url = 'https://www.bbc.com/'  # Set your target URL
    
    crawler = WebCrawler(desire_url)
    
    try:
        crawler.crawl_website()
    except Exception as e:
        print(f"Error during crawling: {e}")
    
    crawler.save_to_excel('web_crawl_data.xlsx')  # Save to Excel file
