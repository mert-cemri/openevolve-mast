'''
WeatherApp class for managing the GUI and user interactions.
'''
import tkinter as tk
from tkinter import messagebox
from weather_api import WeatherAPI
class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather App")
        self.api = WeatherAPI(api_key="YOUR_API_KEY_HERE")
        self.city_label = tk.Label(self.root, text="Enter City:")
        self.city_label.pack()
        self.city_entry = tk.Entry(self.root)
        self.city_entry.pack()
        self.fetch_button = tk.Button(self.root, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
    def fetch_weather(self):
        city = self.city_entry.get()
        if city:
            try:
                weather_data = self.api.get_weather(city)
                self.display_weather(weather_data)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter a city name.")
    def display_weather(self, weather_data):
        if weather_data:
            weather_info = f"Weather in {weather_data['name']}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°C"
            self.result_label.config(text=weather_info)
        else:
            self.result_label.config(text="No data available.")
    def run(self):
        self.root.mainloop()