# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is a simple Python script designed to be efficient and easy to use.

## Main Functions

The main function of this software is `prime_fib(n: int) -> int`, which returns the n-th Fibonacci number that is also a prime number. The function uses a generator to produce Fibonacci numbers and checks each one for primality until it finds the desired count of prime Fibonacci numbers.

### Key Components

- **`is_prime(num: int) -> bool`**: A helper function that checks if a given number is prime.
- **`fibonacci_generator()`**: A generator function that yields Fibonacci numbers indefinitely.
- **`prime_fib(n: int) -> int`**: The main function that returns the n-th prime Fibonacci number.

## Installation

This software does not require any external dependencies. It is implemented using standard Python libraries, making it easy to set up and run.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required as there are no external dependencies.

## Usage

To use the software, simply run the `main.py` script. You can test the `prime_fib` function using the built-in doctests.

### Running the Script

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the script using Python:

   ```bash
   python main.py
   ```

This will execute the doctests included in the script, verifying that the `prime_fib` function works as expected.

### Example Usage

You can also use the `prime_fib` function directly in your Python code:

```python
from main import prime_fib

# Get the 5th prime Fibonacci number
result = prime_fib(5)
print(result)  # Output: 89
```

## Documentation

For further documentation, you can refer to the docstrings provided in the code. These docstrings include examples and explanations of how each function works.

This software is designed to be simple and straightforward, making it easy for developers to integrate the `prime_fib` function into their own projects or use it for educational purposes.