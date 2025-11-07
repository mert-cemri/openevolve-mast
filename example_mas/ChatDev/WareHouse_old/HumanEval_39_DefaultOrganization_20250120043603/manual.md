manual.md

```
# Prime Fibonacci Finder

This software provides a function to find the n-th number that is both a Fibonacci number and a prime number. It is implemented in Python and does not require any external dependencies.

## Main Function

### `prime_fib(n: int)`

- **Description**: This function returns the n-th number that is both a Fibonacci number and a prime number.
- **Parameters**: 
  - `n` (int): The position of the desired prime Fibonacci number in the sequence.
- **Returns**: 
  - An integer representing the n-th prime Fibonacci number.
- **Examples**:
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

This software does not require any external dependencies, so you can run it with a standard Python installation.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone or download the repository containing the `main.py` file.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `main.py` file.
3. Run the Python interpreter and import the `prime_fib` function:
   ```bash
   python
   >>> from main import prime_fib
   ```
4. Use the `prime_fib` function to find the desired prime Fibonacci number:
   ```python
   >>> prime_fib(1)
   2
   >>> prime_fib(5)
   89
   ```

## Documentation

For further information on how the function works, you can refer to the docstring within the `main.py` file. The docstring provides a brief description of the function, its parameters, and examples of usage.

This software is designed to be simple and efficient, focusing solely on the task of finding prime Fibonacci numbers without any additional features or interfaces.
```