# Prime Number Checker

This software module provides a function to determine if a given number is prime. It is a simple utility that can be used in various applications where prime number checking is required.

## Main Function

The main function provided by this module is `is_prime(n)`. This function takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise.

### Function Signature

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
```

### Example Usage

```python
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
```

## Installation

This module does not require any external dependencies, making it easy to integrate into your existing Python projects.

### Quick Install

Simply download the `main.py` file and include it in your project directory. You can then import the `is_prime` function into your scripts as needed.

```bash
# No external dependencies required
```

## How to Use

1. **Download the `main.py` file**: Ensure that the file is in your project directory.

2. **Import the function**: In your Python script, import the `is_prime` function.

    ```python
    from main import is_prime
    ```

3. **Call the function**: Use the `is_prime` function by passing an integer as an argument to check if it is a prime number.

    ```python
    result = is_prime(29)
    print(result)  # Output: True
    ```

## Documentation

The function is designed to be efficient and straightforward. It checks for primality by:

- Returning `False` for numbers less than or equal to 1.
- Returning `True` for the number 2, which is the only even prime number.
- Returning `False` for any other even number.
- Iterating through odd numbers up to the square root of `n` to check for divisibility.

This approach ensures that the function runs efficiently even for larger numbers.