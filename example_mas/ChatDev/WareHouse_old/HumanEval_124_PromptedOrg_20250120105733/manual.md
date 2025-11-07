# Date Validation Software

This software provides a function to validate date strings based on specific rules. It ensures that the date is in the correct format and checks the validity of the day, month, and year components.

## Main Function

### `valid_date(date)`

- **Purpose**: Validates a given date string and returns `True` if the date is valid according to the specified rules, otherwise `False`.
- **Parameters**: 
  - `date` (string): The date string to be validated.
- **Returns**: 
  - `True` if the date is valid.
  - `False` if the date is invalid.

### Validation Rules

1. The date string must not be empty.
2. The date must be in the format `mm-dd-yyyy`.
3. The month must be between 1 and 12.
4. The day must be valid for the given month:
   - 31 days for months 1, 3, 5, 7, 8, 10, 12.
   - 30 days for months 4, 6, 9, 11.
   - 28 or 29 days for month 2 (February), depending on whether it is a leap year.

## Installation

No external dependencies are required for this project. The function is implemented in pure Python.

## Usage

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can use the function in your Python scripts by importing it.

   ```python
   from main import valid_date

   # Example usage
   print(valid_date('03-11-2000'))  # Output: True
   print(valid_date('15-01-2012'))  # Output: False
   ```

## Examples

- `valid_date('03-11-2000')` returns `True` because the date is valid.
- `valid_date('15-01-2012')` returns `False` because the month is invalid.
- `valid_date('04-0-2040')` returns `False` because the day is invalid.
- `valid_date('06-04-2020')` returns `True` because the date is valid.
- `valid_date('06/04/2020')` returns `False` because the format is incorrect.

## Documentation

For further details and examples, please refer to the code comments within the `main.py` file. The function is self-contained and does not require any additional setup or libraries.