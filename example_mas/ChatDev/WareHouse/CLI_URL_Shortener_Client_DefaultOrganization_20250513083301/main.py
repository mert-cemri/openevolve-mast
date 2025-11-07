'''
Main application file for the URL Shortening CLI.
'''
import argparse
from url_shortener import URLShortener
def shorten_url(long_url):
    url_shortener = URLShortener()
    try:
        short_url = url_shortener.shorten(long_url)
        print(f"Shortened URL: {short_url}")
    except Exception as e:
        print(f"Failed to shorten URL: {e}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='URL Shortener CLI')
    parser.add_argument('url', type=str, help='The URL to shorten')
    args = parser.parse_args()
    shorten_url(args.url)