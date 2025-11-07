manual.md

```
# Monotonic List Checker

This software provides a simple utility function to determine if a list of numbers is monotonically increasing or decreasing. It is implemented in Python and does not require any external dependencies.

## Quick Install

Since there are no external dependencies required for this software, you can simply run the Python script without any additional installation steps.

## 🤔 What is this?

The Monotonic List Checker is a Python function that checks if the elements of a list are either entirely non-increasing or non-decreasing. This can be useful in various data analysis tasks where the order of data points is significant.

### Main Functionality

- **monotonic(l: list)**: This function takes a list of numbers as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise.

### Example Usage

```python
from main import monotonic

# Example 1: Monotonically increasing list
print(monotonic([1, 2, 4, 20]))  # Output: True

# Example 2: Non-monotonic list
print(monotonic([1, 20, 4, 10]))  # Output: False

# Example 3: Monotonically decreasing list
print(monotonic([4, 1, 0, -10]))  # Output: True
```

## 📖 Documentation

### Function Details

- **monotonic(l: list)**:
  - **Parameters**: 
    - `l` (list): A list of numbers to be checked for monotonicity.
  - **Returns**: 
    - `bool`: `True` if the list is monotonically increasing or decreasing, `False` otherwise.
  - **Examples**:
    - `monotonic([1, 2, 4, 20])` returns `True`
    - `monotonic([1, 20, 4, 10])` returns `False`
    - `monotonic([4, 1, 0, -10])` returns `True`

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Run the Script**: Use a Python interpreter to run the `main.py` script.
3. **Test the Function**: You can test the function using the examples provided above or with your own list of numbers.

This software is designed to be simple and efficient, making it easy to integrate into larger projects or use as a standalone utility.
```