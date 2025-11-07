# get_positive Function User Manual

Welcome to the user manual for the `get_positive` function. This function is designed to filter and return only the positive numbers from a given list of integers.

## Overview

The `get_positive` function is a simple utility that processes a list of integers and returns a new list containing only the positive numbers from the original list. This can be particularly useful in data processing tasks where you need to isolate positive values for further analysis or operations.

## Quick Install

The `get_positive` function is implemented in Python and does not require any external dependencies. You can use it directly in your Python environment.

### Requirements

- Python 3.x

### Installation

Since there are no external dependencies, you can simply copy the function into your Python script or interactive environment to use it.

## Usage

### Function Definition

```python
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]
```

### How to Use

1. **Import or Define the Function**: Ensure the function is available in your script or interactive session. You can copy the function definition provided above.

2. **Call the Function**: Pass a list of integers to the `get_positive` function to retrieve a list of positive numbers.

   ```python
   # Example usage
   positive_numbers = get_positive([-1, 2, -4, 5, 6])
   print(positive_numbers)  # Output: [2, 5, 6]
   ```

3. **Interpret the Results**: The function will return a new list containing only the positive integers from the input list.

### Examples

```python
# Example 1
result1 = get_positive([-1, 2, -4, 5, 6])
print(result1)  # Output: [2, 5, 6]

# Example 2
result2 = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(result2)  # Output: [5, 3, 2, 3, 9, 123, 1]
```

## Conclusion

The `get_positive` function is a straightforward and efficient tool for filtering positive numbers from a list. With no external dependencies, it is easy to integrate into any Python project. Use this function to streamline your data processing tasks and focus on positive values.