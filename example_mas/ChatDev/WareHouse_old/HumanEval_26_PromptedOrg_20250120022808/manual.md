# Remove Duplicates

This software provides a simple function to remove duplicate integers from a list, keeping only the elements that appear once and maintaining their order.

## Main Functionality

The main function of this software is:

- `remove_duplicates(numbers: List[int]) -> List[int]`: This function takes a list of integers as input and returns a new list with all elements that occur more than once removed, while maintaining the order of the remaining elements.

### Example

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Dictionary to count occurrences of each number
    count = {}
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    # List to store numbers that occur only once
    result = []
    for number in numbers:
        if count[number] == 1:
            result.append(number)
    return result
```

## Installation

There are no external dependencies required for this software. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Get the code onto your local machine.

3. **Run the code**: You can run the function directly in a Python environment or script.

## How to Use

1. **Import the function**: Ensure that the function `remove_duplicates` is accessible in your Python environment.

2. **Call the function**: Pass a list of integers to the function and receive a list with duplicates removed.

### Example Usage

```python
# Example usage of the remove_duplicates function
numbers = [1, 2, 3, 2, 4]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 3, 4]
```

## Documentation

For further details on how the function works, refer to the docstring within the code. The docstring provides an example and a brief description of the function's purpose and behavior.