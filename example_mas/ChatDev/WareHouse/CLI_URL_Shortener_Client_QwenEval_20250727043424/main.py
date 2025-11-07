'''
Main entry point for the URL shortener CLI application.
Handles command-line arguments and calls the URL shortening function.
'''
import argparse
import logging
from url_shortener import shorten_url
def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    parser = argparse.ArgumentParser(description="Shorten a URL using TinyURL")
    parser.add_argument("url", type=str, help="The long URL to shorten")
    args = parser.parse_args()
    long_url = args.url
    logging.info(f"Attempting to shorten URL: {long_url}")
    shortened_url = shorten_url(long_url)
    print(f"Shortened URL: {shortened_url}")
if __name__ == "__main__":
    main()