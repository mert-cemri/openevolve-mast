# Binary XOR String Operation

This software module provides a simple function to perform a binary XOR operation on two binary strings. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The main function of this software is `string_xor`, which takes two binary strings as input and returns their XOR result as a binary string. The XOR operation is performed bit by bit, where the result is '1' if the bits are different and '0' if they are the same.

### Function Signature

```python
def string_xor(a: str, b: str) -> str:
```

### Parameters

- `a` (str): A binary string consisting of '1's and '0's.
- `b` (str): Another binary string consisting of '1's and '0's. It must be of the same length as `a`.

### Returns

- A binary string representing the result of the XOR operation.

### Example

```python
>>> string_xor('010', '110')
'100'
```

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `string_xor` function.

2. **Run the Function**: You can use the function in your Python scripts by importing it or by directly running the `main.py` file.

3. **Example Usage**: To use the function, simply call it with two binary strings of equal length.

```python
from main import string_xor

result = string_xor('1010', '1100')
print(result)  # Output will be '0110'
```

## Error Handling

- The function raises a `ValueError` if the input strings `a` and `b` are not of the same length. Ensure both strings are of equal length before calling the function.

## Documentation

For further details and examples, refer to the inline documentation within the `main.py` file. The function is straightforward and designed for ease of use in various applications requiring binary XOR operations.