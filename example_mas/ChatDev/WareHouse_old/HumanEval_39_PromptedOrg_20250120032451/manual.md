# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `prime_fib(n: int) -> int`

- **Description**: This function returns the n-th Fibonacci number that is also a prime number.
- **Parameters**: 
  - `n` (int): The position of the prime Fibonacci number you want to find.
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

This software does not require any external libraries or dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Move into the directory where the code is located:
   ```bash
   cd <directory-name>
   ```

4. **Run the Code**: You can run the code directly using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are using this function in another script, import it:
   ```python
   from main import prime_fib
   ```

2. **Call the Function**: Use the `prime_fib` function by passing the desired position of the prime Fibonacci number:
   ```python
   result = prime_fib(5)
   print(result)  # Output will be 89
   ```

## Documentation

The code is documented with docstrings and inline comments to help understand the logic and flow. The main logic involves generating Fibonacci numbers and checking for primality until the desired n-th prime Fibonacci number is found.

For further assistance or questions, please refer to the comments within the code or contact the development team.