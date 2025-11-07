# Date Validation Software Manual

Welcome to the Date Validation Software! This software provides a simple yet effective function to validate date strings based on specific rules. This manual will guide you through the main functions of the software, how to install it, and how to use it.

## Main Function

The primary function of this software is `valid_date(date)`. This function checks if a given date string is valid based on the following criteria:

1. **Non-Empty String**: The date string must not be empty.
2. **Date Format**: The date must be in the format `mm-dd-yyyy`.
3. **Valid Month**: The month must be between 1 and 12.
4. **Valid Day**: 
   - For months 1, 3, 5, 7, 8, 10, 12, the day must be between 1 and 31.
   - For months 4, 6, 9, 11, the day must be between 1 and 30.
   - For month 2, the day must be between 1 and 29 in a leap year and between 1 and 28 otherwise.
5. **Digit Check**: All parts of the date (month, day, year) must be numeric.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.
2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

## How to Use

1. **Run the Script**: You can run the script directly from your terminal or command prompt using Python. Use the following command:

   ```bash
   python main.py
   ```

2. **Function Usage**: You can use the `valid_date` function within your Python scripts by importing it from `main.py`. Here is an example of how to use it:

   ```python
   from main import valid_date

   # Example usage
   print(valid_date('03-11-2000'))  # Output: True
   print(valid_date('15-01-2012'))  # Output: False
   print(valid_date('04-0-2040'))   # Output: False
   print(valid_date('06-04-2020'))  # Output: True
   print(valid_date('06/04/2020'))  # Output: False
   ```

## Conclusion

This Date Validation Software is a straightforward tool designed to help you validate date strings efficiently. With no external dependencies, it is easy to integrate into your existing Python projects. If you have any questions or need further assistance, feel free to reach out to our support team. Enjoy using the software!