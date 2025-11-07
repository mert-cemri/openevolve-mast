'''
Handles the web scraping functionality.
'''
import requests
from bs4 import BeautifulSoup
class WebScraper:
    def fetch_url(self, url):
        '''
        Fetches the content of the URL.
        Raises exceptions that may occur during the HTTP request.
        '''
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            raise e  # Raising the exception to be handled at a higher level
    def extract_title(self, html_content):
        '''
        Extracts the title from the HTML content.
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.find('title')
        return title_tag.string if title_tag else 'No title found'