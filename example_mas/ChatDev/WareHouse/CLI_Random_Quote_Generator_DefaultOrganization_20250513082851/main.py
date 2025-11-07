'''
Main entry point for the Quote Display CLI application.
'''
import sys
from quote_manager import QuoteManager
def main():
    '''
    Main function to display a random quote from the command line.
    '''
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_quotes_file>")
        return
    file_path = sys.argv[1]
    quote_manager = QuoteManager()
    quote_manager.load_quotes(file_path)
    print(quote_manager.get_random_quote())
if __name__ == "__main__":
    main()