'''
Main entry point for the Weather CLI Application.
'''
import argparse
import os
from weather_api import WeatherAPI
def main():
    parser = argparse.ArgumentParser(description='Fetch and display the current weather for a given city.')
    parser.add_argument('city', type=str, help='Name of the city to fetch weather for')
    args = parser.parse_args()
    # Retrieve the API key from an environment variable
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        print("Error: API key not found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
        return
    api = WeatherAPI(api_key=api_key)
    try:
        weather_data = api.get_weather(args.city)
        display_weather(weather_data)
    except Exception as e:
        print(f"Error: {e}")
def display_weather(weather_data):
    if weather_data:
        weather_info = f"Weather in {weather_data['name']}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°C"
        print(weather_info)
    else:
        print("No data available.")
if __name__ == "__main__":
    main()