manual.md

```
# Simple Power Checker

This software provides a function to determine if a given number is a simple power of another number. It is implemented in Python and is designed to be lightweight with no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `is_simple_power` function. This function checks if a number `x` is a simple power of another number `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

### Function Definition

```python
def is_simple_power(x, n):
    """Returns True if x is a simple power of n, otherwise False."""
```

### Example Usage

- `is_simple_power(1, 4)` returns `True` because 1 is 4**0.
- `is_simple_power(2, 2)` returns `True` because 2 is 2**1.
- `is_simple_power(8, 2)` returns `True` because 8 is 2**3.
- `is_simple_power(3, 2)` returns `False` because there is no integer k such that 2**k = 3.
- `is_simple_power(3, 1)` returns `False` because 1 raised to any power is always 1.
- `is_simple_power(5, 3)` returns `False` because there is no integer k such that 3**k = 5.

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

To use the function, simply download the `main.py` file and run it in your Python environment.

## How to Use

1. **Download the Code:**
   - Obtain the `main.py` file containing the `is_simple_power` function.

2. **Run the Function:**
   - Open a Python interpreter or script.
   - Import the function from the `main.py` file.
   - Call the function with your desired values for `x` and `n`.

Example:

```python
from main import is_simple_power

result = is_simple_power(8, 2)
print(result)  # Output: True
```

## Documentation

For further information on Python and its capabilities, please refer to the [official Python documentation](https://docs.python.org/3/).

This software is designed to be simple and efficient, providing a straightforward solution to check if a number is a simple power of another number.
```