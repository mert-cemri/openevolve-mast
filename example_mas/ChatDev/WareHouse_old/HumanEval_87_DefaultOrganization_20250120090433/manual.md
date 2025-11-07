# User Manual for `get_row` Function

## Introduction

The `get_row` function is a Python utility designed to process a 2D list (nested lists) and identify the coordinates of a specified integer within this list. It returns these coordinates sorted by specific criteria, making it a useful tool for data analysis and manipulation tasks where matrix-like structures are involved.

## Main Functionality

The primary function of this software is:

- **`get_row(lst, x)`**: This function takes a 2D list `lst` and an integer `x` as inputs. It searches for occurrences of `x` within the list and returns a list of tuples. Each tuple represents the coordinates (row, column) of `x` in the list. The coordinates are sorted first by row index in ascending order and then by column index in descending order.

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

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `get_row` function.

3. **Run the script**: Use a Python interpreter to execute the script and test the function.

```bash
python main.py
```

## How to Use

1. **Prepare your data**: Ensure your data is structured as a 2D list (nested lists).

2. **Call the `get_row` function**: Pass your 2D list and the integer you want to find as arguments to the function.

3. **Process the output**: The function will return a list of tuples indicating the positions of the integer in the list, sorted as specified.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is documented with a detailed docstring explaining its purpose, parameters, and expected output.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you make the most out of our software.