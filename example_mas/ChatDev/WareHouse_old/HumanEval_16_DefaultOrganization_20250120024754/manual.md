# Distinct Character Counter

This software provides a simple function to count the number of distinct characters in a given string, ignoring case sensitivity. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is:

### `count_distinct_characters(string: str) -> int`

- **Description**: This function takes a string as input and returns the number of distinct characters in the string, regardless of their case. For example, 'A' and 'a' are considered the same character.

- **Usage Examples**:
  ```python
  >>> count_distinct_characters('xyzXYZ')
  3
  >>> count_distinct_characters('Jerry')
  4
  ```

## Installation

There are no external dependencies required for this software. It is implemented in pure Python. To use it, simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the function.

## How to Use

1. **Open a Python environment**: You can use any Python IDE or a simple command-line interface.

2. **Import the function**: If you have saved the `main.py` file in your working directory, you can import the function using:
   ```python
   from main import count_distinct_characters
   ```

3. **Call the function**: Pass a string to the function to get the count of distinct characters.
   ```python
   result = count_distinct_characters('YourStringHere')
   print(result)
   ```

## Documentation

The function is straightforward and does not require additional setup or configuration. It is designed to be easily integrated into larger projects or used as a standalone utility for counting distinct characters in strings.

For further assistance or inquiries, please contact our support team.