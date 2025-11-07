'''
Handles command-line interface for the stock price checker application.
'''
import argparse
from stock_price_checker import StockPriceChecker
class CLI:
    def run(self):
        parser = argparse.ArgumentParser(description='Check stock price via CLI')
        parser.add_argument('ticker', type=str, help='Ticker symbol of the stock')
        args = parser.parse_args()
        checker = StockPriceChecker()
        try:
            price, change = checker.get_current_price(args.ticker)
            print(f"Current price of {args.ticker}: ${price:.2f}")
            print(f"Change: ${change:.2f}")
        except ValueError as e:
            print(e)