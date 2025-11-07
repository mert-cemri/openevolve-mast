'''
Handles the translation logic using a language translation API.
'''
import os
import requests
from dotenv import load_dotenv
load_dotenv()
class Translator:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_url = 'https://translation.googleapis.com/language/translate/v2'
        if not self.api_key:
            raise ValueError("API_KEY is not set in the environment variables.")
    def translate(self, text, target_language):
        if not text or not target_language:
            return "Error: Text and target language must be provided."
        params = {
            'q': text,
            'target': target_language,
            'key': self.api_key
        }
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()['data']['translations'][0]['translatedText']
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"