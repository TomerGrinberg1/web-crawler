import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.parse import urljoin


class WebCrawler:
    """
    A class for web crawling and extracting data from web pages.
    Args:
        base_url (str): The base URL of the website to crawl.
    Attributes:
        base_url (str): The base URL of the website to crawl.
        page_data (list): A list to store the crawled page data.
        visited_urls (set): A set to store the URLs that have been visited during crawling.
    Methods:
        extract_main_content(soup): Extracts the main textual content from a BeautifulSoup object.
        crawl_website(): Crawls the website, extracts page data, and saves it to the page_data list.
        save_to_excel(filename): Saves the crawled page data to an Excel file.
    """
    
    def __init__(self, base_url):
        """
        Initializes a new instance of the WebCrawler class.
        Args:
            base_url (str): The base URL of the website to crawl.
        """
        self.base_url = base_url
        self.page_data = []
        self.visited_urls = set()

    def extract_main_content(self, soup):
        """
        Extracts the main textual content from a BeautifulSoup object.
        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the web page.
        Returns:
            str: The extracted main textual content.
        """
        content = []
        
        # Assuming text from headers and paragraphs will represent the main content of most pages
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
            content.append(tag.get_text(strip=True))
        
        return ' '.join(content)

    def crawl_website(self):
        """
        Crawls the website, extracts page data, and saves it to the page_data list.
        Raises:
            Exception: If not enough links are found on the main page (<10).
        """
        # Request the main page
        self.visited_urls.add(self.base_url)

        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract page title and main textual content
        page_title = soup.title.string if soup.title else "Missing Title"
        page_content = self.extract_main_content(soup)
        
        self.page_data.append({
            'Page Name': page_title,
            'Page URL': self.base_url,
            'Page Content': page_content
        })
        
        # Find all the links on the main page (2nd level)
        links = soup.find_all('a', href=True)
        if len(links) < 10:
            raise Exception("Not enough links found on the main page")
        
        # Limit the number of links to at least 10
        for link in links:
            href = link['href']
            full_url = urljoin(self.base_url, href)
            if full_url in self.visited_urls:
                continue
            else:
                self.visited_urls.add(full_url)
 
            try:
                response = requests.get(full_url)
                soup = BeautifulSoup(response.content, 'html.parser')
                page_title = soup.title.string if soup.title else "Missing Title"
                page_content = self.extract_main_content(soup)

                self.page_data.append({
                    'Page Name': page_title,
                    'Page URL': full_url,
                    'Page Content': page_content
                })
            except requests.RequestException as e:
                print(f"Failed to crawl {full_url}: {e}")


    def save_to_excel(self, filename='web_crawl_data.xlsx'):
        """
        Saves the crawled page data to an Excel file.
        Args:
            filename (str, optional): The name of the Excel file to save the data to. Defaults to 'web_crawl_data.xlsx'.
        """
        df = pd.DataFrame(self.page_data)
        if os.path.exists(filename):
            os.remove(filename)
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
