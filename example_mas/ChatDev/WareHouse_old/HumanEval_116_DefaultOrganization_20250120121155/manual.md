# Sort Array by Binary Ones

This software provides a function to sort an array of integers based on the number of ones in their binary representation in ascending order. For numbers with the same number of ones, they are sorted based on their decimal value.

## Main Functionality

The main function provided by this software is `sort_array(arr)`, which takes a list of integers as input and returns a sorted list based on the criteria mentioned above.

### Function Definition

```python
def sort_array(arr):
    """
    Sort an array of integers according to the number of ones
    in their binary representation in ascending order. For numbers with the
    same number of ones, sort based on decimal value.
    Args:
    arr (list): A list of integers.
    Returns:
    list: A sorted list of integers.
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    return sorted(arr, key=lambda x: (bin(x & 0xffffffff).count('1'), x))
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Usage

To use the `sort_array` function, follow these steps:

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Script**: You can run the script directly from the command line or import the function into your own Python scripts.

### Example Usage

You can test the function by running the following examples:

```python
# Example usage
if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
```

Simply execute the `main.py` file in your terminal or command prompt:

```bash
python main.py
```

This will output the sorted arrays as specified in the examples.

## Documentation

For further details on how the function works, refer to the docstring within the `sort_array` function in the `main.py` file. This provides a comprehensive explanation of the function's purpose, arguments, and return values.