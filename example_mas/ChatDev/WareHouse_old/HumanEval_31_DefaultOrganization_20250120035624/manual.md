# Prime Number Checker

This software module provides a simple function to determine if a given number is prime. It is implemented in Python and is designed to be straightforward and efficient.

## Main Function

The main function provided by this module is `is_prime(n)`. This function takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise.

### Function Definition

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

## Installation

This module does not require any external dependencies, making it easy to install and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `is_prime` function.

3. **Run the function**: You can use the function directly in your Python environment.

## How to Use

1. **Open your Python environment**: This could be a Python shell, a script, or an integrated development environment (IDE) like PyCharm or VSCode.

2. **Import the function**: If you have saved the `main.py` file in your working directory, you can import the function using:
   ```python
   from main import is_prime
   ```

3. **Call the function**: Use the function by passing an integer to check if it is prime.
   ```python
   print(is_prime(101))  # Output: True
   print(is_prime(6))    # Output: False
   ```

## Documentation

The function is documented with examples in the docstring. You can run these examples using Python's built-in `doctest` module to verify the function's correctness.

### Running Doctests

To run the doctests, execute the following command in your terminal or command prompt:
```bash
python -m doctest -v main.py
```

This will run the examples in the docstring and verify that the function behaves as expected.

## Conclusion

This module provides a simple and efficient way to check for prime numbers in Python. With no external dependencies, it is easy to integrate into any Python project.