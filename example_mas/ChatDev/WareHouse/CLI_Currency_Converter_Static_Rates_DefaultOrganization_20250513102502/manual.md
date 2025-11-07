```markdown
# CLI Currency Converter

A simple command-line interface (CLI) application for converting currencies using a predefined set of exchange rates.

## Introduction

The CLI Currency Converter allows users to convert an amount from one currency to another using static exchange rates stored in a configuration file. This tool is useful for quick currency conversions without the need for real-time exchange rate updates.

## Main Functions

- **Currency Conversion**: Convert an amount from a source currency to a target currency using predefined exchange rates.
- **Static Exchange Rates**: The application uses a static set of exchange rates stored in a `config.json` file.

## Quick Install

### Prerequisites

- Python 3.6 or higher

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   Install the required Python version by ensuring your environment is set up with Python 3.6 or higher. You can create a virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Ensure the Python version is correct:

   ```bash
   python --version
   ```

   The `requirements.txt` file specifies the minimum Python version required:

   ```text
   python_version >= 3.6
   ```

## How to Use

1. **Run the Application**

   Execute the main script to start the currency converter:

   ```bash
   python main.py
   ```

2. **Input Details**

   - Enter the amount you wish to convert.
   - Enter the source currency code (e.g., USD, EUR).
   - Enter the target currency code (e.g., JPY, GBP).

3. **View Results**

   The application will display the converted amount in the target currency.

## Configuration

The exchange rates are stored in a `config.json` file. You can modify this file to update the exchange rates as needed:

```json
{
    "USD": 1.0,
    "EUR": 0.85,
    "JPY": 110.0,
    "GBP": 0.75,
    "AUD": 1.35
}
```

## Error Handling

- If an invalid currency code is entered, the application will raise a `ValueError` with the message "Invalid currency code."
- Ensure that the `config.json` file is correctly formatted and contains valid exchange rates.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided within the codebase.

```
