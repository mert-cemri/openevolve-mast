# Date Validation Software

This software provides a function to validate date strings based on specific rules. It is designed to ensure that a given date string is in the correct format and adheres to logical constraints regarding days and months.

## Main Functionality

The main function provided by this software is `valid_date(date)`. This function checks if a given date string is valid based on the following criteria:

1. The date string is not empty.
2. The date format must be `mm-dd-yyyy`.
3. The month must be between 1 and 12.
4. The day must be valid for the given month:
   - 31 days for months 1, 3, 5, 7, 8, 10, 12.
   - 30 days for months 4, 6, 9, 11.
   - 29 days for month 2.

### Example Usage

```python
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone the repository or download the `main.py` file containing the `valid_date` function.

## How to Use

1. Open the `main.py` file in your preferred Python IDE or text editor.
2. Use the `valid_date(date)` function by passing a date string in the format `mm-dd-yyyy`.
3. The function will return `True` if the date is valid and `False` otherwise.

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The code is documented to explain the logic behind each validation step.

This software is a simple utility for validating date strings and can be integrated into larger applications where date validation is required.