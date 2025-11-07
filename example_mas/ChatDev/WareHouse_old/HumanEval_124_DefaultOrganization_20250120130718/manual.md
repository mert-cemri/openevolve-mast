# Date Validation Software

This software provides a function to validate date strings based on specific rules. It is designed to ensure that date strings are in the correct format and adhere to the constraints of the Gregorian calendar.

## Main Function

The primary function of this software is `valid_date(date)`, which checks whether a given date string is valid according to the following rules:

1. **Non-Empty String**: The date string must not be empty.
2. **Correct Format**: The date should be in the format `mm-dd-yyyy`.
3. **Valid Month**: The month must be a number between 1 and 12.
4. **Valid Day**: 
   - For months 1, 3, 5, 7, 8, 10, 12, the day must be between 1 and 31.
   - For months 4, 6, 9, 11, the day must be between 1 and 30.
   - For month 2, the day must be between 1 and 29.
5. **Valid Year**: The year must be a valid number.

### Example Usage

```python
print(valid_date('03-11-2000'))  # Output: True
print(valid_date('15-01-2012'))  # Output: False
print(valid_date('04-0-2040'))   # Output: False
print(valid_date('06-04-2020'))  # Output: True
print(valid_date('06/04/2020'))  # Output: False
```

## Installation

This project does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Project Directory**: 
   ```bash
   cd <project-directory>
   ```
3. **Run the Code**: You can run the `main.py` file directly to test the `valid_date` function.

## How to Use

1. **Import the Function**: If you want to use the `valid_date` function in another Python script, you can import it as follows:
   ```python
   from main import valid_date
   ```

2. **Call the Function**: Pass a date string to the `valid_date` function to check its validity.
   ```python
   is_valid = valid_date('03-11-2000')
   print(is_valid)  # Output: True
   ```

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The code is documented to explain the logic behind each validation step.

This software is designed to be simple and efficient, ensuring that date strings are validated correctly without any unnecessary complexity.