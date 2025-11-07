# String XOR Application

This application provides a simple utility to perform a binary XOR operation on two strings consisting only of 1s and 0s. The XOR operation is a fundamental binary operation used in various fields such as cryptography, error detection, and digital logic design.

## Main Functionality

The core functionality of this application is encapsulated in the `string_xor` function. This function takes two binary strings as input and returns a new string representing the result of the XOR operation between the corresponding bits of the input strings.

### Function Definition

```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
```

### How It Works

- **Input**: Two strings `a` and `b` of equal length, consisting only of the characters '1' and '0'.
- **Output**: A string of the same length, where each character is the result of the XOR operation on the corresponding characters of `a` and `b`.

The XOR operation is defined as follows:
- If both bits are the same, the result is '0'.
- If the bits are different, the result is '1'.

## Installation

This application does not require any external dependencies beyond Python itself. To use the application, ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

## Usage

To use the `string_xor` function, follow these steps:

1. **Open a Python Environment**: You can use a Python shell, script, or an integrated development environment (IDE) like PyCharm or VSCode.
2. **Import the Function**: Ensure that the `string_xor` function is accessible in your environment. If you're using a script, you can include the function directly or import it from `main.py`.
3. **Call the Function**: Use the function by passing two binary strings of equal length as arguments.

### Example

```python
from main import string_xor

result = string_xor('010', '110')
print(result)  # Output: '100'
```

## Error Handling

The function raises a `ValueError` if the input strings are not of the same length. Ensure that both input strings have the same number of characters to avoid this error.

## Conclusion

This application provides a straightforward and efficient way to perform binary XOR operations on strings. It is designed to be simple to use and integrate into larger projects where binary operations are required.