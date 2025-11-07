'''
Handles the command-line interface interactions.
'''
from rss_fetcher import RSSFetcher
from rss_parser import RSSParser
class CLIInterface:
    def run(self):
        url = input("Enter the RSS feed URL: ")
        fetcher = RSSFetcher()
        parser = RSSParser()
        try:
            content = fetcher.fetch(url)
            articles = parser.parse(content)
            for title, link in articles:
                print(f"Title: {title}\nLink: {link}\n")
        except Exception as e:
            print(f"An error occurred: {e}")