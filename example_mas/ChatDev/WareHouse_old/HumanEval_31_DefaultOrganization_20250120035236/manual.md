# Prime Number Checker

This software provides a simple function to check if a given number is a prime number. It is implemented in Python and does not require any external dependencies.

## Quick Install

No installation of external packages is required as the software is implemented using only Python's standard library. Ensure you have Python installed on your system.

## 🤔 What is this?

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. This software provides a function `is_prime(n)` that determines if a given number `n` is prime.

## Main Function

### `is_prime(n)`

- **Description**: This function checks if a given number `n` is a prime number.
- **Parameters**: 
  - `n` (int): The number to be checked.
- **Returns**: 
  - `bool`: Returns `True` if `n` is a prime number, `False` otherwise.

### Example Usage

```python
from main import is_prime

print(is_prime(6))    # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))   # Output: True
print(is_prime(13441))# Output: True
print(is_prime(61))   # Output: True
print(is_prime(4))    # Output: False
print(is_prime(1))    # Output: False
```

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.
3. **Run the Code**: You can use the function `is_prime(n)` in your Python scripts by importing it from `main.py`.

## 📖 Documentation

For further information on prime numbers and their properties, you can refer to [Wikipedia's Prime Number Page](https://en.wikipedia.org/wiki/Prime_number).

This software is designed to be simple and efficient, providing a quick way to check the primality of numbers without any additional setup or dependencies.