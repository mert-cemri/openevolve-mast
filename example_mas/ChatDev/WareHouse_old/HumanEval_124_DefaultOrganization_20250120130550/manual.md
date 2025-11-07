# Date Validation Software

This software provides a function to validate date strings based on specific rules. It is designed to ensure that date inputs adhere to a specified format and range of values.

## Main Function

### `valid_date(date)`

- **Purpose**: Validates a given date string and returns `True` if the date is valid, otherwise `False`.
- **Validation Rules**:
  1. The date string must not be empty.
  2. The date must be in the format `mm-dd-yyyy`.
  3. The month must be between 1 and 12.
  4. The day must be valid for the given month:
     - 1 to 31 for months 1, 3, 5, 7, 8, 10, 12
     - 1 to 30 for months 4, 6, 9, 11
     - 1 to 29 for month 2
- **Parameters**: 
  - `date` (str): A string representing the date.
- **Returns**: 
  - `bool`: `True` if the date is valid, `False` otherwise.

## Installation

This project does not require any external dependencies. You can simply download the `main.py` file and run it with Python.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: 
   - Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Script**:
   - Execute the script using Python:
     ```bash
     python main.py
     ```

## Usage

To use the `valid_date` function, you can import it into your Python script and call it with a date string as an argument. Here is an example:

```python
from main import valid_date

# Example usage
print(valid_date('03-11-2000'))  # Output: True
print(valid_date('15-01-2012'))  # Output: False
print(valid_date('04-0-2040'))   # Output: False
print(valid_date('06-04-2020'))  # Output: True
print(valid_date('06/04/2020'))  # Output: False
```

## Documentation

For further details on the function and its implementation, please refer to the comments within the `main.py` file. The code is self-explanatory and includes detailed comments to help you understand the logic behind the date validation process.

Feel free to reach out for support or further inquiries regarding the software.