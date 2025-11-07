'''
This module contains the main application logic for the CLI RSS feed reader.
'''
from rss_utils import fetch_rss_feed
def main():
    '''
    Main function to execute the RSS feed reader.
    Prompts the user for an RSS feed URL and displays the latest article titles and links.
    '''
    url = input("Enter RSS Feed URL: ")
    if not url:
        print("Please enter a valid RSS feed URL.")
        return
    try:
        articles = fetch_rss_feed(url)
        if not articles:
            print("No articles found.")
        else:
            for title, link in articles:
                print(f"Title: {title}\nLink: {link}\n")
    except Exception as e:
        print(f"Failed to fetch RSS feed: {e}")
if __name__ == "__main__":
    main()