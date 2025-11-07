# Fibonacci Calculator

This software module provides a function to calculate the n-th Fibonacci number. It is implemented in Python and is designed to be simple and efficient, suitable for educational purposes or as a utility in larger projects.

## Main Functionality

The main function provided by this module is `fib(n: int) -> int`, which returns the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. For this implementation, the sequence starts with 1 and 1.

### Example Usage

```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```

## Installation

To use this software, you need to have Python installed on your machine. This module does not require any additional dependencies beyond the Python standard library.

### Steps to Install Python

1. **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the instructions provided on the website to install Python on your system. Make sure to check the option to add Python to your system PATH during installation.

3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the Fibonacci function.

2. **Run the Function**: You can run the function in a Python environment (such as IDLE, PyCharm, or a Jupyter Notebook) by importing the function and calling it with the desired integer input.

### Example

```python
from main import fib

# Calculate the 10th Fibonacci number
result = fib(10)
print(f"The 10th Fibonacci number is: {result}")
```

## Error Handling

- The function raises a `ValueError` if the input `n` is less than or equal to 0, as the Fibonacci sequence is defined for positive integers only.

## Documentation

For further information and detailed documentation, please refer to the comments within the `main.py` file. The function is documented with examples to guide you on how to use it effectively.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to assist you with any inquiries related to this software module.