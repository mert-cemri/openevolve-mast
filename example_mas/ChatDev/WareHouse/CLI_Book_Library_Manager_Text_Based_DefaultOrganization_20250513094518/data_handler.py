'''
Handles data storage and retrieval for the library.
'''
import json
from book import Book
class DataHandler:
    def __init__(self, filename):
        self.filename = filename
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except FileNotFoundError:
            return []
    def save_data(self, books):
        with open(self.filename, 'w') as file:
            json.dump([book.__dict__ for book in books], file)