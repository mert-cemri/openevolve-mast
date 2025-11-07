# Date Validation Software

This software provides a function to validate a given date string based on specific rules. It ensures that the date string is in the correct format and adheres to the rules regarding valid days and months.

## Main Function

The main function provided by this software is `valid_date(date)`. This function checks if a given date string is valid based on the following criteria:

1. The date string is not empty.
2. The date string is in the format `mm-dd-yyyy`.
3. The month is between 1 and 12.
4. The day is valid for the given month:
   - 31 days for months 1, 3, 5, 7, 8, 10, 12.
   - 30 days for months 4, 6, 9, 11.
   - 28 or 29 days for month 2, depending on whether it is a leap year.

## Installation

This software does not require any external dependencies. It uses Python's built-in libraries. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the `valid_date` function by importing it into your Python script or by running it directly in a Python environment.

   Example usage:
   ```python
   from main import valid_date

   print(valid_date('03-11-2000'))  # Output: True
   print(valid_date('15-01-2012'))  # Output: False
   print(valid_date('04-0-2040'))   # Output: False
   print(valid_date('06-04-2020'))  # Output: True
   print(valid_date('06/04/2020'))  # Output: False
   ```

## Documentation

The function is straightforward and does not require additional configuration. It is designed to be used in any Python environment. If you encounter any issues or have questions, please refer to the comments within the `main.py` file for further clarification on the implementation details.