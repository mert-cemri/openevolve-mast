# Order By Points

This software module provides a function to sort a list of integers based on the sum of their digits. It is designed to handle lists of integers and sort them in a specific order as described below.

## Main Functionality

The primary function of this module is `order_by_points`, which sorts a list of integers in ascending order according to the sum of their digits. If multiple integers have the same digit sum, they are ordered based on their original index in the list.

### Function: `order_by_points(nums)`

- **Input**: A list of integers (`nums`).
- **Output**: A list of integers sorted based on the sum of their digits.

#### Example Usage

```python
>>> order_by_points([1, 11, -1, -11, -12])
[-1, -11, 1, -12, 11]

>>> order_by_points([])
[]
```

## Installation

This module does not have any external dependencies, so you can use it directly without installing any additional packages. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `order_by_points` function.

2. **Run the Function**: You can use the function by importing it into your Python script or interactive session.

   ```python
   from main import order_by_points

   # Example usage
   sorted_list = order_by_points([1, 11, -1, -11, -12])
   print(sorted_list)  # Output: [-1, -11, 1, -12, 11]
   ```

3. **Modify and Extend**: Feel free to modify the function for your specific needs or integrate it into larger projects.

## Documentation

For further details on how the function works, you can refer to the docstring provided within the `main.py` file. This includes a description of the function, its arguments, and the expected output.

## Support

If you encounter any issues or have questions about using this module, please reach out to our support team for assistance. We are here to help you make the most of this software.