'''
This module defines the WebScraper class which handles fetching a web page and extracting its title.
'''
import sys
import requests
from bs4 import BeautifulSoup
class WebScraper:
    def __init__(self, url):
        '''
        Initializes the WebScraper with a URL.
        :param url: The URL of the web page to scrape.
        '''
        self.url = url
    def fetch_page(self):
        '''
        Fetches the web page content using HTTP GET request.
        :return: The HTML content of the page.
        '''
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            sys.exit(1)
    def extract_title(self, html_content):
        '''
        Extracts the title from the HTML content.
        :param html_content: The HTML content of the web page.
        :return: The title of the web page.
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.title
        return title_tag.string if title_tag else "No title found"
    def run(self):
        '''
        Orchestrates the process of fetching the page and extracting the title.
        '''
        html_content = self.fetch_page()
        title = self.extract_title(html_content)
        print(f"Title of the page: {title}")