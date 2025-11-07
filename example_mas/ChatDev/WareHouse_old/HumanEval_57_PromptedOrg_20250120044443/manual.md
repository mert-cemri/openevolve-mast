# Monotonic List Checker

This software module provides a function to check if a list of numbers is monotonically increasing or decreasing. It is a simple utility that can be used in various applications where such a check is necessary.

## Main Functionality

The main function provided by this module is `monotonic(l: list)`. This function takes a list of numbers as input and returns `True` if the list is either monotonically increasing or monotonically decreasing. Otherwise, it returns `False`.

### Function Definition

```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if not l:
        return True
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            decreasing = False
        if l[i] < l[i - 1]:
            increasing = False
    return increasing or decreasing
```

## Installation

This module does not require any external dependencies, making it easy to integrate into your existing Python projects.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python environment. Simply copy the function into your Python script or module.

## Usage

To use the `monotonic` function, simply pass a list of numbers to it. Here are some examples:

```python
print(monotonic([1, 2, 4, 20]))  # Output: True
print(monotonic([1, 20, 4, 10])) # Output: False
print(monotonic([4, 1, 0, -10])) # Output: True
```

## Documentation

This function is self-contained and does not require additional documentation. The docstring within the function provides examples of how to use it.

For further assistance or inquiries, please contact our support team.