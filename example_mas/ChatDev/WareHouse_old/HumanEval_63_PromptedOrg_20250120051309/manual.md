# FibFib Sequence Calculator

This software provides a function to compute the n-th element of the FibFib number sequence, a sequence similar to the Fibonacci sequence but with a unique definition. This user manual will guide you through the main functions of the software, how to install environment dependencies, and how to use the function.

## Main Function

### fibfib(n: int) -> int

The `fibfib` function computes the n-th element of the FibFib number sequence. The sequence is defined as follows:

- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- For `n >= 3`, `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

#### Parameters:
- `n (int)`: The index of the sequence to compute.

#### Returns:
- `int`: The n-th element of the FibFib sequence.

#### Examples:
```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```

## Installation

This software does not have any external dependencies, so you can use it directly in a Python environment. However, ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the `main.py` file containing the `fibfib` function.

## Usage

1. **Open a Python Environment**: You can use any Python IDE or a simple command-line interface.

2. **Import the Function**: If you have saved the `main.py` file in your working directory, you can import the function using:
   ```python
   from main import fibfib
   ```

3. **Compute the FibFib Sequence**: Call the `fibfib` function with the desired index to compute the n-th element of the sequence.
   ```python
   result = fibfib(5)
   print(result)  # Output will be 4
   ```

## Documentation

For further details and examples, refer to the docstring provided within the `main.py` file. This includes comprehensive examples and explanations of the function's behavior.

This concludes the user manual for the FibFib Sequence Calculator. Enjoy computing the FibFib sequence!