# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Quick Install

Since there are no external dependencies required for this software, you can simply use Python to run the code. Ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

## 🤔 What is this?

This software is designed to find Fibonacci numbers that are also prime. Fibonacci numbers are a sequence where each number is the sum of the two preceding ones, starting from 0 and 1. A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. This function combines these two mathematical concepts to find numbers that are both Fibonacci and prime.

## Main Functions

- **`is_prime(num: int) -> bool`**: This helper function checks if a given number is prime.
- **`generate_fibonacci()`**: This generator function produces Fibonacci numbers indefinitely.
- **`prime_fib(n: int) -> int`**: This is the main function that returns the n-th Fibonacci number that is also prime.

## How to Use

1. **Clone or Download the Code**: Obtain the `main.py` file containing the implementation.

2. **Run the Code**: Use a Python environment to execute the code. You can run the function directly in a Python interpreter or include it in your own scripts.

3. **Example Usage**:
   ```python
   from main import prime_fib

   print(prime_fib(1))  # Output: 2
   print(prime_fib(2))  # Output: 3
   print(prime_fib(3))  # Output: 5
   print(prime_fib(4))  # Output: 13
   print(prime_fib(5))  # Output: 89
   ```

## Documentation

The code is straightforward and self-contained. The `prime_fib` function is the primary function of interest, and it utilizes helper functions to determine prime numbers and generate Fibonacci numbers. You can modify or extend the code as needed for more complex applications or integrations.

For any further questions or support, please contact our development team.