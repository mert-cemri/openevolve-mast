# Fib4 Sequence Calculator

This software module provides an implementation of the `fib4` function, which computes the n-th element of the Fib4 number sequence. The Fib4 sequence is a variation of the Fibonacci sequence with a unique definition.

## Main Functions

### `fib4(n: int) -> int`

This function computes the n-th element of the Fib4 number sequence. The sequence is defined as follows:

- `fib4(0) -> 0`
- `fib4(1) -> 0`
- `fib4(2) -> 2`
- `fib4(3) -> 0`
- For `n >= 4`, `fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`

#### Arguments:
- `n (int)`: The index of the sequence to compute.

#### Returns:
- `int`: The n-th element of the Fib4 sequence.

#### Examples:
```python
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
```

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly use the provided code.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can run the `fib4` function directly in a Python environment or script.

## Usage

To use the `fib4` function, simply import it into your Python script or interactive session and call it with the desired index `n`.

Example usage:
```python
from main import fib4

# Compute the 5th element of the Fib4 sequence
result = fib4(5)
print(result)  # Output: 4
```

## Documentation

For further details on how the function works and additional examples, please refer to the docstring within the `main.py` file. The docstring provides comprehensive information on the function's behavior and expected outputs for various inputs.

This software is designed to be simple and efficient, focusing solely on computing the Fib4 sequence without any unnecessary features or dependencies.