'''
Manages loading and retrieval of quotes from a text file.
'''
import random
import sys
class QuoteManager:
    def __init__(self):
        '''
        Initialize the QuoteManager with an empty list of quotes.
        '''
        self.quotes = []
    def load_quotes(self, file_path):
        '''
        Load quotes from a specified text file.
        :param file_path: Path to the text file containing quotes.
        '''
        try:
            with open(file_path, 'r') as file:
                self.quotes = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            sys.exit(1)  # Exit the program with a non-zero status
    def get_random_quote(self):
        '''
        Return a random quote from the loaded list.
        :return: A random quote string.
        '''
        if not self.quotes:
            return "No quotes available."
        return random.choice(self.quotes)