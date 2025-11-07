# Prime Number Checker

This software provides a simple function to determine if a given number is a prime number. It is implemented in Python and does not require any external dependencies.

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
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You only need to have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## Usage

To use the `is_prime` function, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the `is_prime` function code into a Python file, for example, `main.py`.
3. Run the Python file using the command line or any Python IDE.

### Example Usage

```python
# Save this code in a file named main.py

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(is_prime(6))    # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))   # Output: True
print(is_prime(13441))# Output: True
print(is_prime(61))   # Output: True
print(is_prime(4))    # Output: False
print(is_prime(1))    # Output: False
```

Run the file using the command:

```bash
python main.py
```

This will execute the `is_prime` function with the test cases provided in the code, and you will see the output in the console.

## Conclusion

This software provides a simple and efficient way to check if a number is prime. It is easy to use and does not require any additional setup beyond having Python installed.