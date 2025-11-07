```markdown
# Stock Price Checker CLI Application

Welcome to the Stock Price Checker CLI Application! This application allows you to check the current stock price and its change for a given ticker symbol using the Alpha Vantage API.

## Main Functions

- **Fetch Current Stock Price**: Retrieve the latest stock price for a specified ticker symbol.
- **Calculate Price Change**: Compute the change in stock price from the previous closing price.
- **User Interaction via CLI**: Interact with the application through a command-line interface, providing a seamless user experience.

## Quick Install

To get started with the Stock Price Checker CLI Application, follow these steps to set up your environment:

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Ensure you have Python installed, then install the required dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**: Obtain an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and set it as an environment variable.

   ```bash
   export ALPHA_VANTAGE_API_KEY='your_api_key_here'
   ```

   Alternatively, you can enter your API key when prompted by the application.

## How to Use

1. **Run the Application**: Start the CLI application by executing the main script.

   ```bash
   python main.py
   ```

2. **Interact with the CLI**: Once the application is running, you will be greeted with a welcome message. You can then enter a ticker symbol to check its current stock price and change.

   - **Enter Ticker Symbol**: Type the ticker symbol of the stock you want to check and press Enter.
   - **View Results**: The application will display the current price and the change from the previous close.
   - **Exit the Application**: Type 'exit' to quit the application.

## Example Usage

```bash
Welcome to the Stock Price Checker CLI!
Enter the ticker symbol (or 'exit' to quit): AAPL
Current price of AAPL: $145.09
Change: $0.50
Enter the ticker symbol (or 'exit' to quit): exit
Exiting the application.
```

## Troubleshooting

- **Invalid Ticker Symbol**: If you enter an invalid ticker symbol, the application will notify you with an error message.
- **API Call Frequency Limit**: If you exceed the API call frequency limit, please wait and try again later.

## Documentation

For further details and documentation, please refer to the source code and comments within the scripts. The code is structured to be intuitive and easy to follow.

Enjoy using the Stock Price Checker CLI Application!
```