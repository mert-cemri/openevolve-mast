# String XOR Utility

This software provides a utility function to perform a binary XOR operation on two binary strings. It is designed to be simple and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `string_xor` function. This function takes two binary strings as input and returns their XOR result as a binary string.

### Function: `string_xor`

- **Input**: Two strings `a` and `b`, consisting only of '1's and '0's.
- **Output**: A string representing the binary XOR of the inputs.
- **Example**:
  ```python
  >>> string_xor('010', '110')
  '100'
  ```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository or download the `main.py` file to your local machine.
2. Ensure Python is installed by running `python --version` in your terminal or command prompt.

## Usage

To use the `string_xor` function, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the Python interpreter or create a Python script to import and use the `string_xor` function.

### Example Usage

```python
# Import the function from main.py
from main import string_xor

# Define two binary strings
a = '010'
b = '110'

# Perform XOR operation
result = string_xor(a, b)

# Output the result
print(result)  # Output: '100'
```

## Error Handling

The `string_xor` function includes basic error handling to ensure the input strings are of the same length. If they are not, a `ValueError` is raised with the message "Input strings must be of the same length."

## Conclusion

This utility provides a simple and effective way to perform binary XOR operations on strings. With no external dependencies, it is easy to integrate into any Python project.