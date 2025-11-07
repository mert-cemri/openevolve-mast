'''
Main application file for the URL Shortener CLI client.
'''
import requests
import argparse
from urllib.parse import quote
def shorten_url(long_url):
    '''
    Shorten the provided URL using the TinyURL API.
    Parameters:
    long_url (str): The long URL to be shortened.
    Returns:
    str: The shortened URL.
    '''
    try:
        encoded_url = quote(long_url, safe='')
        response = requests.get(f"http://tinyurl.com/api-create.php?url={encoded_url}")
        if response.status_code == 200:
            return response.text
        else:
            return "Error: Unable to shorten URL."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
def main():
    '''
    Main function to handle command-line arguments and output the shortened URL.
    '''
    parser = argparse.ArgumentParser(description='URL Shortener CLI')
    parser.add_argument('long_url', type=str, help='The long URL to shorten')
    args = parser.parse_args()
    short_url = shorten_url(args.long_url)
    print(f"Shortened URL: {short_url}")
if __name__ == "__main__":
    main()