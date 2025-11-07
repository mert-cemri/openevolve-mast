# is_multiply_prime User Manual

## Introduction

The `is_multiply_prime` function is a Python utility designed to determine whether a given number is the product of exactly three prime numbers. This function is particularly useful for mathematical computations and educational purposes where understanding the composition of numbers in terms of prime factors is required.

## Main Functions

### is_prime(n)

- **Purpose**: Checks if a number `n` is a prime number.
- **Input**: An integer `n`.
- **Output**: Returns `True` if `n` is a prime number, otherwise returns `False`.

### is_multiply_prime(a)

- **Purpose**: Determines if the given number `a` is the product of exactly three prime numbers.
- **Input**: An integer `a` (less than 100).
- **Output**: Returns `True` if `a` is the product of three prime numbers, otherwise returns `False`.

## Installation

### Environment Setup

This software does not require any external dependencies beyond a standard Python installation. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

Since there are no external dependencies, you can directly use the provided Python script. Simply download or clone the repository containing the `main.py` file.

## Usage

1. **Download the Script**: Ensure you have the `main.py` file available in your working directory.

2. **Run the Function**: You can use the function in any Python environment (such as a Python shell, script, or Jupyter notebook).

   Example usage:
   ```python
   from main import is_multiply_prime

   result = is_multiply_prime(30)
   print(result)  # Output: True

   result = is_multiply_prime(28)
   print(result)  # Output: False
   ```

3. **Understanding the Output**: The function will return `True` if the input number is the product of exactly three prime numbers and `False` otherwise.

## Additional Information

- **Limitations**: The function is designed to work with numbers less than 100. It may not provide accurate results for numbers equal to or greater than 100.
- **Customization**: You can modify the `is_prime` function to include additional checks or optimizations if needed for larger numbers.

This manual provides all necessary information to effectively use the `is_multiply_prime` function. For further assistance or inquiries, please contact our support team.