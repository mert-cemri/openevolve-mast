# Prime Number Checker

This software provides a simple function to determine if a given number is prime. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function of this software is `is_prime(n)`, which checks if a number `n` is prime. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

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

- If `n` is less than or equal to 1, it returns `False` because numbers less than or equal to 1 are not prime.
- If `n` is 2, it returns `True` because 2 is the only even prime number.
- If `n` is divisible by 2, it returns `False` because even numbers greater than 2 are not prime.
- For odd numbers greater than 2, it checks divisibility from 3 up to the square root of `n`. If `n` is divisible by any of these numbers, it returns `False`. Otherwise, it returns `True`.

## Installation

This software does not require any external libraries or dependencies. It is implemented in pure Python. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can test the function by running the Python interpreter and importing the function:

   ```bash
   python
   ```

   ```python
   from main import is_prime

   # Test the function
   print(is_prime(6))    # Output: False
   print(is_prime(101))  # Output: True
   ```

4. **Run Tests**: You can also run the provided examples to verify the function's correctness.

## Conclusion

This software provides a straightforward method to check for prime numbers using Python. It is efficient for small to moderately large numbers and does not require any additional setup beyond having Python installed.