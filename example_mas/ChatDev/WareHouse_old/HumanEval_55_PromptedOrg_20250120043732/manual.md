# Fibonacci Calculator

This software module provides a function to calculate the n-th Fibonacci number. It is a simple and efficient implementation that can be used in various applications where Fibonacci numbers are required.

## Main Function

The main function provided by this software is:

- `fib(n: int) -> int`: This function returns the n-th Fibonacci number. It raises a `ValueError` if the input `n` is not a positive integer.

### Example Usage

```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```

## Installation

This module does not require any external dependencies. It is implemented purely in Python, so you only need a Python environment to run it.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the module to your local machine.

3. Navigate to the directory containing the `main.py` file.

4. You can now use the `fib` function in your Python scripts or interactive shell.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where the `main.py` file is located.

3. Open a Python interactive shell by typing `python` and pressing Enter.

4. Import the `fib` function from the `main.py` file:

   ```python
   from main import fib
   ```

5. Call the `fib` function with a positive integer to get the corresponding Fibonacci number:

   ```python
   print(fib(10))  # Output: 55
   ```

6. If you input a non-positive integer, the function will raise a `ValueError`:

   ```python
   print(fib(0))  # Raises ValueError: n must be a positive integer
   ```

## Documentation

This module is straightforward and does not require extensive documentation. The function is self-explanatory and follows standard Python practices for error handling and input validation.

For any further questions or support, please contact our support team.