'''
Main entry point for the stock price checker CLI application.
Parses command-line arguments and displays the stock price and change.
'''
import argparse
from stock_checker import StockChecker
import logging
logging.basicConfig(level=logging.INFO)
def main():
    parser = argparse.ArgumentParser(description='Check the current stock price for a given ticker symbol.')
    parser.add_argument('ticker', type=str, help='The ticker symbol of the stock (e.g., AAPL)')
    args = parser.parse_args()
    stock_checker = StockChecker()
    stock_data = stock_checker.get_stock_data(args.ticker)
    if stock_data:
        logging.info(f"Current Price for {args.ticker}: ${stock_data['current_price']:.2f}")
        logging.info(f"Change: ${stock_data['change']:.2f}")
    else:
        logging.error(f"Failed to retrieve stock data for {args.ticker}")
if __name__ == '__main__':
    main()