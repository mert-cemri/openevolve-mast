# String XOR Application

This application provides a simple utility function to perform a binary XOR operation on two binary strings. The function is implemented in Python and is designed to be easy to use and integrate into other projects.

## Main Functionality

The core functionality of this application is the `string_xor` function, which takes two binary strings as input and returns their binary XOR result as a string. The function ensures that both input strings are of the same length and performs the XOR operation bit by bit.

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
# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```

## Installation

This application does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file.

3. **Navigate to the project directory**: Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open a terminal or command prompt**: Navigate to the directory containing the `main.py` file.

2. **Run the script**: Execute the script using Python by running the following command:

   ```bash
   python main.py
   ```

3. **View the output**: The script will output the result of the XOR operation for the example provided in the code.

## Documentation

The `string_xor` function is documented with a docstring that includes a brief description of its purpose and an example of its usage. The function raises a `ValueError` if the input strings are not of the same length, ensuring that the operation is performed correctly.

For further customization or integration into other projects, you can modify the `main.py` file as needed. The code is simple and self-contained, making it easy to adapt for various use cases.

## Support

For any issues or questions regarding this application, please contact the development team at ChatDev. We are committed to providing support and assistance to ensure the successful use of our software.