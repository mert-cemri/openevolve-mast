# User Manual for `get_row` Function

## Introduction

The `get_row` function is a Python utility designed to work with 2-dimensional data represented as nested lists. Unlike traditional matrices, each row in this data structure may contain a different number of columns. The primary function of `get_row` is to locate all occurrences of a specified integer within this data structure and return their coordinates in a specific order.

## Main Functionality

### `get_row(lst, x)`

- **Purpose**: To find all occurrences of an integer `x` in a 2-dimensional list `lst` and return their coordinates.
- **Input**:
  - `lst`: A list of lists (2D data structure) where each sublist represents a row.
  - `x`: An integer value to search for within the 2D list.
- **Output**: A list of tuples, where each tuple represents the coordinates `(row_index, column_index)` of an occurrence of `x`. The coordinates are sorted by row index in ascending order and by column index in descending order within each row.

### Example Usage

```python
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

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python 3.x installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file using Python:
   ```bash
   python main.py
   ```

## Usage

To use the `get_row` function, simply import it into your Python script and call it with the appropriate parameters. The function will return a list of coordinates where the specified integer is found in the 2D list.

## Documentation

For further details and advanced usage examples, please refer to the inline comments and docstrings within the `main.py` file. These provide comprehensive guidance on how to utilize the function effectively.

## Support

For any issues or questions, please contact our support team or refer to the project's issue tracker if available. We are committed to providing assistance to ensure you have a smooth experience using our software.