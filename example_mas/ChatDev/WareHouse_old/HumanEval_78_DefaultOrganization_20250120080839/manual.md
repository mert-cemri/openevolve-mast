manual.md

```
# Hex Key Prime Counter

This software provides a simple utility function to count the number of prime hexadecimal digits in a given string. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functionality

The main function provided by this software is `hex_key`, which performs the following tasks:

- Receives a hexadecimal number as a string.
- Counts the number of hexadecimal digits that are prime numbers.
- Returns the count of these prime digits.

### Prime Hexadecimal Digits

In the context of this software, the prime hexadecimal digits are:
- 2
- 3
- 5
- 7
- B (equivalent to decimal 11)
- D (equivalent to decimal 13)

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** or download the `main.py` file to your local machine.

2. **Ensure Python is installed** on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the script** directly using Python.

## Usage

To use the `hex_key` function, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script with the desired input. You can do this by opening a Python interactive shell or by modifying the script to include test cases.

### Example Usage

Here are some examples of how to use the `hex_key` function:

```python
# Example usage:
print(hex_key("AB"))  # Output: 1
print(hex_key("1077E"))  # Output: 2
print(hex_key("ABED1A33"))  # Output: 4
print(hex_key("123456789ABCDEF0"))  # Output: 6
print(hex_key("2020"))  # Output: 2
```

Simply copy the above code into a Python script or interactive shell to see the function in action.

## Documentation

For further details, please refer to the comments within the `main.py` file, which provide a comprehensive explanation of the function's parameters and return values.

```

This manual provides a clear and concise guide for users to understand and utilize the `hex_key` function effectively.