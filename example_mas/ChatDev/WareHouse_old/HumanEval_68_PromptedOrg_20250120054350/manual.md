# Pluck Function User Manual

Welcome to the user manual for the `pluck` function, a simple yet efficient Python function designed to identify and return the smallest even number from a list of non-negative integers, along with its index. This document will guide you through the installation process, usage, and functionality of the `pluck` function.

## Quick Install

The `pluck` function does not require any external dependencies, so there is no need to install additional packages. Simply ensure you have Python installed on your system.

## 🤔 What is this?

The `pluck` function is a utility that processes an array of non-negative integers, representing nodes of a tree branch, and returns the smallest even node value along with its index. If there are multiple nodes with the same smallest even value, the function returns the one with the smallest index. If no even values are present or the array is empty, it returns an empty list.

## 📖 How to Use the Pluck Function

### Function Definition

```python
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.
    The plucked node should be returned in a list, [smallest_value, its index].
    If there are no even values or the given array is empty, return [].
    """
```

### Usage

1. **Input**: Provide a list of non-negative integers to the `pluck` function.
2. **Output**: The function returns a list containing the smallest even value and its index. If no even values are found, it returns an empty list.

### Examples

- **Example 1**:
  - **Input**: `[4, 2, 3]`
  - **Output**: `[2, 1]`
  - **Explanation**: The smallest even value is 2, located at index 1.

- **Example 2**:
  - **Input**: `[1, 2, 3]`
  - **Output**: `[2, 1]`
  - **Explanation**: The smallest even value is 2, located at index 1.

- **Example 3**:
  - **Input**: `[]`
  - **Output**: `[]`
  - **Explanation**: The array is empty, so no even values are present.

- **Example 4**:
  - **Input**: `[5, 0, 3, 0, 4, 2]`
  - **Output**: `[0, 1]`
  - **Explanation**: The smallest even value is 0, and the first occurrence is at index 1.

### Constraints

- The length of the input array should be between 1 and 10,000.
- All node values should be non-negative integers.

## Conclusion

The `pluck` function is a straightforward tool for identifying the smallest even number in a list and its index. It is efficient and easy to integrate into larger applications or use as a standalone utility. With no external dependencies, it is ready to use with any standard Python environment.