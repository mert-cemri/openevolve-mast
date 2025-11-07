manual.md

```
# Any_Int Function

A simple Python function to determine if one of three given numbers is equal to the sum of the other two, with the condition that all numbers must be integers.

## Overview

The `any_int` function is designed to take three numbers as input and return `True` if one of the numbers is equal to the sum of the other two, provided all numbers are integers. If any of the numbers are not integers, or if no number equals the sum of the other two, the function returns `False`.

### Function Signature

```python
def any_int(x, y, z):
```

### Examples

- `any_int(5, 2, 7)` returns `True` because 5 + 2 = 7.
- `any_int(3, 2, 2)` returns `False` because no number equals the sum of the other two.
- `any_int(3, -2, 1)` returns `True` because 3 + (-2) = 1.
- `any_int(3.6, -2.2, 2)` returns `False` because not all numbers are integers.

## Installation

This function does not require any external dependencies, so no installation of additional packages is necessary. You only need Python installed on your system.

### Python Installation

Ensure you have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

## Usage

1. **Create a Python Script:**

   Create a new Python file, for example, `main.py`, and include the `any_int` function code:

   ```python
   def any_int(x, y, z):
       # Check if all numbers are integers
       if not all(isinstance(i, int) for i in (x, y, z)):
           return False
       # Check if one of the numbers is equal to the sum of the other two
       return x == y + z or y == x + z or z == x + y
   ```

2. **Call the Function:**

   You can call the `any_int` function with your desired inputs:

   ```python
   print(any_int(5, 2, 7))  # Output: True
   print(any_int(3, 2, 2))  # Output: False
   ```

3. **Run the Script:**

   Execute your script using a Python interpreter:

   ```bash
   python main.py
   ```

## Conclusion

The `any_int` function is a straightforward utility to check the relationship between three integers. It is easy to integrate into larger projects or use as a standalone utility for quick checks. Since it requires no external libraries, it is lightweight and efficient for use in various Python environments.
```