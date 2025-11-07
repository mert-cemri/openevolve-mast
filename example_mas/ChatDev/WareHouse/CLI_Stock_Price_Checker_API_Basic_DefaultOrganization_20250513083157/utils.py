'''
Utility functions for the stock price checker application.
'''
import requests
def fetch_data_from_api(api_url, params):
    '''
    Makes an API request and returns the response data.
    '''
    response = requests.get(api_url, params=params)
    return response.json()