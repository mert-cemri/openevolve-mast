# Tribonacci Sequence Calculator

This software module provides a function to calculate the Tribonacci sequence, a lesser-known sequence similar to the Fibonacci sequence. The function `tri(n)` returns a list of the first `n + 1` numbers of the Tribonacci sequence.

## Main Functionality

### `tri(n)`

- **Purpose**: Calculate the first `n + 1` numbers of the Tribonacci sequence.
- **Input**: A non-negative integer `n`.
- **Output**: A list containing the first `n + 1` numbers of the Tribonacci sequence.

The Tribonacci sequence is defined as follows:
- `tri(1) = 3`
- `tri(n) = 1 + n / 2`, if `n` is even.
- `tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3)`, if `n` is odd.

### Example Usage

```python
# Example usage of the tri function
print(tri(3))  # Output: [1, 3, 2, 8]
```

## Installation

To use this module, you need to have Python installed on your system. The module does not have any external dependencies, so no additional installations are required.

### Steps to Install Python

1. **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.
2. **Install Python**: Follow the installation instructions provided on the website for your specific operating system.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the Tribonacci sequence function.
2. **Run the Script**: Use a Python interpreter to run the script and test the function.

### Running the Script

- Open a terminal or command prompt.
- Navigate to the directory where `main.py` is located.
- Run the script using the command:

  ```bash
  python main.py
  ```

- You can modify the script to test the `tri(n)` function with different values of `n`.

## Documentation

For further details on the Tribonacci sequence and the implementation, refer to the comments within the `main.py` file. The code is documented to explain the logic and calculations involved in generating the sequence.

## Support

For any issues or questions regarding the use of this module, please contact our support team at support@chatdev.com. We are here to assist you with any inquiries you may have.