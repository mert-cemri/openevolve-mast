manual.md

```
# Move One Ball

A Python application to determine if an array can be sorted in non-decreasing order by performing a series of right shift operations.

## Overview

The `move_one_ball` function is designed to check if it is possible to sort an array of unique integers in non-decreasing order by performing any number of right shift operations. A right shift operation moves all elements of the array one position to the right, with the last element wrapping around to the first position.

### Key Features

- **Unique Elements**: The function assumes all elements in the array are unique.
- **Right Shift Operation**: The function checks if the array can be sorted by performing right shifts.
- **Empty Array Handling**: If the array is empty, the function returns `True`.

## Installation

This application does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **No Additional Dependencies**: 
   Since there are no external dependencies, you can directly run the Python script.

## Usage

To use the `move_one_ball` function, follow these steps:

1. **Open a Python Environment**: You can use a terminal, command prompt, or any Python IDE.

2. **Import the Function**:
   ```python
   from main import move_one_ball
   ```

3. **Call the Function**: 
   Pass an array of integers to the function to check if it can be sorted by right shifts.
   ```python
   result = move_one_ball([3, 4, 5, 1, 2])
   print(result)  # Output: True

   result = move_one_ball([3, 5, 4, 1, 2])
   print(result)  # Output: False
   ```

### Function Explanation

- **Input**: A list of unique integers.
- **Output**: A boolean value (`True` or `False`).
  - Returns `True` if the array can be sorted in non-decreasing order by right shifts.
  - Returns `False` otherwise.

### Example

```python
# Example 1
arr1 = [3, 4, 5, 1, 2]
print(move_one_ball(arr1))  # Output: True

# Example 2
arr2 = [3, 5, 4, 1, 2]
print(move_one_ball(arr2))  # Output: False

# Example 3 (Empty Array)
arr3 = []
print(move_one_ball(arr3))  # Output: True
```

## Conclusion

The `move_one_ball` function provides a simple yet effective way to determine if an array can be sorted using right shift operations. With no external dependencies, it is easy to integrate into any Python project.
```