# Binary String XOR Utility

This software provides a simple utility function to perform a binary XOR operation on two binary strings. The function is designed to take two strings consisting only of '1's and '0's, perform a binary XOR operation, and return the result as a new string.

## Main Functionality

The main function provided by this software is `string_xor`, which performs the following operations:

- **Input**: Two binary strings `a` and `b` of the same length.
- **Output**: A new binary string representing the XOR of the input strings.

### Example Usage

```python
>>> string_xor('010', '110')
'100'
```

In this example, the XOR operation is performed bit by bit:

- '0' XOR '1' = '1'
- '1' XOR '1' = '0'
- '0' XOR '0' = '0'

Thus, the result is '100'.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the code using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: In your Python script, import the `string_xor` function.

   ```python
   from main import string_xor
   ```

2. **Call the Function**: Use the function by passing two binary strings of equal length.

   ```python
   result = string_xor('1010', '1100')
   print(result)  # Output will be '0110'
   ```

## Error Handling

- The function checks if the input strings are of the same length. If not, it raises a `ValueError` with the message "Input strings must be of the same length."

## Documentation

For further details and examples, please refer to the inline documentation within the `main.py` file. The function is well-documented with a docstring explaining its purpose, inputs, and outputs.

This utility is designed to be simple and effective for performing binary XOR operations on strings, making it a useful tool for developers working with binary data.