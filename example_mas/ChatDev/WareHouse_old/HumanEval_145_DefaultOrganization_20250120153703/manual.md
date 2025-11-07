manual.md

```
# Order By Points

A Python utility to sort a list of integers based on the sum of their digits. If two numbers have the same digit sum, they are ordered based on their original position in the list.

## Overview

The `order_by_points` function is designed to take a list of integers and return a new list sorted by the sum of the digits of each integer. This can be particularly useful in scenarios where digit-based sorting is required, such as in certain mathematical or data processing applications.

## Main Function

### order_by_points(nums)

- **Description**: Sorts a list of integers in ascending order based on the sum of their digits. If two numbers have the same digit sum, they maintain their relative order from the original list.
- **Parameters**: 
  - `nums` (list of int): The list of integers to sort.
- **Returns**: 
  - `list of int`: The sorted list of integers.

- **Examples**:
  ```python
  >>> order_by_points([1, 11, -1, -11, -12])
  [-1, -11, 1, -12, 11]

  >>> order_by_points([])
  []
  ```

## Installation

This utility does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the script**:
   - You can directly run the `main.py` file to see the function in action:
     ```bash
     python main.py
     ```

## Usage

To use the `order_by_points` function in your own projects, you can import it from the module where it is defined. Here is an example of how to use it:

```python
from main import order_by_points

# Example usage
sorted_list = order_by_points([1, 11, -1, -11, -12])
print(sorted_list)  # Output: [-1, -11, 1, -12, 11]
```

## Documentation

For further details on the implementation and examples, please refer to the comments within the `main.py` file. The function is well-documented to provide insights into its working and usage.

## Support

For any issues or questions, please contact the development team at ChatDev. We are here to assist you with any queries regarding the usage of this utility.
```
