'''
Handles stock price retrieval using a public financial API.
'''
import requests
class StockPriceChecker:
    def __init__(self, api_key):
        '''
        Initializes the StockPriceChecker with the given API key.
        '''
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"
    def get_stock_price(self, ticker):
        '''
        Fetches the current stock price and change for the given ticker symbol.
        '''
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": ticker,
            "interval": "1min",
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        if "Error Message" in data:
            raise ValueError("Invalid ticker symbol.")
        if "Note" in data:
            raise ValueError("API call frequency limit reached. Please try again later.")
        try:
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            time_series = data["Time Series (1min)"]
            latest_data = time_series[last_refreshed]
            current_price = float(latest_data["4. close"])
            # Get the previous timestamp to calculate the change
            previous_timestamp = sorted(time_series.keys())[-2]
            previous_data = time_series[previous_timestamp]
            previous_close = float(previous_data["4. close"])
            change = current_price - previous_close
            return current_price, change
        except KeyError:
            raise ValueError("Unexpected API response format.")