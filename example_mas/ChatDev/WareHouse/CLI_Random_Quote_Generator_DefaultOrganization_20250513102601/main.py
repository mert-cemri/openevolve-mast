'''
This script implements a CLI tool that displays a random quote from a predefined list of quotes stored in a text file.
'''
import random
class QuoteManager:
    '''
    Manages the retrieval of quotes from a file and provides a random quote.
    '''
    def __init__(self, file_path):
        '''
        Initializes the QuoteManager with the path to the quotes file.
        :param file_path: Path to the text file containing quotes.
        '''
        self.file_path = file_path
        self.quotes = self._load_quotes()
    def _load_quotes(self):
        '''
        Loads quotes from the specified file.
        :return: A list of quotes.
        '''
        with open(self.file_path, 'r') as file:
            quotes = file.readlines()
        return [quote.strip() for quote in quotes if quote.strip()]
    def get_random_quote(self):
        '''
        Returns a random quote from the list of quotes.
        :return: A random quote as a string.
        '''
        return random.choice(self.quotes)
def main():
    '''
    Main function to execute the CLI tool.
    '''
    quote_manager = QuoteManager('quotes.txt')
    print("Here's a random quote for you:")
    print(quote_manager.get_random_quote())
if __name__ == "__main__":
    main()