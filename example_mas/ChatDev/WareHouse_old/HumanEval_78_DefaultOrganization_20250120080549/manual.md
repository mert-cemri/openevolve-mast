# Hexadecimal Prime Digit Counter

This software provides a function to count the number of prime hexadecimal digits in a given string. It is designed to be simple and efficient, requiring no external dependencies.

## Main Function

### `hex_key(num)`

- **Description**: This function receives a hexadecimal number as a string and counts the number of hexadecimal digits that are prime numbers. The prime hexadecimal digits considered are: 2, 3, 5, 7, B (11 in decimal), and D (13 in decimal).

- **Parameters**:
  - `num` (str): A string representing a hexadecimal number. The input is assumed to be correct or an empty string, with uppercase letters for A, B, C, D, E, F.

- **Returns**:
  - `int`: The count of prime hexadecimal digits in the input string.

- **Examples**:
  - `hex_key("AB")` returns `1`.
  - `hex_key("1077E")` returns `2`.
  - `hex_key("ABED1A33")` returns `4`.
  - `hex_key("123456789ABCDEF0")` returns `6`.
  - `hex_key("2020")` returns `2`.

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can use the function by importing it into your Python script or by running the examples directly in the Python interpreter.

   ```python
   from main import hex_key

   # Example usage
   print(hex_key("AB"))  # Output: 1
   print(hex_key("1077E"))  # Output: 2
   ```

4. **Modify and Extend**: Feel free to modify the code to suit your needs or extend its functionality.

## Notes

- The function assumes that the input string is a valid hexadecimal number or an empty string.
- The hexadecimal digits are case-sensitive, and the function expects uppercase letters for A, B, C, D, E, F.

This software is designed to be straightforward and easy to integrate into larger projects where counting prime hexadecimal digits is necessary. Enjoy using the Hexadecimal Prime Digit Counter!