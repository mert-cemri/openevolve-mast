'''
This module provides a simple CLI web scraper that takes a URL and extracts and prints the title of the web page.
'''
import requests
from bs4 import BeautifulSoup
class WebScraper:
    '''
    A class to represent a web scraper for extracting the title of a web page.
    '''
    def fetch_html(self, url):
        '''
        Makes an HTTP GET request to the given URL and returns the HTML content.
        Parameters:
            url (str): The URL of the web page to scrape.
        Returns:
            str: The HTML content of the web page.
        '''
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the URL: {e}")
            return None
    def extract_title(self, html):
        '''
        Parses the HTML content and extracts the title of the web page.
        Parameters:
            html (str): The HTML content of the web page.
        Returns:
            str: The title of the web page.
        '''
        if html is None:
            return None
        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.title
        return title_tag.string if title_tag else "No title found"
def main():
    '''
    The main function to run the CLI web scraper.
    '''
    url = input("Enter the URL of the web page: ")
    scraper = WebScraper()
    html = scraper.fetch_html(url)
    title = scraper.extract_title(html)
    if title:
        print(f"The title of the web page is: {title}")
    else:
        print("Failed to extract the title.")
if __name__ == "__main__":
    main()