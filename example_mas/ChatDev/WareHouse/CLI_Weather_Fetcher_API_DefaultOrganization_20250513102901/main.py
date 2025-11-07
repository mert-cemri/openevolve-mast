'''
Main application file that implements a CLI tool to fetch and display weather data for a given city.
'''
import argparse
from weather_api import get_weather_data
def fetch_weather(city_name):
    if city_name:
        weather_data = get_weather_data(city_name)
        if weather_data:
            display_weather(weather_data)
        else:
            print("Error: Could not fetch weather data.")
    else:
        print("Input Error: Please enter a city name.")
def display_weather(weather_data):
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather_info = f"Weather: {description}\nTemperature: {temp}°C\nHumidity: {humidity}%"
    print(weather_info)
def main():
    parser = argparse.ArgumentParser(description="Fetch and display the current weather for a given city.")
    parser.add_argument('city', type=str, help='Name of the city to fetch weather for')
    args = parser.parse_args()
    fetch_weather(args.city)
if __name__ == "__main__":
    main()