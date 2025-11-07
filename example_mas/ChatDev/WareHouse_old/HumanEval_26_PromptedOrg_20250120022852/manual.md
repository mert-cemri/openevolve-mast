# Remove Duplicates from List

This software module provides a function to remove duplicates from a list of integers, keeping only those elements that appear exactly once. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function provided by this module is `remove_duplicates`, which takes a list of integers as input and returns a new list containing only the integers that appear exactly once in the original list. The order of elements in the returned list is the same as their order in the input list.

### Function Signature

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
```

### Example Usage

```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```

## Installation

Since this module does not require any external dependencies, you can use it directly in your Python environment without any additional installation steps. Ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Module:**
   - Obtain the `main.py` file containing the `remove_duplicates` function.

2. **Run the Function:**
   - Import the function into your Python script or interactive session.
   - Call the `remove_duplicates` function with a list of integers as an argument.

### Example

```python
from main import remove_duplicates

numbers = [1, 2, 3, 2, 4]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 3, 4]
```

## Documentation

The function is documented with a docstring that includes a brief description and an example. You can view this documentation by using Python's built-in help system:

```python
help(remove_duplicates)
```

This will display the function's docstring, providing details on its usage and an example.

## Conclusion

This module offers a simple and efficient way to filter out duplicate integers from a list, retaining only those that appear once. It is easy to integrate into existing Python projects and requires no additional setup.