manual.md

```
# Hex Key Prime Counter

A simple Python application to count the number of prime hexadecimal digits in a given hexadecimal string.

## Introduction

The Hex Key Prime Counter is a utility function designed to process a hexadecimal number represented as a string and count how many of its digits are prime numbers. In the context of hexadecimal digits, the prime numbers are 2, 3, 5, 7, B (11 in decimal), and D (13 in decimal).

## Main Functionality

- **hex_key(num):** This function takes a single argument `num`, which is a string representing a hexadecimal number. It returns an integer count of the prime digits found in the string.

## Installation

This application does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the source code directly.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the source code is located.

## Usage

To use the Hex Key Prime Counter, you can directly call the `hex_key` function from a Python script or an interactive Python session.

### Example Usage

```python
# Import the function from the main.py file
from main import hex_key

# Example calls to the function
print(hex_key("AB"))          # Output: 1
print(hex_key("1077E"))       # Output: 2
print(hex_key("ABED1A33"))    # Output: 4
print(hex_key("123456789ABCDEF0")) # Output: 6
print(hex_key("2020"))        # Output: 2
```

## Documentation

The function is straightforward and does not require additional configuration or setup. The logic is encapsulated within the `hex_key` function, which iterates over the input string and counts the prime digits.

For any further questions or support, please refer to the comments within the code or contact the development team.

## Conclusion

The Hex Key Prime Counter is a lightweight and efficient tool for counting prime hexadecimal digits. It is designed to be easy to use and integrate into larger projects if needed.
```
