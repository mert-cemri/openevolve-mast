'''
Handles fetching the RSS feed from a given URL.
'''
import requests
class RSSFetcher:
    def fetch(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content