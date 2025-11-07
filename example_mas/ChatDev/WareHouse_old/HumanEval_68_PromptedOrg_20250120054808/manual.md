# Pluck Function User Manual

Welcome to the user manual for the `pluck` function. This document will guide you through the main features of the software, how to install it, and how to use it effectively.

## Overview

The `pluck` function is designed to process an array of non-negative integer nodes, representing a branch of a tree. The function identifies and returns the node with the smallest even value. If multiple nodes have the same smallest even value, the function returns the node with the smallest index. If there are no even values or the array is empty, the function returns an empty list.

### Main Features

- **Identify Smallest Even Node**: The function finds the smallest even node in the array.
- **Return Node with Smallest Index**: In case of ties, it returns the node with the smallest index.
- **Handles Empty Arrays**: If the array is empty or contains no even numbers, it returns an empty list.

## Installation

The `pluck` function is a standalone Python function and does not require any external dependencies. You can simply copy the function into your Python script and use it. There is no need to install any additional packages.

### Requirements

- Python 3.x

## Usage

To use the `pluck` function, follow these steps:

1. **Copy the Function**: Copy the `pluck` function code into your Python script.

2. **Call the Function**: Pass an array of non-negative integers to the function.

3. **Receive Output**: The function will return a list containing the smallest even value and its index, or an empty list if no even values are found.

### Example Usage

```python
def pluck(arr):
    # Initialize variables to track the smallest even value and its index
    smallest_even = None
    smallest_index = None
    # Iterate through the array
    for index, value in enumerate(arr):
        # Check if the value is even
        if value % 2 == 0:
            # If it's the first even number or smaller than the current smallest even
            if smallest_even is None or value < smallest_even:
                smallest_even = value
                smallest_index = index
    # If a smallest even value was found, return it with its index
    if smallest_even is not None:
        return [smallest_even, smallest_index]
    # If no even value was found, return an empty list
    return []

# Example 1
print(pluck([4, 2, 3]))  # Output: [2, 1]

# Example 2
print(pluck([1, 2, 3]))  # Output: [2, 1]

# Example 3
print(pluck([]))  # Output: []

# Example 4
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```

## Conclusion

The `pluck` function is a simple yet effective tool for identifying the smallest even node in an array of non-negative integers. With no external dependencies, it is easy to integrate into your Python projects. Simply copy the function and start using it to process your data.