# Decimal to Binary Converter

This software module provides a simple function to convert a decimal number into a binary string with a specific format. The binary string is enclosed with the characters 'db' at both the beginning and the end.

## Main Functionality

The main function provided by this module is `decimal_to_binary(decimal)`, which takes a decimal number as input and returns a formatted binary string. The binary string is prefixed and suffixed with 'db' to meet the specified format requirements.

### Function: `decimal_to_binary(decimal)`

- **Input:** 
  - `decimal` (int): The decimal number you want to convert to binary.
  
- **Output:**
  - Returns a string that represents the binary equivalent of the decimal number, formatted with 'db' at the start and end.

- **Example Usage:**
  ```python
  result = decimal_to_binary(15)
  print(result)  # Output: "db1111db"
  
  result = decimal_to_binary(32)
  print(result)  # Output: "db100000db"
  ```

## Installation

To use this module, you need to have Python installed on your system. The module does not require any additional external dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed:** 
   - You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the module:**
   - You can clone the repository or download the `main.py` file containing the `decimal_to_binary` function.

3. **Run your Python script:**
   - You can use the function in any Python script by importing it from the `main.py` file.

## Usage

1. **Import the function:**
   - If you have the `main.py` file in your project directory, you can import the function using:
     ```python
     from main import decimal_to_binary
     ```

2. **Call the function with a decimal number:**
   - Use the function by passing a decimal number as an argument to get the formatted binary string.

3. **Example:**
   ```python
   from main import decimal_to_binary

   # Convert decimal number 15 to binary
   binary_string = decimal_to_binary(15)
   print(binary_string)  # Output: "db1111db"
   ```

This module is designed to be simple and straightforward, providing a specific utility for converting decimal numbers to a formatted binary string. Enjoy using the Decimal to Binary Converter!