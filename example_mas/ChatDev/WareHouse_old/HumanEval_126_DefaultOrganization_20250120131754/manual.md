manual.md

```
# is_sorted Function

This software provides a simple utility function to determine if a list of integers is sorted in ascending order and checks for duplicate occurrences of numbers. It is designed to be used in Python environments and does not require any external dependencies.

## Main Functionality

The primary function provided by this software is `is_sorted(lst)`. It performs the following tasks:

- **Check Ascending Order**: Determines if the list of integers is sorted in ascending order.
- **Check Duplicates**: Ensures that no number appears more than twice in the list. If a number appears more than twice, the function returns `False`.

### Function Signature

```python
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
```

### Examples

- `is_sorted([5])` ➞ `True`
- `is_sorted([1, 2, 3, 4, 5])` ➞ `True`
- `is_sorted([1, 3, 2, 4, 5])` ➞ `False`
- `is_sorted([1, 2, 2, 3, 3, 4])` ➞ `True`
- `is_sorted([1, 2, 2, 2, 3, 4])` ➞ `False`

## Installation

This software does not require any external dependencies, making it easy to integrate into any Python project. Simply ensure that you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.
3. **Run the Function**: You can directly use the function in your Python scripts or interactive sessions.

## Usage

To use the `is_sorted` function, follow these steps:

1. **Import the Function**: Ensure that the `main.py` file is in your working directory or in your Python path.
2. **Call the Function**: Use the function by passing a list of integers as an argument.

### Example Usage

```python
from main import is_sorted

# Example list
numbers = [1, 2, 3, 4, 5]

# Check if the list is sorted and has no more than one duplicate of any number
result = is_sorted(numbers)

print(result)  # Output: True
```

## Documentation

For further details and examples, refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into larger projects.

Feel free to modify and extend the functionality as needed for your specific use case.
```