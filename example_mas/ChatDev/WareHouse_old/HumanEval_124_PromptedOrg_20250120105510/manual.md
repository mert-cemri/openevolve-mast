# Date Validation Software

This software provides a function to validate date strings based on specific rules. It is designed to ensure that the date is in the correct format and adheres to the rules for valid days and months.

## Main Functionality

The main function provided by this software is `valid_date(date)`. This function checks if a given date string is valid based on the following criteria:

1. The date string is not empty.
2. The date should be in the format `mm-dd-yyyy`.
3. The month should be between 1 and 12.
4. The day should be valid for the given month:
   - For months 1, 3, 5, 7, 8, 10, 12, the day should be between 1 and 31.
   - For months 4, 6, 9, 11, the day should be between 1 and 30.
   - For month 2 (February), the day should be between 1 and 29 if it is a leap year, otherwise between 1 and 28.

## Quick Install

There are no external dependencies required for this software. You can directly use the provided Python code in your environment.

## How to Use

1. **Copy the Code**: Copy the code provided in the `main.py` file into your Python environment.

2. **Use the Function**: Call the `valid_date(date)` function with a date string as an argument to check its validity.

   ```python
   # Example usage
   print(valid_date('03-11-2000'))  # Output: True
   print(valid_date('15-01-2012'))  # Output: False
   print(valid_date('04-0-2040'))   # Output: False
   print(valid_date('06-04-2020'))  # Output: True
   print(valid_date('06/04/2020'))  # Output: False
   ```

## Documentation

The function `valid_date(date)` is documented within the code. It includes a helper function `is_leap_year(year)` to determine if a given year is a leap year, which is used for validating February dates.

For further assistance or questions, please contact our support team.