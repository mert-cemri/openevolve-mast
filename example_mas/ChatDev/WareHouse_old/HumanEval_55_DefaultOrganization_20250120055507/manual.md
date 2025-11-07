# Fibonacci Calculator

This software module provides a function to calculate the n-th Fibonacci number using Python. It is designed to be simple and efficient, with no external dependencies required.

## Main Function

The core functionality of this software is encapsulated in the `fib` function, which computes the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1.

### Function Definition

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
```

### How It Works

- **Input**: The function takes a single integer `n` as input, which represents the position in the Fibonacci sequence.
- **Output**: It returns the n-th Fibonacci number.
- **Constraints**: The input `n` must be a positive integer. If `n` is less than or equal to 0, the function raises a `ValueError`.

### Example Usage

```python
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

## Installation

This module does not require any external libraries or dependencies. It is implemented purely in Python, making it easy to integrate into any Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the Fibonacci function.

2. **Run the Function**: You can use the function directly in your Python scripts or interactive Python shell.

3. **Testing**: You can test the function using the provided examples in the docstring to ensure it works as expected.

## Documentation

For further details, you can refer to the docstring within the `fib` function in the `main.py` file. This includes example usage and expected outputs for various inputs.

This module is designed to be straightforward and efficient, providing a reliable way to compute Fibonacci numbers for any positive integer input.