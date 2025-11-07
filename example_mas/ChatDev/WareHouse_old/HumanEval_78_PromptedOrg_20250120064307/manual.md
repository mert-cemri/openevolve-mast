manual.md

```
# Hexadecimal Prime Digit Counter

This software provides a function to count the number of prime hexadecimal digits in a given string. It is designed to help users determine how many of the digits in a hexadecimal number are prime numbers.

## Main Functionality

The main function provided by this software is `hex_key(num)`, which takes a single argument:

- `num`: A string representing a hexadecimal number. The function will count the number of prime hexadecimal digits in this string.

Prime hexadecimal digits are defined as: 2, 3, 5, 7, B (which is 11 in decimal), and D (which is 13 in decimal).

### Examples

- For the input `"AB"`, the output will be `1`.
- For the input `"1077E"`, the output will be `2`.
- For the input `"ABED1A33"`, the output will be `4`.
- For the input `"123456789ABCDEF0"`, the output will be `6`.
- For the input `"2020"`, the output will be `2`.

## Installation

This project does not require any external dependencies, so you can use it directly without installing additional packages.

### Quick Start

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Run the function**: You can run the function in a Python environment by importing the `hex_key` function from the `main.py` file.

```python
from main import hex_key

# Example usage
result = hex_key("123456789ABCDEF0")
print(result)  # Output: 6
```

## Usage

To use the `hex_key` function, simply call it with a string representing a hexadecimal number. The function will return an integer representing the count of prime hexadecimal digits in the input string.

This function is useful for applications where you need to analyze hexadecimal numbers and determine the presence of prime digits.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is well-documented to help you understand its purpose and usage.

```
