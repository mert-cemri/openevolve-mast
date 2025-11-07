```markdown
# CLI Currency Converter

A simple command-line interface (CLI) application for converting currencies using predefined static exchange rates.

## Overview

The CLI Currency Converter allows users to convert an amount from one currency to another using a predefined set of exchange rates stored in a configuration file. The application is written in Python and is designed to be easy to use and extend.

## Main Features

- **Currency Conversion**: Convert an amount from a source currency to a target currency using predefined exchange rates.
- **Static Exchange Rates**: Exchange rates are stored in a configuration file (`config.json`) and are relative to USD.
- **Error Handling**: Provides user-friendly error messages for invalid inputs or unsupported currencies.

## Quick Install

### Prerequisites

- Python 3.6 or higher

### Installation Steps

1. **Clone the Repository**: Clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up the Environment**: Ensure you have Python 3.6 or higher installed. You can check your Python version with:
   ```bash
   python --version
   ```

3. **Install Dependencies**: Install the required dependencies using pip.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Prepare the Configuration File**: Ensure the `config.json` file is present in the same directory as the application. This file contains the exchange rates:
   ```json
   {
       "USD": 1.0,
       "EUR": 0.85,
       "JPY": 110.0,
       "GBP": 0.75,
       "AUD": 1.35
   }
   ```

2. **Run the Application**: Execute the `main.py` script to start the currency converter.
   ```bash
   python main.py
   ```

3. **Input Details**: Follow the prompts to input the amount, source currency, and target currency. The application will output the converted amount.

   Example interaction:
   ```
   Enter amount: 100
   Enter source currency: USD
   Enter target currency: EUR
   Converted amount: 85.00 EUR
   ```

## Error Handling

- **Invalid Amount**: If a non-numeric value is entered for the amount, the application will display an error message.
- **Unsupported Currency**: If the source or target currency is not supported (i.e., not listed in `config.json`), an error message will be shown.
- **Configuration File Issues**: If the `config.json` file is missing or contains invalid JSON, the application will alert the user.

## Extending the Application

To add more currencies or update exchange rates, simply modify the `config.json` file with the new rates. Ensure the rates are relative to USD for consistency.

## Documentation

For further details on the application's architecture and code, please refer to the source code comments in `main.py` and `converter.py`.

```
