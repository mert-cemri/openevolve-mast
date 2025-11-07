# Hexadecimal Prime Digit Counter

This software provides a function to count the number of prime hexadecimal digits in a given string. It is designed to be simple and efficient, requiring no external dependencies.

## Main Functionality

The main function of this software is `hex_key`, which takes a string representing a hexadecimal number and returns the count of hexadecimal digits that are prime numbers. The prime hexadecimal digits considered are: 2, 3, 5, 7, B (11 in decimal), and D (13 in decimal).

### Examples

- For input `"AB"`, the output is `1`.
- For input `"1077E"`, the output is `2`.
- For input `"ABED1A33"`, the output is `4`.
- For input `"123456789ABCDEF0"`, the output is `6`.
- For input `"2020"`, the output is `2`.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Code**: You can directly run the `main.py` file to test the function.

## Usage

To use the `hex_key` function, follow these steps:

1. **Open the `main.py` File**: Locate the `main.py` file in your project directory.

2. **Call the Function**: Use the `hex_key` function by passing a hexadecimal string as an argument. For example:
   ```python
   result = hex_key("ABED1A33")
   print(result)  # Output will be 4
   ```

3. **Interpret the Result**: The function returns an integer representing the count of prime hexadecimal digits in the input string.

## Documentation

For further details on the implementation and usage, refer to the comments within the `main.py` file. The function is well-documented to provide clarity on its operation and expected inputs/outputs.

Feel free to modify the code to suit your specific needs or integrate it into larger projects. The simplicity of the function makes it highly adaptable for various applications involving hexadecimal numbers.