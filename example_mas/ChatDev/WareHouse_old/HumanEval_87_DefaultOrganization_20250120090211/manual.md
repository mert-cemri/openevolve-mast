manual.md

```
# get_row Function

This software module provides a function `get_row` that allows users to find all occurrences of a specified integer within a 2D list (nested lists) and returns their coordinates. The coordinates are sorted by rows in ascending order and columns in descending order.

## Main Functionality

The primary function of this module is `get_row`, which performs the following tasks:

- Takes a 2D list (nested lists) and an integer as input.
- Searches for the integer within the 2D list.
- Returns a list of tuples representing the coordinates of the integer in the format (row, column).
- Coordinates are sorted by row index in ascending order and by column index in descending order within each row.

### Example Usage

```python
from main import get_row

# Example 1
result = get_row([
  [1, 2, 3, 4, 5, 6],
  [1, 2, 3, 4, 1, 6],
  [1, 2, 3, 4, 5, 1]
], 1)
print(result)  # Output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

# Example 2
result = get_row([], 1)
print(result)  # Output: []

# Example 3
result = get_row([[], [1], [1, 2, 3]], 3)
print(result)  # Output: [(2, 2)]
```

## Installation

This module does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Quick Install

1. Clone the repository or download the `main.py` file to your local machine.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. Import the `get_row` function from the `main.py` file.
2. Call the `get_row` function with your 2D list and the integer you want to find.
3. The function will return a list of tuples with the coordinates of the integer.

## Documentation

For further details on the implementation and usage, please refer to the comments within the `main.py` file. The function is designed to be intuitive and easy to integrate into existing Python projects.

```