# Fibonacci Calculator

This software module provides a function to calculate the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. This module allows you to compute the n-th Fibonacci number efficiently.

## Main Function

The main function provided by this module is `fib(n: int) -> int`. This function returns the n-th Fibonacci number, where `n` is a positive integer.

### Function Signature

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
```

### Example Usage

```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```

### Function Behavior

- If `n` is less than or equal to 0, the function raises a `ValueError` indicating that `n` must be a positive integer.
- If `n` is 1 or 2, the function returns 1, as the first two Fibonacci numbers are both 1.
- For `n` greater than 2, the function calculates the Fibonacci number using an iterative approach for efficiency.

## Installation

To use this module, you need to have Python installed on your system. This module does not require any external dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Module**: You can clone the repository or download the `main.py` file containing the Fibonacci function.

3. **Run the Function**: You can run the function in a Python environment or script by importing the `fib` function from `main.py`.

## How to Use

1. **Import the Function**: In your Python script or interactive shell, import the `fib` function.

    ```python
    from main import fib
    ```

2. **Call the Function**: Use the `fib` function by passing a positive integer to get the corresponding Fibonacci number.

    ```python
    result = fib(10)
    print(result)  # Output will be 55
    ```

3. **Error Handling**: Ensure that the input `n` is a positive integer to avoid `ValueError`.

## Documentation

This module is straightforward and does not require additional documentation beyond the function's docstring and this manual. If you have any questions or need further assistance, please contact our support team.

Enjoy calculating Fibonacci numbers with ease!