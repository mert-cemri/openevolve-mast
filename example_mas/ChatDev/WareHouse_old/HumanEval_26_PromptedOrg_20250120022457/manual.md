manual.md

```
# Remove Duplicates from List

This software provides a simple utility function to remove duplicates from a list of integers, retaining only those elements that occur exactly once and maintaining their original order.

## Main Functionality

The core functionality of this software is encapsulated in the `remove_duplicates` function. This function takes a list of integers as input and returns a new list with all elements that occur more than once removed. The order of the elements in the returned list is the same as their order in the input list.

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
    # Count each number in the list
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    # Collect numbers that occur exactly once
    result = [number for number in numbers if count[number] == 1]
    return result
```

## Installation

There are no external dependencies required for this software, so you can use it directly in your Python environment.

### Quick Start

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Copy the code from the `main.py` file into your Python environment or script.

3. Use the `remove_duplicates` function as demonstrated in the example above.

## Usage

To use the `remove_duplicates` function, simply pass a list of integers to it. The function will return a new list with duplicates removed.

### Example Usage

```python
numbers = [1, 2, 3, 2, 4]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 3, 4]
```

This software is designed to be simple and efficient, making it easy to integrate into larger projects or use as a standalone utility for processing lists of integers.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you with any problems or inquiries you may have regarding the software.
```