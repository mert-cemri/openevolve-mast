```markdown
# Weather CLI Tool

A Command-Line Interface (CLI) tool to fetch and display the current weather for a given city using the OpenWeatherMap API.

## Overview

The Weather CLI Tool is a simple application that allows users to retrieve current weather information for any city by using the OpenWeatherMap API. This tool is designed to be used in a terminal or command prompt environment.

## Main Functions

- **Fetch Weather Data**: Retrieve current weather data for a specified city.
- **Display Weather Information**: Display the weather description and temperature in Celsius.

## Installation

### Prerequisites

- Python 3.6 or higher
- An API key from OpenWeatherMap

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

## Usage

To use the Weather CLI Tool, follow these steps:

1. **Run the CLI Tool**

   Execute the `main.py` script with the city name as an argument:

   ```bash
   python main.py <city_name>
   ```

   Replace `<city_name>` with the name of the city you want to fetch the weather for.

2. **Example**

   To get the weather for London, run:

   ```bash
   python main.py London
   ```

   This will output the current weather description and temperature in Celsius for London.

## Troubleshooting

- **API Key Error**: If you encounter an error regarding the API key, ensure that the `OPENWEATHERMAP_API_KEY` environment variable is set correctly with a valid API key.
- **Network Issues**: Ensure you have a stable internet connection to fetch data from the OpenWeatherMap API.
- **City Not Found**: If the city name is incorrect or not recognized, the tool will display an error message. Ensure the city name is spelled correctly.

## Documentation

For more detailed information on the OpenWeatherMap API, visit their [official documentation](https://openweathermap.org/api).

```
```