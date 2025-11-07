# Fibonacci Number Calculator

This software module provides a function to calculate the n-th Fibonacci number. It is a simple and efficient implementation designed for educational and practical purposes.

## Main Function

The main function provided by this module is:

- `fib(n: int) -> int`: This function returns the n-th Fibonacci number. It uses an iterative approach to calculate the Fibonacci sequence, which is efficient and avoids the overhead of recursive function calls.

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

This module does not require any external dependencies, making it straightforward to use in any Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the module in your Python environment. Ensure you have Python installed on your system.

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the Fibonacci function.

2. **Run the Python Script**: You can use the function directly in your Python scripts or interactive shell.

## How to Use

1. **Import the Function**: If you have the `main.py` file in your project directory, you can import the `fib` function.

    ```python
    from main import fib
    ```

2. **Call the Function**: Use the `fib` function by passing an integer `n` to get the n-th Fibonacci number.

    ```python
    result = fib(10)
    print(result)  # Output: 55
    ```

3. **Testing**: You can test the function using the provided examples to ensure it works as expected.

## Documentation

This module is designed to be simple and self-contained. For further information or support, you can refer to Python's standard library documentation for additional context on iterative algorithms and integer operations.

Feel free to modify and extend the code to suit your specific needs or to integrate it into larger projects.