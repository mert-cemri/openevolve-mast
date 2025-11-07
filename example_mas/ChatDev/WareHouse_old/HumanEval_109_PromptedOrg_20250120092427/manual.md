# Move One Ball

This software provides a function `move_one_ball` that determines if an array can be sorted in non-decreasing order by performing any number of right shift operations.

## Main Functionality

The main function of this software is:

- **move_one_ball(arr):** This function takes an array `arr` of N unique integers and determines if it is possible to sort the array in non-decreasing order by performing any number of right shift operations. If it is possible, the function returns `True`; otherwise, it returns `False`. If the array is empty, it returns `True`.

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

This software does not require any external dependencies. You can directly use the provided Python code in your environment.

### Quick Install

Since there are no external dependencies, you can simply copy the function `move_one_ball` into your Python script or project.

## How to Use

1. **Copy the Function:**
   - Copy the `move_one_ball` function from the `main.py` file into your Python script.

2. **Call the Function:**
   - Call the `move_one_ball` function with an array of unique integers as an argument to determine if it can be sorted by right shifts.

3. **Interpret the Result:**
   - The function will return `True` if the array can be sorted in non-decreasing order by right shifts, and `False` otherwise.

## Documentation

The function is documented within the code itself, providing a clear explanation of its purpose, parameters, and return values. For further details, refer to the comments in the `main.py` file.

Feel free to reach out if you have any questions or need further assistance with using this software.