manual.md

```
# Odd Elements Sum Calculator

This software provides a simple function to calculate the sum of all odd integers that are located at even positions in a given list. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `solution` function. This function takes a single argument, a non-empty list of integers, and returns the sum of all odd integers that are found at even indices (0-based) in the list.

### Function Signature

```python
def solution(lst):
    """
    Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples:
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
```

### Examples

- `solution([5, 8, 7, 1])` returns `12` because the odd numbers at even positions are 5 and 7.
- `solution([3, 3, 3, 3, 3])` returns `9` because the odd numbers at even positions are 3, 3, and 3.
- `solution([30, 13, 24, 321])` returns `0` because there are no odd numbers at even positions.

## Installation

This software does not require any external libraries or dependencies, making it very easy to set up. Simply ensure you have Python installed on your system.

### Requirements

- Python 3.x

## Usage

To use the `solution` function, follow these steps:

1. Ensure Python is installed on your system.
2. Copy the `solution` function code into your Python script or interactive environment.
3. Call the `solution` function with a list of integers as the argument.

### Example Usage

```python
# Example usage of the solution function
result = solution([5, 8, 7, 1])
print(result)  # Output: 12
```

This will output `12`, as explained in the examples section.

## Conclusion

This software provides a simple yet effective way to calculate the sum of odd integers at even positions in a list. With no external dependencies, it is easy to integrate into any Python project.
```