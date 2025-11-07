# Stock Price Checker CLI Application

## Overview

The Stock Price Checker CLI Application is a command-line tool that allows users to check the current stock price and change for a given ticker symbol using the Alpha Vantage API. This application is built using Python and provides a simple and efficient way to access real-time stock data.

## Main Functions

- **Fetch Stock Data:** The application fetches the latest stock data for a given ticker symbol from the Alpha Vantage API.
- **Calculate Change:** It calculates the change in stock price based on the latest and previous data points.
- **Display Information:** The application displays the current stock price and the change in price.

## Prerequisites

Before using the Stock Price Checker CLI Application, you need to have the following:

- Python 3.6 or higher installed on your system.
- An API key from Alpha Vantage. You can obtain this by signing up on the [Alpha Vantage website](https://www.alphavantage.co/support/#api-key).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/stock-price-checker.git
   cd stock-price-checker
   ```

2. **Install Dependencies:**

   The application requires the `requests` library to make HTTP requests. You can install it using pip:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain:

   ```txt
   requests
   ```

3. **Set Environment Variable:**

   Set the `ALPHA_VANTAGE_API_KEY` environment variable with your Alpha Vantage API key. You can do this by running the following command in your terminal:

   ```bash
   export ALPHA_VANTAGE_API_KEY=your_api_key_here
   ```

   Alternatively, you can add this line to your shell configuration file (e.g., `.bashrc`, `.zshrc`) to set the environment variable permanently.

## Usage

1. **Run the Application:**

   You can run the Stock Price Checker CLI Application by executing the following command in your terminal:

   ```bash
   python main.py <ticker_symbol>
   ```

   Replace `<ticker_symbol>` with the ticker symbol of the stock you want to check. For example, to check the stock price for Apple Inc., you would run:

   ```bash
   python main.py AAPL
   ```

2. **View Output:**

   The application will display the current stock price and the change in price for the specified ticker symbol. For example:

   ```
   INFO:root:Current Price for AAPL: $150.75
   INFO:root:Change: $0.50
   ```

## Troubleshooting

- **API Key Not Found:** If you encounter an error indicating that the API key is not found, make sure that you have set the `ALPHA_VANTAGE_API_KEY` environment variable correctly.
- **HTTP Error:** If you encounter an HTTP error, check your API key and network connection.
- **Request Error:** If you encounter a request error, check your network connection.
- **Unexpected Error:** If you encounter an unexpected error, try running the application again later.

## Contributing

We welcome contributions to the Stock Price Checker CLI Application. If you have any ideas for improvements or bug fixes, please feel free to submit a pull request.

## License

The Stock Price Checker CLI Application is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This manual should provide a comprehensive guide for users to install, configure, and use the Stock Price Checker CLI Application effectively.