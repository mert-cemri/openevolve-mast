'''
Main entry point for the CLI web scraper application.
Handles user input, web scraping, and output.
'''
import sys
from scraper import WebScraper
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    url = cli.get_user_input()
    scraper = WebScraper()
    try:
        html_content = scraper.fetch_url(url)
        title = scraper.extract_title(html_content)
        cli.display_title(title)
    except requests.exceptions.RequestException as e:
        cli.display_title(f"Error fetching URL: {e}")
if __name__ == "__main__":
    main()