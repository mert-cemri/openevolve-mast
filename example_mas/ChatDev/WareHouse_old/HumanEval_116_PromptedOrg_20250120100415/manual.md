# Sort Array User Manual

Welcome to the Sort Array software! This software provides a function to sort an array of integers based on specific criteria. This manual will guide you through the main functions of the software, how to install environment dependencies, and how to use the function effectively.

## Main Functionality

The primary function of this software is `sort_array`, which sorts an array of integers according to the following rules:

1. **Non-negative Integers**: These are sorted based on the number of ones in their binary representation. If two numbers have the same number of ones, they are sorted by their decimal value.
2. **Negative Integers**: These are sorted by their decimal value in ascending order.

### Function Signature

```python
def sort_array(arr):
    """
    Sort an array of integers according to the number of ones in their binary representation for non-negative numbers.
    For numbers with the same number of ones, sort them by their decimal value.
    Negative numbers should be sorted by their decimal value.
    Args:
    arr (list): A list of integers.
    Returns:
    list: A sorted list of integers.
    """
```

### Examples

- `sort_array([1, 5, 2, 3, 4])` returns `[1, 2, 3, 4, 5]`
- `sort_array([-2, -3, -4, -5, -6])` returns `[-6, -5, -4, -3, -2]`
- `sort_array([1, 0, 2, 3, 4])` returns `[0, 1, 2, 3, 4]`

## Installation

This software does not require any external dependencies, so there is no need for a `requirements.txt` file. You can directly use the function in your Python environment.

### Quick Start

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Code**: You can use the function directly in your Python scripts or interactive environment.
   ```python
   from main import sort_array

   # Example usage
   result = sort_array([1, 5, 2, 3, 4])
   print(result)  # Output: [1, 2, 3, 4, 5]
   ```

## Usage

To use the `sort_array` function, simply pass a list of integers to it. The function will return a new list sorted according to the specified rules.

```python
# Example
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sort_array(numbers)
print(sorted_numbers)
```

## Conclusion

The Sort Array software provides a simple yet powerful function to sort arrays of integers based on binary representation and decimal values. With no external dependencies, it is easy to integrate into any Python project. Enjoy sorting your arrays with ease!