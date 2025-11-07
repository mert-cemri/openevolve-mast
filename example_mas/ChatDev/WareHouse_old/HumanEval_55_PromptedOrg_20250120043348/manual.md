# Fibonacci Calculator

This software module provides a simple function to calculate the n-th Fibonacci number. It is designed to be lightweight and does not require any external dependencies.

## Main Function

The main function provided by this module is `fib(n: int)`, which returns the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. However, in this implementation, the sequence starts with 1 and 1.

### Function Signature

```python
def fib(n: int) -> int:
```

### Parameters

- `n` (int): The position in the Fibonacci sequence to retrieve. It must be a positive integer.

### Returns

- (int): The n-th Fibonacci number.

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

This module does not require any external libraries or dependencies. It is implemented purely in Python and can be used directly in any Python environment.

### Quick Start

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run Python**: Use Python to execute the script or import the function in your own scripts.

## Usage

To use the Fibonacci function, you can either run the `main.py` script directly or import the `fib` function into your own Python scripts.

### Running Directly

If you want to test the function directly, you can run the following command in your terminal:

```bash
python main.py
```

### Importing into Your Script

To use the `fib` function in your own Python scripts, simply import it:

```python
from main import fib

# Example usage
print(fib(10))  # Output: 55
```

## Error Handling

The function will raise a `ValueError` if the input `n` is not a positive integer. Ensure that you provide a valid input to avoid errors.

## Conclusion

This module provides a simple and efficient way to calculate Fibonacci numbers. It is ideal for educational purposes, small projects, or as a utility in larger applications where Fibonacci calculations are needed.