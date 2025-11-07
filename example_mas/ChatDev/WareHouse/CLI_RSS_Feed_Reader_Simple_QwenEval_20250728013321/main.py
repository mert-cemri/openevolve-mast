'''
Main entry point for the RSS feed reader application.
Handles the command-line interface interactions.
'''
import requests
from rss_fetcher import RSSFetcher
from rss_parser import RSSParser
def main():
    url = input("Enter the RSS feed URL: ")
    fetcher = RSSFetcher()
    parser = RSSParser()
    try:
        content = fetcher.fetch(url)
        articles = parser.parse(content)
        if not articles:
            print("No articles found in the feed.")
        else:
            for title, link in articles:
                print(f"Title: {title}\nLink: {link}\n")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the feed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    main()