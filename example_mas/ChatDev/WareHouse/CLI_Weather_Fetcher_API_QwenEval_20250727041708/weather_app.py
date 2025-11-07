'''
Handles the logic for fetching and parsing weather data from the OpenWeatherMap API.
'''
import requests
class WeatherFetcher:
    def __init__(self, api_key):
        '''
        Initializes the WeatherFetcher with an API key and sets the base URL for the OpenWeatherMap API.
        :param api_key: str - API key for OpenWeatherMap
        '''
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
    def fetch_weather(self, city_name):
        '''
        Fetches weather data for the specified city from the OpenWeatherMap API.
        :param city_name: str - Name of the city to fetch weather data for
        :return: dict - JSON response from the API
        '''
        complete_url = f"{self.base_url}appid={self.api_key}&q={city_name}&units=metric"
        try:
            response = requests.get(complete_url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                return {"cod": 404, "message": "City not found"}
            else:
                return {"cod": response.status_code, "message": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as err:
            return {"cod": 500, "message": f"Error occurred: {err}"}
    def parse_weather_data(self, data):
        '''
        Parses the weather data from the API response and returns a formatted string.
        :param data: dict - JSON response from the API
        :return: str - Formatted weather information
        '''
        if data["cod"] == 200:
            main_data = data["main"]
            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_description = data["weather"][0]["description"]
            return f"Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description}"
        else:
            return f"Error: {data.get('message', 'City Not Found')}"