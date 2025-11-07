'''
Handles interaction with the URL shortening API.
'''
import os
import requests
class URLShortener:
    def __init__(self):
        self.api_url = "https://api.tinyurl.com/create"
        self.api_key = os.getenv("TINYURL_API_KEY")  # Fetch the API key from environment variables
    def shorten(self, long_url):
        if not self.api_key:
            raise Exception("API key not found. Please set the TINYURL_API_KEY environment variable.")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "url": long_url,
            "domain": "tiny.one"
        }
        response = requests.post(self.api_url, json=data, headers=headers)
        if response.status_code == 201:
            return response.json()["data"]["tiny_url"]
        else:
            try:
                error_message = response.json().get('message', 'Unknown error')
            except ValueError:  # includes simplejson.decoder.JSONDecodeError
                error_message = 'Non-JSON response received'
            raise Exception(f"Error: {error_message}")