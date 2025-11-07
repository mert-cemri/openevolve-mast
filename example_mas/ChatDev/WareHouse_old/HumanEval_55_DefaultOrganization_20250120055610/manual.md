# Fibonacci Calculator

This software module provides a simple function to compute the n-th Fibonacci number. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Function

The main function provided by this software is `fib(n: int) -> int`. This function calculates and returns the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. In this implementation, the sequence starts with 1 and 1.

### Function Signature

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
```

### Example Usage

Here are some examples of how to use the `fib` function:

```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Script**: You can run the script directly using Python. There are no additional installation steps required.

## How to Use

1. **Open a Terminal**: Open your terminal or command prompt.

2. **Navigate to the Script Location**: Use the `cd` command to navigate to the directory containing `main.py`.

3. **Run the Script**: Execute the script using Python to test the function with the built-in doctests.

   ```bash
   python main.py
   ```

   This will run the doctests included in the `fib` function's docstring to verify that the function works as expected.

4. **Use the Function in Your Code**: You can import the `fib` function into your own Python scripts to compute Fibonacci numbers as needed.

   ```python
   from main import fib

   result = fib(10)
   print(result)  # Output: 55
   ```

## Documentation

The function is documented within the code using Python docstrings. You can view these docstrings for more information on how the function works and its expected input and output.

For any further questions or support, please refer to the comments within the code or contact the development team.