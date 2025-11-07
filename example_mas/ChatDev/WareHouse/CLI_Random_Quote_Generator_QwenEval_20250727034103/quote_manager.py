'''
Handles reading quotes from a file and selecting a random quote.
'''
import random
class QuoteManager:
    def __init__(self, filename='quotes.txt'):
        '''
        Initializes the QuoteManager with a filename.
        :param filename: The name of the file containing quotes.
        '''
        self.filename = filename
        self.quotes = self.load_quotes()
    def load_quotes(self):
        '''
        Loads quotes from a file.
        :return: A list of quotes.
        '''
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found. Please ensure the file is in the correct directory.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []
    def get_random_quote(self):
        '''
        Returns a random quote from the loaded quotes.
        :return: A random quote as a string.
        '''
        if not self.quotes:
            return "Life is what happens when you're busy making other plans." - "John Lennon"
        return random.choice(self.quotes).strip()