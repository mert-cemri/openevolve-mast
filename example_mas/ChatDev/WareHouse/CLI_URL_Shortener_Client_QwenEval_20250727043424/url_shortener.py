'''
Module containing the URL shortening logic.
Handles the HTTP request to the TinyURL API and includes error handling.
'''
import requests
import logging
from urllib.parse import urlparse
def is_valid_url(url):
    """Check if the URL is valid."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
def shorten_url(long_url):
    """Shorten a URL using the TinyURL API."""
    if not is_valid_url(long_url):
        logging.error(f"Invalid URL: {long_url}")
        return "Error: Invalid URL"
    api_url = "https://tinyurl.com/api-create.php"
    params = {'url': long_url}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        logging.info(f"Successfully shortened URL: {long_url} to {response.text}")
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error shortening URL: {e}")
        return f"Error: {e}"