# Move One Ball

This software provides a function to determine if an array of unique integers can be sorted in non-decreasing order by performing any number of right shift operations.

## Main Functionality

The main function provided by this software is `move_one_ball(arr)`. This function takes an array of unique integers as input and returns a boolean value indicating whether the array can be sorted in non-decreasing order by performing right shift operations.

### Function Definition

```python
def move_one_ball(arr):
    """Determine if the array can be sorted in non-decreasing order by right shifts.
    Args:
        arr (list): A list of unique integers.
    Returns:
        bool: True if the array can be sorted by right shifts, False otherwise.
    """
```

### How It Works

- **Input**: A list of unique integers.
- **Output**: A boolean value:
  - `True`: If the array can be sorted in non-decreasing order by performing right shift operations.
  - `False`: If it is not possible to sort the array in non-decreasing order by right shifts.

### Example Usage

```python
# Example 1
result = move_one_ball([3, 4, 5, 1, 2])
print(result)  # Output: True

# Example 2
result = move_one_ball([3, 5, 4, 1, 2])
print(result)  # Output: False
```

## Installation

This project does not require any external dependencies. You can simply download the `main.py` file and run it using Python.

### Steps to Install

1. **Download the Code**: Download the `main.py` file to your local machine.
2. **Run the Code**: Use Python to run the file. Ensure you have Python installed on your machine.

```bash
python main.py
```

## How to Use

1. **Prepare Your Array**: Have your array of unique integers ready.
2. **Call the Function**: Use the `move_one_ball` function with your array as the argument.
3. **Get the Result**: The function will return `True` or `False` based on whether the array can be sorted by right shifts.

## Conclusion

This software provides a simple yet effective way to determine if an array can be sorted in non-decreasing order using right shift operations. With no external dependencies, it is easy to set up and use. Simply download the code, run it, and use the `move_one_ball` function to get your results.