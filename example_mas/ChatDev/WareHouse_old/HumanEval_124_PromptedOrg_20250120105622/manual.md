# Date Validation Software

This software provides a function to validate date strings based on specific rules. It ensures that the date format and values are correct, considering leap years for February.

## Main Function

### `valid_date(date)`

- **Description**: Validates a given date string and returns `True` if the date is valid, otherwise `False`.
- **Parameters**: 
  - `date` (str): The date string to validate.
- **Returns**: 
  - `bool`: `True` if the date is valid, `False` otherwise.

### Validation Rules

1. The date string must not be empty.
2. The date should be in the format: `mm-dd-yyyy`.
3. The month should be between 1 and 12.
4. The number of days should be:
   - Between 1 and 31 for months 1, 3, 5, 7, 8, 10, 12.
   - Between 1 and 30 for months 4, 6, 9, 11.
   - Between 1 and 29 for month 2, considering leap years.

### Examples

- `valid_date('03-11-2000')` returns `True`
- `valid_date('15-01-2012')` returns `False`
- `valid_date('04-0-2040')` returns `False`
- `valid_date('06-04-2020')` returns `True`
- `valid_date('06/04/2020')` returns `False`

## Installation

This project does not require any external dependencies. You can directly use the provided `main.py` file in your Python environment.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.
3. **Run the Function**: You can test the function by importing it into your Python script or interactive shell.

```python
from main import valid_date

# Test the function
print(valid_date('03-11-2000'))  # Output: True
print(valid_date('15-01-2012'))  # Output: False
```

## Documentation

For further information and examples, refer to the comments within the `main.py` file. The function is well-documented to help you understand its usage and functionality.