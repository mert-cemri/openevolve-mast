# Prime Length Checker

This software provides a simple utility to determine if the length of a given string is a prime number. It includes a function `prime_length` that takes a string as input and returns `True` if the string's length is a prime number, and `False` otherwise.

## Main Functions

### `prime_length(string)`

- **Description**: This function checks if the length of the input string is a prime number.
- **Parameters**: 
  - `string` (str): The input string whose length is to be checked.
- **Returns**: 
  - `bool`: Returns `True` if the length of the string is a prime number, otherwise returns `False`.
- **Examples**:
  - `prime_length('Hello')` returns `True`
  - `prime_length('abcdcba')` returns `True`
  - `prime_length('kittens')` returns `True`
  - `prime_length('orange')` returns `False`

## Installation

This software does not require any external dependencies, so you can directly run the code without installing additional packages.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can run the code using Python. Open a Python interpreter or create a script to use the `prime_length` function.

   ```python
   from main import prime_length

   # Example usage
   print(prime_length('Hello'))  # Output: True
   print(prime_length('orange')) # Output: False
   ```

## Additional Information

- **No External Dependencies**: This software is self-contained and does not require any additional Python packages.
- **Python Version**: Ensure you have Python installed on your machine. This code is compatible with Python 3.x.

This utility is designed to be simple and efficient, providing a quick way to check the primality of string lengths for various applications.