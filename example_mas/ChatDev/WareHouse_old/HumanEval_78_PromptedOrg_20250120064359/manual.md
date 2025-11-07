# Hex Key User Manual

Welcome to the Hex Key software, a simple yet powerful tool designed to count the number of prime hexadecimal digits in a given string. This manual will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it effectively.

## Introduction

Hexadecimal numbers are often used in computing and digital electronics. The Hex Key software helps you identify and count the prime digits within a hexadecimal string. Prime numbers in the context of hexadecimal digits are 2, 3, 5, 7, B (11 in decimal), and D (13 in decimal).

## Main Function

The core functionality of the Hex Key software is encapsulated in the `hex_key` function. This function takes a string representing a hexadecimal number as input and returns the count of prime hexadecimal digits within that string.

### Function Signature

```python
def hex_key(num: str) -> int:
```

### Parameters

- `num` (str): A string representing a hexadecimal number. The string may contain characters from the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}.

### Returns

- `int`: The count of prime hexadecimal digits in the input string.

### Examples

- For `num = "AB"`, the output is `1`.
- For `num = "1077E"`, the output is `2`.
- For `num = "ABED1A33"`, the output is `4`.
- For `num = "123456789ABCDEF0"`, the output is `6`.
- For `num = "2020"`, the output is `2`.

## Installation

The Hex Key software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Script**: You can run the script using Python to test the `hex_key` function.

```bash
python main.py
```

## Usage

To use the Hex Key software, simply call the `hex_key` function with your desired hexadecimal string as the argument. The function will return the count of prime hexadecimal digits.

### Example Usage

```python
# Example usage of the hex_key function
result = hex_key("123456789ABCDEF0")
print(f"The number of prime hexadecimal digits is: {result}")
```

This will output:

```
The number of prime hexadecimal digits is: 6
```

## Conclusion

The Hex Key software is a straightforward tool designed to help you count prime hexadecimal digits in a string. With no external dependencies, it is easy to set up and use. We hope this manual has provided you with the necessary information to get started with Hex Key. If you have any questions or need further assistance, please feel free to reach out.