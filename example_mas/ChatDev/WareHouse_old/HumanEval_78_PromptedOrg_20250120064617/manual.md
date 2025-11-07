# Hexadecimal Prime Digit Counter

This software provides a function to count the number of prime hexadecimal digits in a given string. It is designed to help users identify prime numbers within hexadecimal strings.

## Main Function

### `hex_key(num)`

- **Description**: This function receives a hexadecimal number as a string and counts the number of hexadecimal digits that are prime numbers. The prime hexadecimal digits are `2`, `3`, `5`, `7`, `B` (which represents decimal 11), and `D` (which represents decimal 13).
- **Parameters**: 
  - `num` (str): A string representing a hexadecimal number. The input is assumed to be correct or an empty string, and symbols A, B, C, D, E, F are always uppercase.
- **Returns**: 
  - `int`: The count of prime hexadecimal digits in the input string.

### Examples

- `hex_key("AB")` returns `1`.
- `hex_key("1077E")` returns `2`.
- `hex_key("ABED1A33")` returns `4`.
- `hex_key("123456789ABCDEF0")` returns `6`.
- `hex_key("2020")` returns `2`.

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

### Dependencies

This software does not have any external dependencies. You can directly use the provided Python code in your environment.

## Usage

1. **Copy the Code**: Copy the `hex_key` function code from the `main.py` file into your Python environment or script.

2. **Run the Function**: Call the `hex_key` function with a hexadecimal string as an argument to get the count of prime hexadecimal digits.

```python
# Example usage
result = hex_key("123456789ABCDEF0")
print(result)  # Output: 6
```

## Documentation

For further details and examples, please refer to the inline comments within the code. The function is straightforward and designed to be easy to integrate into larger projects or use as a standalone utility.

Feel free to modify and extend the code to suit your specific needs. If you encounter any issues or have questions, please reach out to our support team for assistance.