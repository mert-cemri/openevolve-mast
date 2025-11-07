'''
Module to fetch stock data from the Alpha Vantage API and compute the change.
'''
import requests
import os
from config import BASE_URL
class StockChecker:
    def __init__(self):
        self.api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")
        self.base_url = BASE_URL
    def get_stock_data(self, ticker):
        try:
            url = f"{self.base_url}function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={self.api_key}"
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.json()
            if 'Time Series (1min)' not in data:
                print(f"Error fetching data for ticker '{ticker}'. Please check the ticker symbol.")
                return None
            time_series = data['Time Series (1min)']
            times = sorted(time_series.keys(), reverse=True)
            if len(times) < 2:
                print(f"Insufficient data to calculate change for ticker '{ticker}'.")
                return None
            latest_time = times[0]
            latest_data = time_series[latest_time]
            current_price = float(latest_data['4. close'])
            previous_time = times[1]
            previous_data = time_series[previous_time]
            previous_price = float(previous_data['4. close'])
            change = current_price - previous_price
            return {
                'current_price': current_price,
                'change': change
            }
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}. Please check your API key and network connection.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}. Please check your network connection.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again later.")
            return None