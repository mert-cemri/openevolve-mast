# Binary String XOR Utility

This software module provides a simple utility function to perform a binary XOR operation on two binary strings. It is designed to be lightweight and requires no external dependencies.

## Main Functionality

The main function provided by this module is `string_xor`, which takes two binary strings as input and returns their XOR result as a binary string. The XOR operation is performed bit by bit, where each bit in the result is '1' if the corresponding bits in the input strings are different, and '0' if they are the same.

### Function Signature

```python
def string_xor(a: str, b: str) -> str:
```

#### Parameters

- `a` (str): A binary string consisting only of '1's and '0's.
- `b` (str): Another binary string consisting only of '1's and '0's. Must be of the same length as `a`.

#### Returns

- (str): A binary string representing the result of the XOR operation.

#### Example

```python
>>> string_xor('010', '110')
'100'
```

## Installation

This module does not require any external libraries or dependencies. It is implemented purely in Python and can be used directly in any Python environment.

### Quick Start

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**

   Change into the directory containing the `main.py` file:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**

   You can use the `string_xor` function directly in your Python scripts or interactive sessions. Here is an example of how to use it:

   ```python
   from main import string_xor

   result = string_xor('1010', '1100')
   print(result)  # Output: '0110'
   ```

## Usage

To use the `string_xor` function, simply import it from the `main.py` file and call it with two binary strings of equal length. The function will return the XOR result as a new binary string.

### Example Usage

```python
from main import string_xor

# Example binary strings
binary_string1 = '1101'
binary_string2 = '1011'

# Perform XOR operation
xor_result = string_xor(binary_string1, binary_string2)

# Output the result
print(f"The XOR of {binary_string1} and {binary_string2} is {xor_result}")
```

## Error Handling

The function raises a `ValueError` if the input strings are not of the same length. Ensure that both input strings are of equal length before calling the function to avoid this error.

## Conclusion

This utility provides a straightforward way to perform binary XOR operations on strings. It is efficient and easy to integrate into larger projects that require binary string manipulation.