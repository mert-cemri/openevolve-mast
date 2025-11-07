# User Manual for `get_row` Function

## Introduction

The `get_row` function is a Python utility designed to search for a specified integer within a 2D list (nested lists) and return the coordinates of its occurrences. The coordinates are returned as a list of tuples, sorted by specific criteria: primarily by row index in ascending order, and secondarily by column index in descending order.

## Main Functionality

- **Function Name**: `get_row`
- **Purpose**: To find all occurrences of a specified integer in a 2D list and return their coordinates.
- **Input**:
  - `lst`: A 2D list (list of lists) where each sublist represents a row.
  - `x`: An integer to search for within the 2D list.
- **Output**: A list of tuples, where each tuple represents the coordinates (row index, column index) of an occurrence of `x`.

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

This function is implemented in pure Python and does not require any external libraries or dependencies. Therefore, there is no need for a `requirements.txt` file or any package installations.

## How to Use

1. **Copy the Code**: Copy the `get_row` function code into your Python script or interactive environment.

2. **Call the Function**: Use the function by passing a 2D list and the integer you want to search for as arguments.

3. **Process the Output**: The function will return a list of tuples representing the coordinates of the integer in the 2D list, sorted by the specified criteria.

## Additional Information

- **Sorting Criteria**: The function sorts the coordinates first by row index in ascending order and then by column index in descending order. This ensures that results are organized in a way that prioritizes row order while listing column indices from right to left within each row.

- **Edge Cases**: The function handles edge cases such as empty lists or rows gracefully, returning an empty list if no occurrences are found.

This utility is simple yet effective for applications that require locating and organizing occurrences of a specific value within irregularly shaped 2D data structures.