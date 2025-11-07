# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main functionality of this software is encapsulated in the `prime_fib` function. This function takes an integer `n` as input and returns the n-th Fibonacci number that is also a prime number.

### Function: `prime_fib(n: int) -> int`

- **Description**: Returns the n-th number that is both a Fibonacci number and a prime number.
- **Parameters**: 
  - `n` (int): The position of the desired prime Fibonacci number in the sequence of prime Fibonacci numbers.
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

This software does not require any external libraries or dependencies. It is implemented using Python's built-in capabilities. Ensure you have Python installed on your system.

### Steps to Install Python

1. **Download Python**: Visit the official [Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.
2. **Install Python**: Follow the installation instructions provided on the website for your specific operating system.
3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.
2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.
3. **Run the Script**: You can use the Python interpreter to run the script and test the `prime_fib` function.

### Example

To find the 5th prime Fibonacci number, you can run the following command in your terminal:

```bash
python -c "from main import prime_fib; print(prime_fib(5))"
```

This command will output `89`, which is the 5th prime Fibonacci number.

## Conclusion

This software provides a simple and efficient way to find prime Fibonacci numbers using Python. It is designed to be easy to use and does not require any additional setup beyond having Python installed on your system.