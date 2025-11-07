# Positive Number Filter

This software module is designed to filter and return only positive numbers from a given list. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this module is `get_positive`, which takes a list of numbers as input and returns a list containing only the positive numbers from the input list.

### Function Signature

```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
```

### Example Usage

```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

## Installation

This module does not require any external libraries or dependencies, making it easy to integrate into your existing Python environment.

### Quick Install

Since there are no dependencies, you can simply copy the `main.py` file into your project directory.

## How to Use

1. **Copy the Code**: Copy the `main.py` file containing the `get_positive` function into your project directory.

2. **Import the Function**: In your Python script, import the `get_positive` function.

   ```python
   from main import get_positive
   ```

3. **Call the Function**: Use the `get_positive` function by passing a list of numbers to it.

   ```python
   positive_numbers = get_positive([-1, 2, -4, 5, 6])
   print(positive_numbers)  # Output: [2, 5, 6]
   ```

## Documentation

The function is straightforward and does not require additional documentation beyond the examples provided. It is designed to be simple and efficient, leveraging Python's list comprehension for filtering.

For any further questions or support, please refer to the comments within the code or contact the development team.