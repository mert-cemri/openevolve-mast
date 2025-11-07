# Prime Number Checker

This software provides a simple function to determine if a given number is a prime number. It is implemented in Python and is designed to be easy to use and integrate into other projects.

## Main Function

The main function provided by this software is `is_prime(n)`. This function takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise.

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

## Installation

No external dependencies are required for this project. The function is implemented in pure Python, and you can use it directly in your Python environment.

### Quick Install

To use the `is_prime` function, simply download the `main.py` file and include it in your project. You can then import the function and use it as needed.

```bash
# Clone the repository or download the main.py file
git clone <repository-url>
```

## How to Use

1. **Import the Function**

   First, ensure that the `main.py` file is in your project directory. Then, import the `is_prime` function into your Python script.

   ```python
   from main import is_prime
   ```

2. **Check if a Number is Prime**

   Use the `is_prime` function to check if a number is prime. Pass the number you want to check as an argument to the function.

   ```python
   result = is_prime(101)
   print(result)  # Output: True
   ```

3. **Examples**

   Here are some examples of how to use the `is_prime` function:

   ```python
   print(is_prime(6))    # Output: False
   print(is_prime(101))  # Output: True
   print(is_prime(11))   # Output: True
   print(is_prime(13441))# Output: True
   print(is_prime(61))   # Output: True
   print(is_prime(4))    # Output: False
   print(is_prime(1))    # Output: False
   ```

## Documentation

For further information and examples, refer to the docstring provided in the `is_prime` function. This includes usage examples and expected outputs for various inputs.

## Support

If you encounter any issues or have questions about using the software, please contact our support team for assistance.