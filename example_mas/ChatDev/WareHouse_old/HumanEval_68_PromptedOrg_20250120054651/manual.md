# Pluck Function User Manual

Welcome to the user manual for the `pluck` function. This document will guide you through the main functionality of the software, how to set up your environment, and how to use the function effectively.

## Introduction

The `pluck` function is designed to process an array of non-negative integers and identify the smallest even value within the array. If multiple nodes with the same smallest even value are found, the function will return the node that has the smallest index. The result is returned as a list containing the smallest even value and its index. If there are no even values or the array is empty, the function returns an empty list.

## Main Functionality

- **Identify the Smallest Even Value**: The function scans through the array to find the smallest even number.
- **Return the Index**: Along with the smallest even value, the function returns the index of this value.
- **Handle Edge Cases**: If the array is empty or contains no even numbers, the function returns an empty list.

## Installation

The `pluck` function does not require any external dependencies, making it straightforward to use. You only need a Python environment to run the function.

### Setting Up Your Environment

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **No Additional Libraries Required**: Since there are no external dependencies, you don't need to install any additional libraries.

## How to Use the `pluck` Function

1. **Copy the Code**: Ensure you have the `pluck` function code in your Python script or environment.

```python
def pluck(arr):
    smallest_even = None
    smallest_index = None
    for index, value in enumerate(arr):
        if value % 2 == 0:  # Check if the number is even
            if smallest_even is None or value < smallest_even:
                smallest_even = value
                smallest_index = index
    if smallest_even is not None:
        return [smallest_even, smallest_index]
    else:
        return []
```

2. **Call the Function**: Pass an array of non-negative integers to the function.

```python
result = pluck([4, 2, 3])
print(result)  # Output: [2, 1]
```

3. **Interpret the Output**: The function will return a list containing the smallest even value and its index. If no even values are found, it will return an empty list.

## Examples

- **Example 1**: Input: `[4, 2, 3]` -> Output: `[2, 1]`
- **Example 2**: Input: `[1, 2, 3]` -> Output: `[2, 1]`
- **Example 3**: Input: `[]` -> Output: `[]`
- **Example 4**: Input: `[5, 0, 3, 0, 4, 2]` -> Output: `[0, 1]`

## Conclusion

The `pluck` function is a simple yet effective tool for identifying the smallest even value in an array of non-negative integers. With no external dependencies, it is easy to integrate into any Python project. Follow the instructions in this manual to set up and use the function effectively.