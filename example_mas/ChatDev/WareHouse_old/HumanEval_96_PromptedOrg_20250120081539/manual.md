# Prime Number Finder

This software provides functionality to find prime numbers less than a given number. It includes a module with functions to determine if a number is prime and to generate a list of prime numbers up to a specified limit.

## Main Functions

### 1. `is_prime(num)`

- **Description**: Checks if a given number is a prime number.
- **Parameters**: 
  - `num` (int): The number to check for primality.
- **Returns**: 
  - `bool`: `True` if the number is prime, `False` otherwise.

### 2. `count_up_to(n)`

- **Description**: Returns a list of prime numbers less than a specified number.
- **Parameters**: 
  - `n` (int): The upper limit (exclusive) for finding prime numbers.
- **Returns**: 
  - `list`: A list of prime numbers less than `n`.

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the prime number functions.

2. **Run the Code**: Use a Python interpreter to run the `main.py` file. You can test the functions by calling them with different arguments.

   Example usage:

   ```python
   from main import count_up_to

   # Find prime numbers less than 11
   primes = count_up_to(11)
   print(primes)  # Output: [2, 3, 5, 7]
   ```

3. **Modify and Extend**: Feel free to modify the code to suit your needs or integrate it into larger projects.

## Documentation

For further details on how the functions work, refer to the docstrings provided in the `main.py` file. These docstrings offer concise explanations of each function's purpose, parameters, and return values.

This software is designed to be straightforward and efficient, providing a reliable way to work with prime numbers in Python.