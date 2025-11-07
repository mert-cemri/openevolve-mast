# Weather CLI Tool

A command-line interface (CLI) tool to fetch and display the current weather for a given city using the OpenWeatherMap API.

## Introduction

The Weather CLI Tool is a simple application designed to provide users with real-time weather information for any city they specify. By leveraging the OpenWeatherMap API, this tool fetches and displays weather data, including temperature, humidity, and a brief weather description.

## Main Functions

- **Fetch Weather Data**: Retrieve current weather data for a specified city using the OpenWeatherMap API.
- **Display Weather Information**: Present the weather data in a user-friendly format, including temperature, humidity, and weather description.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- An API key from OpenWeatherMap. You can obtain one by signing up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

### Quick Install

1. **Clone the Repository**

   Clone the repository to your local machine using:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variable**

   Set the `OPENWEATHERMAP_API_KEY` environment variable with your OpenWeatherMap API key:

   - On Windows:

     ```bash
     set OPENWEATHERMAP_API_KEY=your_api_key_here
     ```

   - On macOS/Linux:

     ```bash
     export OPENWEATHERMAP_API_KEY=your_api_key_here
     ```

## How to Use

1. **Run the CLI Tool**

   Execute the main script with the city name as an argument:

   ```bash
   python main.py <city_name>
   ```

   Replace `<city_name>` with the name of the city you want to fetch the weather for.

2. **Example Usage**

   To get the weather for London, run:

   ```bash
   python main.py London
   ```

   This will output the current weather, temperature, and humidity for London.

## Error Handling

- If no city name is provided, the tool will prompt you to enter one.
- If the API key is missing or incorrect, an error message will be displayed.
- Network-related errors such as connection issues or timeouts will be handled gracefully with appropriate error messages.

## Conclusion

The Weather CLI Tool is a straightforward application that provides essential weather information quickly and efficiently. By following the installation and usage instructions, you can easily integrate this tool into your daily routine to stay updated with the latest weather conditions.