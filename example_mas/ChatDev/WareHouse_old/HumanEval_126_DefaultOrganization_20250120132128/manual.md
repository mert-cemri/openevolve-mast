manual.md

```
# is_sorted Function

This software provides a simple utility function to determine if a list of integers is sorted in ascending order and ensures that no number appears more than once consecutively. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The main function provided by this software is `is_sorted(lst)`. This function checks if a given list of integers is sorted in ascending order and ensures that no number appears more than once consecutively. If the list meets these criteria, the function returns `True`; otherwise, it returns `False`.

### Function Details

- **Input**: A list of integers `lst`.
- **Output**: A boolean value:
  - `True` if the list is sorted in ascending order and no number appears more than once consecutively.
  - `False` otherwise.

### Examples

- `is_sorted([5])` ➞ `True`
- `is_sorted([1, 2, 3, 4, 5])` ➞ `True`
- `is_sorted([1, 3, 2, 4, 5])` ➞ `False`
- `is_sorted([1, 2, 2, 3, 3, 4])` ➞ `True`
- `is_sorted([1, 2, 2, 2, 3, 4])` ➞ `False`

## Installation

This software does not require any external dependencies, making it easy to integrate into your existing Python projects.

### Quick Install

Since there are no external dependencies, you can simply copy the `is_sorted` function into your Python script or project.

## Usage

1. **Copy the Function**: Copy the `is_sorted` function from the `main.py` file into your Python script.

2. **Call the Function**: Use the function by passing a list of integers as an argument.

```python
# Example usage
from your_module import is_sorted

result = is_sorted([1, 2, 3, 4, 5])
print(result)  # Output: True
```

3. **Integrate into Projects**: You can integrate this function into larger projects where you need to check if lists are sorted and meet the specified criteria.

## Documentation

For further details on how to use the function or to see more examples, please refer to the comments within the `main.py` file. The function is self-contained and includes inline documentation for ease of understanding.

```