# Move One Ball

This software provides a function to determine if an array can be sorted in non-decreasing order by performing any number of right shift operations. The function is implemented in Python and does not require any external dependencies.

## Main Function

### `move_one_ball(arr)`

- **Description**: This function takes an array of integers and checks if it is possible to sort the array in non-decreasing order by performing right shift operations. A right shift operation involves moving all elements of the array one position to the right, with the last element moving to the first position.

- **Parameters**: 
  - `arr` (list of int): An array of integers with unique elements.

- **Returns**: 
  - `bool`: Returns `True` if the array can be sorted by right shifting, otherwise `False`. If the array is empty, it returns `True`.

- **Example Usage**:
  ```python
  result1 = move_one_ball([3, 4, 5, 1, 2])
  print(result1)  # Output: True

  result2 = move_one_ball([3, 5, 4, 1, 2])
  print(result2)  # Output: False
  ```

## Installation

This software does not require any external libraries or dependencies. It can be run with a standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can test the function by running a Python script or using an interactive Python shell. Here is an example of how to use the function in a script:

   ```python
   from main import move_one_ball

   # Test the function with different arrays
   print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
   print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
   ```

4. **Modify and Test**: Feel free to modify the `main.py` file and test the function with different inputs to see how it behaves.

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to understand, with comments explaining each step of the logic.

This software is a simple utility to solve a specific problem and is designed to be used as a standalone function in Python scripts.