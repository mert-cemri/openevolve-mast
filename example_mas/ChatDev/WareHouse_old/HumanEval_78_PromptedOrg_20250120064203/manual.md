# Hex Key User Manual

## Introduction

The Hex Key software is a simple Python application designed to count the number of prime hexadecimal digits in a given string. Hexadecimal digits range from 0 to F, and the prime numbers among these are 2, 3, 5, 7, B (11 in decimal), and D (13 in decimal). This tool is useful for developers and analysts who need to process hexadecimal data and identify prime digits within it.

## Main Function

The primary function of this software is `hex_key(num)`, which takes a single argument:

- `num`: A string representing a hexadecimal number. The function will count and return the number of prime hexadecimal digits within this string.

### Functionality

- The function identifies prime digits from the set: {'2', '3', '5', '7', 'B', 'D'}.
- It iterates through each character in the input string and checks if it is a prime digit.
- It returns the count of prime digits found in the string.

### Example Usage

```python
# Example 1
print(hex_key("AB"))  # Output: 1

# Example 2
print(hex_key("1077E"))  # Output: 2

# Example 3
print(hex_key("ABED1A33"))  # Output: 4

# Example 4
print(hex_key("123456789ABCDEF0"))  # Output: 6

# Example 5
print(hex_key("2020"))  # Output: 2
```

## Installation

To use the Hex Key software, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

4. **Run the Script**: You can execute the script using Python by running the following command in your terminal:

   ```bash
   python main.py
   ```

## Dependencies

This software does not require any external Python packages or libraries beyond the standard Python installation. Therefore, there is no need for a `requirements.txt` file.

## Conclusion

The Hex Key software provides a straightforward solution for counting prime hexadecimal digits in a string. With its simple installation and usage, it is an efficient tool for anyone working with hexadecimal data. If you encounter any issues or have questions, please refer to the documentation or contact support for assistance.