# Order By Points

This software module provides a function to sort a list of integers based on the sum of their digits. If two numbers have the same digit sum, they maintain their original order from the input list.

## Main Functionality

The main function provided by this module is `order_by_points`. It takes a list of integers and returns a new list sorted by the sum of the digits of each integer. If two integers have the same digit sum, they are ordered according to their original position in the input list.

### Function Signature

```python
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.
    Args:
    nums (list of int): The list of integers to be sorted.
    Returns:
    list of int: The sorted list of integers.
    """
```

### Example Usage

```python
# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # Output: []
```

## Installation

This module does not require any external dependencies, so you can directly use it in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the script using Python:

   ```bash
   python main.py
   ```

   This will execute the example usage provided in the script and display the sorted lists.

## Documentation

The function is straightforward and does not require additional configuration or setup. The logic for sorting is encapsulated within the function `order_by_points`, which uses a helper function `digit_sum` to calculate the sum of digits for each integer.

For any further questions or support, please refer to the comments within the code for guidance on how the function operates.