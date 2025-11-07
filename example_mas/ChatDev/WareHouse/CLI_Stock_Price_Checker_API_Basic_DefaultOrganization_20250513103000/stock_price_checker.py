'''
Provides functionality to fetch stock prices using a public financial API.
'''
import requests
class StockPriceChecker:
    API_URL = "https://www.alphavantage.co/query"
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    def get_current_price(self, ticker):
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": ticker,
            "interval": "1min",
            "apikey": self.API_KEY
        }
        response = requests.get(self.API_URL, params=params)
        data = response.json()
        # Check for API error message
        if "Error Message" in data:
            raise ValueError("Invalid ticker symbol or API error.")
        try:
            time_series = data['Time Series (1min)']
            # Get the most recent timestamp
            last_refreshed = sorted(time_series.keys())[0]
            last_price = float(time_series[last_refreshed]['4. close'])
            # Get the previous timestamp
            previous_timestamp = sorted(time_series.keys())[1]
            previous_close = float(time_series[previous_timestamp]['4. close'])
            price_change = last_price - previous_close
            return last_price, price_change
        except (KeyError, IndexError):
            raise ValueError("Unexpected response format or API limit reached.")