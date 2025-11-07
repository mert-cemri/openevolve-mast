```markdown
# Fibonacci Calculator

This software module provides a simple function to calculate the n-th Fibonacci number. It is designed to be lightweight and efficient, requiring no external dependencies.

## Quick Install

Since this module does not require any external dependencies, you can directly use the provided `main.py` file in your Python environment.

## 🤔 What is this?

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. This module provides a function to calculate the n-th Fibonacci number, which is a common mathematical problem with applications in various fields such as computer science, mathematics, and finance.

## Main Function

### `fib(n: int) -> int`

- **Description**: This function returns the n-th Fibonacci number.
- **Parameters**: 
  - `n` (int): The position in the Fibonacci sequence (must be a positive integer).
- **Returns**: 
  - The n-th Fibonacci number.
- **Example Usage**:
  ```python
  >>> fib(10)
  55
  >>> fib(1)
  1
  >>> fib(8)
  21
  ```

## How to Use

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Download the Code**: Save the `main.py` file to your local machine.

3. **Run the Code**: You can run the code in a Python environment. Open a terminal or command prompt and navigate to the directory where `main.py` is located. Use the Python interpreter to execute the file or import the function into your own scripts.

   Example:
   ```bash
   python main.py
   ```

   Or, if you want to use the function in another script:
   ```python
   from main import fib

   print(fib(10))  # Output: 55
   ```

## Documentation

For further information on the Fibonacci sequence and its applications, you can refer to resources such as:

- [Wikipedia: Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)
- [Math is Fun: Fibonacci Sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html)

This module is designed to be simple and efficient, making it easy to integrate into larger projects or use as a standalone tool for educational purposes.
```