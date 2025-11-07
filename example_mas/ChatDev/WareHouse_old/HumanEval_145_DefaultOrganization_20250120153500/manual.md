manual.md

```
# Order By Points

A Python utility to sort a list of integers based on the sum of their digits. If two numbers have the same digit sum, they maintain their original order.

## Overview

The `order_by_points` function is designed to sort a list of integers in ascending order according to the sum of their digits. This utility is particularly useful when you need to prioritize numbers based on their digit sum while preserving the original order for numbers with the same sum.

### Key Features

- **Digit Sum Sorting**: Sorts integers based on the sum of their digits.
- **Stable Sorting**: Maintains the original order for numbers with the same digit sum.
- **Simple and Lightweight**: No external dependencies required.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Setting Up the Environment

Since there are no external dependencies required for this utility, you can directly use the provided Python script without any additional setup.

## Usage

### Function Definition

```python
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.
    Args:
    nums (list of int): The list of integers to sort.
    Returns:
    list of int: The sorted list of integers.
    """
```

### Example Usage

To use the `order_by_points` function, simply call it with a list of integers. Here are some examples:

```python
# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # Output: []
```

### How It Works

1. **Digit Sum Calculation**: The function calculates the sum of digits for each integer in the list.
2. **Sorting**: The list is sorted based on these sums. If two numbers have the same digit sum, they retain their original order in the list.

## Conclusion

The `order_by_points` utility is a straightforward and efficient way to sort integers based on the sum of their digits. With no external dependencies, it is easy to integrate into any Python project. Simply include the function in your code and use it as needed to achieve your sorting requirements.
```