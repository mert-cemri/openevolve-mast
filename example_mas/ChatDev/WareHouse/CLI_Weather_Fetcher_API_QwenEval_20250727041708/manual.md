# Weather CLI Tool User Manual

## Overview

The Weather CLI Tool is a command-line interface application that allows users to fetch and display the current weather for a specified city using the OpenWeatherMap API. This tool is designed to be simple and easy to use, providing essential weather information such as temperature, pressure, humidity, and a brief description of the weather conditions.

## Main Functions

- **Fetch Weather Data:** The tool connects to the OpenWeatherMap API to retrieve the latest weather data for the specified city.
- **Parse Weather Data:** The tool processes the API response to extract relevant weather information.
- **Display Weather Information:** The tool presents the weather data in a user-friendly format.

## Prerequisites

- Python 3.6 or higher
- An API key from OpenWeatherMap (https://openweathermap.org/api)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/weather-cli-tool.git
   cd weather-cli-tool
   ```

2. **Install Dependencies:**
   The tool requires the `requests` library. You can install it using pip:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file specifies the exact version of `requests` to ensure compatibility:
   ```
   requests==2.25.1
   ```

## Configuration

Before using the tool, you need to set your OpenWeatherMap API key as an environment variable. This can be done in your terminal:

- **Linux/Mac:**
  ```bash
  export OPENWEATHERMAP_API_KEY=your_api_key_here
  ```

- **Windows:**
  ```bash
  set OPENWEATHERMAP_API_KEY=your_api_key_here
  ```

## Usage

To use the Weather CLI Tool, open your terminal and run the following command:

```bash
python main.py <city_name>
```

Replace `<city_name>` with the name of the city for which you want to fetch the weather information.

### Example

To fetch the weather for London, you would run:

```bash
python main.py London
```

### Output

The tool will display the current weather information in the following format:

```
Temperature: 15°C
Pressure: 1012 hPa
Humidity: 81%
Description: light rain
```

## Error Handling

- **City Not Found:** If the specified city is not found, the tool will display an error message:
  ```
  Error: City not found
  ```

- **API Errors:** If there is an issue with the API request (e.g., network error, invalid API key), the tool will display an appropriate error message.

## Troubleshooting

- **API Key Not Set:** If the `OPENWEATHERMAP_API_KEY` environment variable is not set, the tool will prompt you to set it:
  ```
  Please set the OPENWEATHERMAP_API_KEY environment variable.
  ```

- **Incorrect API Key:** If the provided API key is invalid, the tool will display an error message:
  ```
  Error: Unauthorized
  ```

## Contributing

We welcome contributions to the Weather CLI Tool! If you have any ideas for improvements or bug fixes, please feel free to open an issue or submit a pull request on our GitHub repository.

## License

The Weather CLI Tool is licensed under the MIT License. See the `LICENSE` file for more information.

---

This manual provides a comprehensive guide for users to install, configure, and use the Weather CLI Tool effectively. If you have any questions or need further assistance, please don't hesitate to reach out.