# Unique Function User Manual

## Introduction

The `unique` function is a simple Python utility designed to return sorted unique elements from a list. This function is particularly useful when you need to remove duplicates from a list and sort the remaining elements in ascending order.

## Main Functionality

- **Function Name**: `unique`
- **Purpose**: To return sorted unique elements from a given list.
- **Input**: A list of elements (e.g., integers).
- **Output**: A list of sorted unique elements.

### Example Usage

```python
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
```

## Installation

This function does not require any external dependencies, making it easy to integrate into your existing Python projects. Simply copy the function into your Python script or module where you need to use it.

### Requirements

- Python 3.x

## How to Use

1. **Copy the Function**: Copy the `unique` function from the provided code into your Python script.

2. **Call the Function**: Use the function by passing a list of elements as an argument. The function will return a new list containing sorted unique elements.

### Example

```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage
result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(result)  # Output: [0, 2, 3, 5, 9, 123]
```

## Notes

- The function uses Python's built-in `set` to remove duplicates and `sorted` to sort the elements.
- The function is designed to work with lists containing elements that are comparable and hashable, such as integers and strings.

By following this manual, you should be able to effectively use the `unique` function in your Python projects to manage lists by removing duplicates and sorting the elements.