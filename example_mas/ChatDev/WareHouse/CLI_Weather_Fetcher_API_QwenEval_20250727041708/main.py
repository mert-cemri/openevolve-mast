'''
Main entry point for the weather CLI tool.
Handles command-line arguments and interacts with the WeatherFetcher class to display weather information.
'''
from weather_app import WeatherFetcher
import argparse
import os
def main():
    parser = argparse.ArgumentParser(description="Fetch and display the current weather for a given city.")
    parser.add_argument("city", type=str, help="The name of the city")
    args = parser.parse_args()
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        print("Please set the OPENWEATHERMAP_API_KEY environment variable.")
        return
    weather_fetcher = WeatherFetcher(api_key)
    weather_data = weather_fetcher.fetch_weather(args.city)
    parsed_data = weather_fetcher.parse_weather_data(weather_data)
    print(parsed_data)
if __name__ == "__main__":
    main()