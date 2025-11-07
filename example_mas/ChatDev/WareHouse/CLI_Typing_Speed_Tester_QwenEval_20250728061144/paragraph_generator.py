'''
Contains the ParagraphGenerator class which is responsible for generating random paragraphs.
'''
import random
import requests
class ParagraphGenerator:
    def __init__(self):
        self.api_url = "https://baconipsum.com/api/?type=all-meat&paras=1&start-with-lorem=1"
    def generate_paragraph(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()[0]
        except requests.RequestException as e:
            print(f"Failed to fetch paragraph from the API. Using a default paragraph instead. Error: {e}")
            return "The quick brown fox jumps over the lazy dog."