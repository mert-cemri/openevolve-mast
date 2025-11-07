# Binary XOR String Operation

This software module provides a simple function to perform a binary XOR operation on two binary strings. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The primary function of this module is `string_xor`, which takes two binary strings as input and returns their XOR result as a binary string. The XOR operation is performed bit by bit, and the result is a new binary string where each bit is the XOR of the corresponding bits in the input strings.

### Function: `string_xor`

- **Input**: Two strings `a` and `b`, each consisting only of the characters '1' and '0'.
- **Output**: A string representing the binary XOR of the input strings.
- **Example**: 
  ```python
  >>> string_xor('010', '110')
  '100'
  ```

## Installation

This module does not require any external libraries or dependencies. It is implemented in pure Python, and you can use it directly in your Python environment.

### Quick Install

Since there are no external dependencies, you can simply download the `main.py` file and include it in your project.

## How to Use

1. **Download the Code**: Obtain the `main.py` file containing the `string_xor` function.

2. **Include in Your Project**: Place the `main.py` file in your project directory.

3. **Import the Function**: In your Python script, import the `string_xor` function:
   ```python
   from main import string_xor
   ```

4. **Perform XOR Operation**: Use the `string_xor` function by passing two binary strings of equal length:
   ```python
   result = string_xor('1010', '1100')
   print(result)  # Output will be '0110'
   ```

## Error Handling

- The function checks if the input strings `a` and `b` are of the same length. If not, it raises a `ValueError` with the message "Input strings must be of the same length."

## Conclusion

This module provides a straightforward and efficient way to perform binary XOR operations on strings. It is ideal for applications that require bitwise operations on binary data represented as strings. Since it has no dependencies, it is easy to integrate into any Python project.