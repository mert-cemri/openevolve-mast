# is_multiply_prime User Manual

## Introduction

The `is_multiply_prime` function is a simple Python utility designed to determine if a given number is the product of exactly three prime numbers. This function is particularly useful for educational purposes, mathematical explorations, or any application where prime factorization is relevant.

## Main Functions

### is_prime(n)

- **Description**: This helper function checks if a given number `n` is a prime number.
- **Parameters**: 
  - `n` (int): The number to check for primality.
- **Returns**: 
  - `bool`: `True` if `n` is a prime number, `False` otherwise.

### is_multiply_prime(a)

- **Description**: This function checks if the given number `a` is the product of exactly three prime numbers.
- **Parameters**: 
  - `a` (int): The number to check.
- **Returns**: 
  - `bool`: `True` if `a` is the product of three prime numbers, `False` otherwise.

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

## Usage

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Script**: You can use the Python interpreter to run the script and test the function. For example:

   ```bash
   python main.py
   ```

4. **Example Usage**: You can test the function by calling it with different numbers. For example, to check if 30 is the product of three prime numbers, you can modify the script to include:

   ```python
   print(is_multiply_prime(30))  # Output: True
   ```

5. **Modify and Extend**: Feel free to modify the script to test other numbers or integrate it into larger projects.

## Conclusion

The `is_multiply_prime` function is a straightforward tool for checking the prime factorization of numbers under 100. With no external dependencies, it is easy to integrate and use in various Python environments. Enjoy exploring the fascinating world of prime numbers!