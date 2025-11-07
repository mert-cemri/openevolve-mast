'''
This script is a simple CLI web scraper that takes a URL as input and extracts and prints the title of the web page.
'''
import sys
from scraper import WebScraper
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    scraper = WebScraper(url)
    scraper.run()
if __name__ == "__main__":
    main()