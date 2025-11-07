# is_multiply_prime User Manual

## Introduction

The `is_multiply_prime` function is a Python utility designed to determine if a given integer is the product of exactly three prime numbers. This function is particularly useful for mathematical applications where prime factorization is required. The function operates under the constraint that the input number is less than 100.

## Main Functions

### is_prime(n)

- **Purpose**: Checks if a number `n` is a prime number.
- **Input**: An integer `n`.
- **Output**: Returns `True` if `n` is a prime number, `False` otherwise.

### is_multiply_prime(a)

- **Purpose**: Determines if the given number `a` is the product of exactly three prime numbers.
- **Input**: An integer `a`.
- **Output**: Returns `True` if `a` is the product of three prime numbers, `False` otherwise.

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Script**: Execute the script using Python. You can test the function by calling it with different integer values.

   ```bash
   python main.py
   ```

4. **Example Usage**: You can test the function directly in a Python environment by importing it and calling it with a number.

   ```python
   from main import is_multiply_prime

   print(is_multiply_prime(30))  # Output: True
   print(is_multiply_prime(60))  # Output: False
   ```

## Additional Information

- The function checks combinations of prime numbers less than 100 to determine if they multiply to the given number.
- The function is efficient for numbers less than 100 due to the limited number of prime combinations.

This manual provides all the necessary information to understand, install, and use the `is_multiply_prime` function effectively. If you encounter any issues or have further questions, please refer to the documentation or contact support.