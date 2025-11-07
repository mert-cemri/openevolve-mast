# Currency Converter CLI

## Overview

The Currency Converter CLI is a simple command-line application that allows users to convert amounts from one currency to another using a predefined set of exchange rates. The exchange rates are stored in a configuration file, making it easy to update them as needed.

## Features

- **User Input:** The user can input the amount, source currency, and target currency.
- **Static Exchange Rates:** Exchange rates are stored in a static JSON configuration file.
- **Error Handling:** The application handles invalid inputs and missing configuration files gracefully.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- `pip` (Python's package installer) should be available.

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/currency-converter-cli.git
   cd currency-converter-cli
   ```

2. **Install Dependencies:**
   This project has no external dependencies, but if you encounter any, you can install them using:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The exchange rates are stored in a JSON file named `exchange_rates.json`. You can modify this file to add or update exchange rates as needed. Here is an example of what the file might look like:

```json
{
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
    "CAD": 1.25
}
```

## Usage

### Running the Application

To run the currency converter, navigate to the project directory and execute the following command:

```bash
python main.py
```

### Input Prompts

1. **Enter the amount:** The user is prompted to enter the amount they wish to convert.
2. **Enter the source currency:** The user is prompted to enter the source currency code (e.g., USD).
3. **Enter the target currency:** The user is prompted to enter the target currency code (e.g., EUR).

### Example

```bash
$ python main.py
Enter the amount: 100
Enter the source currency (e.g., USD): USD
Enter the target currency (e.g., EUR): EUR
100.0 USD is 85.00 EUR
```

### Error Handling

- **Invalid Amount:** If the user enters a non-numeric value for the amount, the application will display an error message.
- **Invalid Currency Code:** If the user enters an invalid currency code, the application will display an error message.
- **Missing Configuration File:** If the `exchange_rates.json` file is missing, the application will display an error message.

## Contributing

We welcome contributions to the Currency Converter CLI. If you have any ideas, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the Currency Converter CLI effectively. If you have any additional requirements or need further customization, feel free to let me know!