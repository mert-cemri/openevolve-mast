# Prime Number Checker

This software module provides a function to determine if a given number is prime. It is designed to be simple and efficient, with no external dependencies required.

## Main Function

The main function provided by this module is `is_prime(n)`, which checks if a number `n` is a prime number.

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
```

### How It Works

- The function first checks if the number `n` is less than or equal to 1, in which case it returns `False` since numbers less than or equal to 1 are not prime.
- If `n` is 2, the function returns `True` because 2 is the smallest and only even prime number.
- If `n` is even and greater than 2, the function returns `False` because even numbers greater than 2 are not prime.
- For odd numbers greater than 2, the function checks divisibility from 3 up to the square root of `n`. If any divisor is found, it returns `False`. If no divisors are found, it returns `True`.

## Installation

This module does not require any external dependencies. You can simply download the `main.py` file and use it in your Python environment.

## Usage

1. **Download the Code**: Ensure you have the `main.py` file in your working directory.

2. **Import the Function**: In your Python script or interactive shell, import the `is_prime` function.

   ```python
   from main import is_prime
   ```

3. **Check Prime Numbers**: Use the `is_prime` function to check if a number is prime.

   ```python
   print(is_prime(6))    # Output: False
   print(is_prime(101))  # Output: True
   print(is_prime(11))   # Output: True
   ```

## Testing

You can test the function using the provided examples in the docstring. Simply run the function with different inputs to verify its correctness.

## Conclusion

This module provides a straightforward and efficient way to check for prime numbers in Python. It is designed to be easy to use and integrate into other projects without the need for additional libraries or dependencies.