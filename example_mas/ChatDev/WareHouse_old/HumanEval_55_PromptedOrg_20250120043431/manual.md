# Fibonacci Calculator

This software module provides a function to calculate the n-th Fibonacci number. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is:

- `fib(n: int) -> int`: This function takes an integer `n` as input and returns the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. In this implementation, the sequence starts with 1 and 1.

### Usage Examples

```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```

## Installation

Since this software does not require any external dependencies, you can directly use the provided Python code. Ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the Fibonacci function.

3. **Run the code**: You can run the code using a Python interpreter. Open a terminal or command prompt and navigate to the directory containing `main.py`. Use the following command to execute the script:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the function**: If you want to use the `fib` function in another Python script, you can import it as follows:

   ```python
   from main import fib
   ```

2. **Call the function**: Use the `fib` function by passing an integer `n` to get the n-th Fibonacci number.

   ```python
   result = fib(10)
   print(result)  # Output: 55
   ```

## Error Handling

- The function raises a `ValueError` if the input `n` is less than or equal to 0, as the Fibonacci sequence is defined for positive integers only.

## Documentation

For further information and examples, please refer to the docstring within the `main.py` file, which provides additional usage examples and details about the function's behavior.