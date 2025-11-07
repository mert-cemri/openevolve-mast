# Prime Number Checker

This software provides a simple function to determine if a given number is a prime number. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `is_prime` function. This function takes an integer as input and returns `True` if the number is prime, and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

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

This software does not require any external libraries or dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `is_prime` function.

3. **Run the function**: You can use the function in any Python environment by importing it from the `main.py` file.

## Usage

To use the `is_prime` function, follow these steps:

1. **Open a Python environment**: This could be a Python shell, a script, or an integrated development environment (IDE) like PyCharm or VSCode.

2. **Import the function**: If you are using a script or an IDE, ensure the `main.py` file is in your working directory or adjust the import path accordingly.

   ```python
   from main import is_prime
   ```

3. **Call the function**: Pass an integer to the `is_prime` function to check if it is a prime number.

   ```python
   result = is_prime(101)
   print(result)  # Output: True
   ```

## Examples

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

For further information on prime numbers and their properties, you can refer to mathematical resources or online encyclopedias such as [Wikipedia](https://en.wikipedia.org/wiki/Prime_number).

This software is designed to be simple and efficient, providing a quick way to check for prime numbers without the need for additional libraries or complex setup.