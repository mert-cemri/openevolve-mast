```markdown
# Stock Price Checker

A Command-Line Interface (CLI) and Graphical User Interface (GUI) application to check the current stock price for a given ticker symbol using a public financial API.

## Overview

The Stock Price Checker application allows users to fetch and display the current stock price and its change for a given ticker symbol. It supports both CLI and GUI modes, providing flexibility for different user preferences.

## Features

- **Command-Line Interface (CLI):** Quickly check stock prices directly from your terminal.
- **Graphical User Interface (GUI):** A user-friendly interface for those who prefer a visual interaction.
- **Real-time Data:** Fetches the latest stock prices using the Alpha Vantage API.
- **Price Change Calculation:** Displays the change in price compared to the previous close.

## Installation

### Prerequisites

- Python 3.x
- An API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) (free registration required).

### Quick Install

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**

   Replace `YOUR_API_KEY` in `stock_price_checker.py` with your actual Alpha Vantage API key.

## Usage

### Command-Line Interface (CLI)

1. **Run the application in CLI mode:**

   ```bash
   python main.py <ticker-symbol>
   ```

   Replace `<ticker-symbol>` with the stock ticker you want to check (e.g., `AAPL` for Apple Inc.).

2. **Example:**

   ```bash
   python main.py AAPL
   ```

   This will display the current price and change for Apple Inc.

### Graphical User Interface (GUI)

1. **Run the application in GUI mode:**

   ```bash
   python main.py --gui
   ```

2. **Using the GUI:**

   - Enter the ticker symbol in the provided text field.
   - Click "Check Price" to fetch and display the current stock price and change.

## Troubleshooting

- **Invalid Ticker Symbol:** Ensure the ticker symbol is correct and exists on the stock exchange.
- **API Limit Reached:** Alpha Vantage has a limit on the number of API requests per minute. Consider upgrading your API plan if you frequently hit this limit.
- **Unexpected Errors:** Check your internet connection and ensure your API key is correctly set up.

## Documentation

For further information and updates, please refer to the official documentation or contact support.

```
```