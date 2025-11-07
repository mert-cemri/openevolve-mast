# FibFib Sequence Calculator

This software module provides an efficient implementation of the FibFib number sequence, which is similar to the Fibonacci sequence but with a different recursive definition. The FibFib sequence is defined as follows:

- fibfib(0) == 0
- fibfib(1) == 0
- fibfib(2) == 1
- fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n >= 3

## Main Function

The main function provided in this module is `fibfib(n: int) -> int`, which computes the n-th element of the FibFib number sequence.

### Usage

To use the `fibfib` function, simply call it with an integer `n` as an argument, where `n` is the position in the FibFib sequence you wish to compute. For example:

```python
result = fibfib(5)
print(result)  # Output: 4
```

## Installation

This module does not require any external dependencies, so there is no need to install additional packages. You can directly use the provided `main.py` file in your Python environment.

### Quick Start

1. **Clone the repository or download the `main.py` file** to your local machine.

2. **Run the Python script** using your preferred Python environment. Ensure you have Python installed on your system.

3. **Execute the function** by calling `fibfib(n)` with your desired input.

## Example

Here is an example of how to use the `fibfib` function:

```python
# Import the function from the module
from main import fibfib

# Compute the 8th element of the FibFib sequence
result = fibfib(8)
print(f"The 8th element of the FibFib sequence is: {result}")
```

## Documentation

The function is documented with a docstring that explains its purpose and provides example usage. You can view this documentation directly in the `main.py` file.

For further questions or support, please contact our development team. We are here to assist you in integrating and utilizing the FibFib sequence calculator in your projects.