manual.md

```
# Prime Multiplication Checker

This software provides a function to determine if a given number is the product of exactly three prime numbers. It is designed to work with numbers less than 100.

## Quick Install

This software does not require any external dependencies. It is implemented in Python and can be run in any standard Python environment.

## 🤔 What is this?

The Prime Multiplication Checker is a simple utility that checks if a given number can be expressed as the product of exactly three prime numbers. This can be useful in mathematical computations and educational purposes to understand prime factorization.

## 📖 Main Functions

### `is_multiply_prime(a)`

- **Description**: This function checks if the input number `a` is the product of exactly three prime numbers.
- **Parameters**: 
  - `a` (int): The number to be checked. It should be less than 100.
- **Returns**: 
  - `True` if `a` is the product of exactly three prime numbers.
  - `False` otherwise.

### Example Usage

```python
from main import is_multiply_prime

# Example: Check if 30 is the product of three prime numbers
result = is_multiply_prime(30)
print(result)  # Output: True

# Example: Check if 20 is the product of three prime numbers
result = is_multiply_prime(20)
print(result)  # Output: False
```

## How to Use

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Download the Code**: Save the provided code into a file named `main.py`.

3. **Run the Code**: Use a Python interpreter to run the code. You can test the function by calling it with different numbers to check if they are the product of three prime numbers.

4. **No External Libraries Required**: This software does not require any additional libraries or dependencies. It uses standard Python functions.

## Additional Information

This software is a simple educational tool to demonstrate the use of prime numbers in factorization. It can be extended or modified for more complex mathematical operations or integrated into larger projects requiring prime factorization checks.
```