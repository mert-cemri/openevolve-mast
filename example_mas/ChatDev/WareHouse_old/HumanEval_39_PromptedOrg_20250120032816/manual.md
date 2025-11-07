# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Main Function

### `prime_fib(n: int)`

- **Description**: This function returns the n-th number that is both a Fibonacci number and a prime number.
- **Parameters**: 
  - `n` (int): The position of the desired prime Fibonacci number in the sequence.
- **Returns**: 
  - An integer representing the n-th prime Fibonacci number.
- **Example Usage**:
  ```python
  >>> prime_fib(1)
  2
  >>> prime_fib(2)
  3
  >>> prime_fib(3)
  5
  >>> prime_fib(4)
  13
  >>> prime_fib(5)
  89
  ```

## Installation

No external dependencies are required for this software. It is implemented purely in Python, and you can run it in any environment where Python is installed.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can use a Python interpreter to run the code. For example, open a Python shell and import the function:
   ```python
   from main import prime_fib
   print(prime_fib(1))  # Output: 2
   print(prime_fib(2))  # Output: 3
   ```

4. **Modify and Experiment**: Feel free to modify the code and experiment with different values of `n` to find other prime Fibonacci numbers.

## Documentation

The code is documented with inline comments and docstrings to help understand the logic and flow of the program. The `is_prime` function is used internally to check if a number is prime, and the `prime_fib` function generates Fibonacci numbers and checks for primality.

For any further questions or support, please contact our development team.