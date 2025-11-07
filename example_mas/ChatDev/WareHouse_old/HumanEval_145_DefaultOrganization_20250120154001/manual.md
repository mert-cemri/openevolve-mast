manual.md

```
# Order by Points

A Python application that sorts a list of integers based on the sum of their digits. If multiple integers have the same digit sum, they are ordered based on their original index in the list.

## Main Functionality

The main function of this software is `order_by_points`, which takes a list of integers and returns a new list sorted according to the sum of their digits. This function is useful for applications where sorting based on digit characteristics is required.

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

### Prerequisites

- Python 3.x

### Quick Install

1. Clone the repository or download the `main.py` file.
2. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
3. No additional dependencies are required for this application.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the script using Python:

```bash
python main.py
```

This will execute the example usage provided in the script, demonstrating the functionality of the `order_by_points` function.

## Documentation

For further details on the implementation, refer to the comments within the `main.py` file. The code is self-explanatory and includes examples to guide you through its usage.

```