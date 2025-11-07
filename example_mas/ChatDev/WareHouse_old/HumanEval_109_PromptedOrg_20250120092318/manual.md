# Move One Ball

This software provides a function `move_one_ball` that determines if an array can be sorted in non-decreasing order by performing right shift operations. The function is implemented in Python and is designed to handle arrays with unique elements.

## Main Function

### `move_one_ball(arr)`

- **Description**: This function checks if it is possible to sort an array in non-decreasing order by performing any number of right shift operations. A right shift operation moves all elements of the array one position to the right, with the last element moving to the first position.

- **Parameters**: 
  - `arr`: A list of unique integers.

- **Returns**: 
  - `True` if the array can be sorted in non-decreasing order by performing right shift operations.
  - `False` otherwise.
  - If the array is empty, it returns `True`.

- **Example Usage**:
  ```python
  move_one_ball([3, 4, 5, 1, 2])  # Returns: True
  move_one_ball([3, 5, 4, 1, 2])  # Returns: False
  ```

## Installation

To use the `move_one_ball` function, you need to have Python installed on your system. The function does not require any additional dependencies beyond Python's standard library.

### Quick Install

1. **Python Installation**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to the location where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

## How to Use

1. **Open a Python Environment**: You can use any Python environment such as IDLE, PyCharm, or VSCode.

2. **Import the Function**: Import the `move_one_ball` function from the `main.py` file.

   ```python
   from main import move_one_ball
   ```

3. **Call the Function**: Pass an array of unique integers to the function and get the result.

   ```python
   result = move_one_ball([3, 4, 5, 1, 2])
   print(result)  # Output: True
   ```

## Documentation

For further details and examples, refer to the comments within the `main.py` file. The function is well-documented with examples to help you understand its usage and functionality.

Feel free to reach out for support or additional information if needed.