# String XOR Application

This application provides a simple utility to perform a binary XOR operation on two strings consisting only of '1's and '0's. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The primary function of this application is `string_xor`, which takes two binary strings as input and returns their XOR result as a binary string. The XOR operation is performed bit by bit, where the result is '1' if the bits are different and '0' if they are the same.

### Function Definition

```python
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
```

### Example Usage

```python
result = string_xor('010', '110')
print(result)  # Output: '100'
```

## Installation

This application does not require any external libraries or dependencies. It is implemented purely in Python, making it easy to set up and use.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone or download the source code to your local machine.

3. Navigate to the directory containing the `main.py` file.

4. Run the Python script using the following command:

   ```bash
   python main.py
   ```

## How to Use

1. Open the `main.py` file in a text editor or IDE of your choice.

2. Modify the input strings `a` and `b` in the `string_xor` function call to your desired binary strings.

3. Save the changes and execute the script to see the XOR result.

## Error Handling

- The function raises a `ValueError` if the input strings `a` and `b` are not of the same length. Ensure both strings have the same number of bits before calling the function.

## Documentation

For further information and updates, please refer to the source code comments and docstrings provided within the `main.py` file. The code is straightforward and self-explanatory, designed to be easily understandable and modifiable.

Feel free to reach out for support or contribute to the project by submitting issues or pull requests on the repository hosting platform.