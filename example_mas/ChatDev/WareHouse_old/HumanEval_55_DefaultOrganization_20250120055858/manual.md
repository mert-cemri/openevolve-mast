# Fibonacci Calculator

This software module provides a simple function to calculate the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. This module is implemented in Python and is designed to be easy to use and integrate into other projects.

## Main Function

The main function provided by this module is `fib(n: int) -> int`, which calculates and returns the n-th Fibonacci number.

### Function Details

- **Function Name:** `fib`
- **Parameters:** 
  - `n` (int): The position in the Fibonacci sequence (must be a positive integer).
- **Returns:** 
  - The n-th Fibonacci number.
- **Example Usage:**
  ```python
  >>> fib(10)
  55
  >>> fib(1)
  1
  >>> fib(8)
  21
  ```

## Installation

This module does not require any external dependencies, making it straightforward to install and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:** Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:** Obtain the source code by cloning the repository or downloading the files directly.

3. **Navigate to the Project Directory:** Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open a Python Environment:** You can use a Python interactive shell, a script, or an integrated development environment (IDE) like PyCharm or VSCode.

2. **Import the Function:**
   ```python
   from main import fib
   ```

3. **Call the Function:**
   Use the `fib` function to calculate the n-th Fibonacci number by passing a positive integer as an argument.
   ```python
   result = fib(10)
   print(result)  # Output: 55
   ```

## Error Handling

- The function will raise a `ValueError` if the input `n` is not a positive integer. Ensure that you pass a valid positive integer to avoid this error.

## Conclusion

This module provides a simple and efficient way to calculate Fibonacci numbers. It is designed to be easy to integrate into other Python projects and requires no additional dependencies. Enjoy using the Fibonacci Calculator in your applications!