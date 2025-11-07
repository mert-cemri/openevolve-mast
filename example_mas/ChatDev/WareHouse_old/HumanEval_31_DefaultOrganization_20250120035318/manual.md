# Prime Number Checker

This software provides a simple function to determine whether a given number is a prime number. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function of this software is `is_prime(n)`, which checks if a given number `n` is prime.

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

- The function first checks if the number `n` is less than or equal to 1. If so, it returns `False` because numbers less than or equal to 1 are not prime.
- If `n` is 2 or 3, it returns `True` because both are prime numbers.
- If `n` is divisible by 2 or 3, it returns `False` because it is not prime.
- For numbers greater than 3, the function checks divisibility from 5 onwards, skipping even numbers, up to the square root of `n`. If any divisor is found, it returns `False`.
- If no divisors are found, it returns `True`, indicating that `n` is a prime number.

## Installation

No installation of external dependencies is required to use this software. It is implemented in pure Python.

## How to Use

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Function**: You can use the `is_prime` function directly in a Python environment. Here is an example of how to use it:

   ```python
   from main import is_prime

   print(is_prime(6))    # Output: False
   print(is_prime(101))  # Output: True
   print(is_prime(11))   # Output: True
   ```

3. **Testing**: You can test the function using the provided examples in the docstring. Simply run the function with different inputs to verify its correctness.

## Documentation

- **Getting Started**: Ensure you have Python installed on your system. No additional setup is required.
- **Usage**: Import the `is_prime` function from `main.py` and call it with an integer argument to check if it is prime.
- **Examples**: Refer to the docstring in the function for example usage and expected outputs.

This software is designed to be simple and efficient for checking prime numbers without any additional overhead.