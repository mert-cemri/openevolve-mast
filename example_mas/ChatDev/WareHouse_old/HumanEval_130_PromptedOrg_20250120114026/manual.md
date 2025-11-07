# Tribonacci Sequence Generator

This software module provides a function to generate the Tribonacci sequence, a lesser-known sequence similar to the Fibonacci sequence. The Tribonacci sequence is defined by specific recurrence relations and can be used for various mathematical and computational applications.

## Main Functions

The primary function provided by this module is:

- `tri(n)`: This function calculates and returns the first `n + 1` numbers of the Tribonacci sequence. The sequence is defined as follows:
  - `tri(1) = 3`
  - `tri(n) = 1 + n / 2`, if `n` is even.
  - `tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)`, if `n` is odd.

### Parameters:
- `n` (int): A non-negative integer representing the number of terms to calculate.

### Returns:
- `list`: A list of the first `n + 1` numbers of the Tribonacci sequence.

### Example Usage:
```python
# Example usage of the tri function
print(tri(3))  # Output: [3, 2, 8]
```

## Installation

This module does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

Since there are no external dependencies, you can simply copy the `main.py` file into your project directory and import the `tri` function as needed.

## How to Use

1. **Copy the Code**: Copy the `main.py` file containing the `tri` function into your project directory.

2. **Import the Function**: In your Python script, import the `tri` function:
   ```python
   from main import tri
   ```

3. **Call the Function**: Use the `tri` function to generate the Tribonacci sequence for a given `n`:
   ```python
   result = tri(3)
   print(result)  # Output: [3, 2, 8]
   ```

## Documentation

The function is documented with a detailed docstring explaining its parameters, return values, and usage. For further information, refer to the comments and docstrings within the `main.py` file.

This module is designed to be simple and straightforward, allowing you to easily integrate the Tribonacci sequence generator into your projects without additional setup or configuration.