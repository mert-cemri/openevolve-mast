manual.md

```
# Hexadecimal Prime Digit Counter

This software provides a function to count the number of prime hexadecimal digits in a given string. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this software is `hex_key`, which takes a string representing a hexadecimal number and returns the count of prime hexadecimal digits within that string. The prime hexadecimal digits considered are: 2, 3, 5, 7, B (11 in decimal), and D (13 in decimal).

### Function Definition

```python
def hex_key(num):
    """Counts the number of prime hexadecimal digits in the input string.
    Prime hexadecimal digits are: 2, 3, 5, 7, B (11), D (13).
    Args:
        num (str): A string representing a hexadecimal number.
    Returns:
        int: The count of prime hexadecimal digits in the input string.
    """
```

## Installation

This project does not require any external dependencies, so no installation of additional packages is necessary. You only need Python installed on your system to run the function.

## Usage

To use the `hex_key` function, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the code from `main.py` into your Python environment or script.
3. Call the `hex_key` function with a string argument representing a hexadecimal number.

### Example Usage

```python
# Example usage of the hex_key function
print(hex_key("AB"))  # Output: 1
print(hex_key("1077E"))  # Output: 2
print(hex_key("ABED1A33"))  # Output: 4
print(hex_key("123456789ABCDEF0"))  # Output: 6
print(hex_key("2020"))  # Output: 2
```

## Documentation

For further details on how the function works, refer to the docstring provided in the function definition. The docstring explains the purpose of the function, the arguments it takes, and the value it returns.

## Support

If you encounter any issues or have questions about using this software, please contact our support team at support@chatdev.com.

```