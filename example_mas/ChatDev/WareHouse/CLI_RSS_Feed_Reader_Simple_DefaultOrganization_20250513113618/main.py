'''
This module contains the main application for the RSS feed reader using a command-line interface (CLI).
'''
import feedparser
def fetch_rss_feed(url):
    '''
    Fetches and parses the RSS feed from the given URL.
    :param url: The URL of the RSS feed.
    :return: Parsed feed object.
    '''
    return feedparser.parse(url)
def main():
    '''
    Main function to run the CLI RSS feed reader.
    Prompts the user for an RSS feed URL, fetches the feed, and displays the titles and links of the latest articles.
    '''
    url = input("Enter RSS Feed URL: ")
    if not url:
        print("Error: Please enter a valid RSS feed URL.")
        return
    try:
        feed = fetch_rss_feed(url)
        if not feed.entries:
            print("No entries found in the feed.")
            return
        for entry in feed.entries:
            print(f"Title: {entry.title}\nLink: {entry.link}\n")
    except Exception as e:
        print(f"Error: Failed to fetch RSS feed: {e}")
if __name__ == "__main__":
    main()