'''
Handles the command-line interface for displaying a random quote.
'''
import random
from quote_manager import QuoteManager
def main():
    '''
    Main function to execute the CLI tool.
    Initializes the QuoteManager and prints a random quote.
    '''
    quote_manager = QuoteManager()
    quote = quote_manager.get_random_quote()
    print(quote)
if __name__ == "__main__":
    main()