
# WebCrawler

A simple Python-based web crawler that extracts page data (titles and textual content) from a website and its linked pages. The crawler saves the crawled data into an Excel file.

## Features

- Crawl a given website, extract page titles and main textual content (headers and paragraphs).
- Handles relative and absolute links.
- Optional depth control to limit how deep the crawler goes into linked pages.
- Saves the crawled data into an Excel file.
- Handles errors gracefully and logs failed requests.
- Retry and timeout mechanisms for better performance and robustness.

## Requirements

To run this project, you'll need Python 3.6+ and the following Python packages:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

You can install the required packages using:

```bash
pip install -r requirements.txt
```

##Installation and Setup
Clone the repository:

```bash
git clone https://github.com/yourusername/web_crawler.git
```

Navigate to the project directory:

```bash
cd web_crawler
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Modify the main.py file to update the desire_url variable to the website you want to crawl.

Run the crawler:

```bash
python main.py
```

## How to Use

Crawling a Website
The web crawler takes a base URL as input (I have used Jeen.ai website as default), crawls the main page, and follows the links found on that page (up to a specified depth). It extracts and saves the following information for each page:

Page Name: The title of the page.
Page URL: The full URL of the page.
Page Content: The main textual content extracted from headers (h1, h2, h3) and paragraphs (p).
Saving Data
By default, the crawler saves the extracted data into an Excel file called web_crawl_data.xlsx. You can change the filename or export it as a CSV by modifying the save_to_excel or save_to_csv functions in the WebCrawler class.

Command-Line Usage
You can configure the base URL and other parameters directly within the main.py file.

```python
from web_crawler import WebCrawler

if __name__ == "__main__":
    desire_url = 'https://jeen.ai/'  # Set your target URL
    
    crawler = WebCrawler(desire_url)
    
    try:
        crawler.crawl_website()
    except Exception as e:
        print(f"Error during crawling: {e}")
    
    crawler.save_to_excel('web_crawl_data.xlsx')  # Save to Excel file
```
## Acknowledgements
The project utilizes the BeautifulSoup library for HTML parsing and requests for handling HTTP requests.

