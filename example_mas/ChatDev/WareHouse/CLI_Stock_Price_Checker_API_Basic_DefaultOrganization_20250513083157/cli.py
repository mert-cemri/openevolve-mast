'''
Handles the command line interface for user interaction.
'''
import os
from stock_price_checker import StockPriceChecker
class CLI:
    def __init__(self):
        '''
        Initializes the CLI with necessary configurations.
        '''
        self.api_key = os.getenv("ALPHA_VANTAGE_API_KEY") or input("Enter your Alpha Vantage API key: ").strip()
        self.stock_checker = StockPriceChecker(self.api_key)
    def run(self):
        '''
        Main method to run the CLI application.
        '''
        print("Welcome to the Stock Price Checker CLI!")
        while True:
            ticker = input("Enter the ticker symbol (or 'exit' to quit): ").strip()
            if ticker.lower() == 'exit':
                print("Exiting the application.")
                break
            try:
                price, change = self.stock_checker.get_stock_price(ticker)
                print(f"Current price of {ticker}: ${price:.2f}")
                print(f"Change: ${change:.2f}")
            except ValueError as e:
                print(e)