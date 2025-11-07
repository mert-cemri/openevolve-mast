'''
This module contains utility functions for fetching and parsing RSS feeds.
'''
import feedparser
def fetch_rss_feed(url):
    '''
    Fetches and parses the RSS feed from the given URL.
    Parameters:
    url (str): The URL of the RSS feed.
    Returns:
    list of tuples: A list of (title, link) tuples for the latest articles.
    '''
    feed = feedparser.parse(url)
    if feed.bozo:
        raise ValueError("Invalid RSS feed URL or feed is not well-formed.")
    articles = []
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        articles.append((title, link))
    return articles