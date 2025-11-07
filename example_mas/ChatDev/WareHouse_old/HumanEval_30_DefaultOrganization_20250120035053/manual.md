# Positive Number Filter

This software module provides a simple function to filter and return only positive numbers from a given list. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this module is `get_positive`, which takes a list of numbers as input and returns a list containing only the positive numbers from the input list.

### Function Signature

```python
def get_positive(l: list) -> list:
```

### Example Usage

```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

## Installation

This module does not require any external dependencies, making it straightforward to use. You only need to have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `get_positive` function.

2. **Run the Function**: You can use the function directly in a Python script or an interactive Python session.

   - Open a terminal or command prompt.
   - Navigate to the directory containing `main.py`.
   - Start a Python session by typing `python` and pressing Enter.
   - Import the function and use it as shown in the example usage.

```python
from main import get_positive

# Example usage
positive_numbers = get_positive([-1, 2, -4, 5, 6])
print(positive_numbers)  # Output: [2, 5, 6]
```

## Documentation

For further details on Python programming and list comprehensions, you can refer to the [official Python documentation](https://docs.python.org/3/).

This module is designed to be simple and efficient, providing a quick solution for filtering positive numbers from a list. Feel free to integrate it into larger projects or use it as a standalone utility.