manual.md

```
# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functions

### prime_fib(n: int) -> int

- **Description**: This function returns the n-th Fibonacci number that is also a prime number.
- **Parameters**: 
  - `n` (int): The position of the prime Fibonacci number you want to retrieve.
- **Returns**: 
  - An integer representing the n-th Fibonacci number that is also prime.

### is_prime(num: int) -> bool

- **Description**: This helper function checks if a given number is prime.
- **Parameters**: 
  - `num` (int): The number to check for primality.
- **Returns**: 
  - A boolean value indicating whether the number is prime.

### fibonacci_sequence()

- **Description**: This is a generator function that yields Fibonacci numbers indefinitely.
- **Returns**: 
  - Yields Fibonacci numbers one by one.

## Installation

This software does not require any external dependencies, so you can run it directly with Python. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: 
   - Clone the repository using `git clone <repository-url>` or download the ZIP file and extract it.

2. **Navigate to the Directory**:
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Code**:
   - You can run the `main.py` file using Python to test the `prime_fib` function. For example:
     ```bash
     python main.py
     ```

4. **Using the Function**:
   - You can import the `prime_fib` function into your own Python scripts and use it as follows:
     ```python
     from main import prime_fib

     # Example usage
     print(prime_fib(1))  # Output: 2
     print(prime_fib(2))  # Output: 3
     print(prime_fib(3))  # Output: 5
     ```

## Example

Here is an example of how to use the `prime_fib` function in a Python script:

```python
from main import prime_fib

# Find the 5th prime Fibonacci number
result = prime_fib(5)
print(f"The 5th prime Fibonacci number is: {result}")
```

This will output:

```
The 5th prime Fibonacci number is: 89
```

## Support

For any issues or questions, please contact our support team at support@chatdev.com.

```