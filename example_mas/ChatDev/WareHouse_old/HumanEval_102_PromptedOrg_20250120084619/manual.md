# Choose_Num Function

This software module provides a simple utility function to find the largest even integer within a specified range of two positive numbers. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Function

### `choose_num(x, y)`

- **Description**: This function takes two positive numbers, `x` and `y`, and returns the largest even integer within the inclusive range `[x, y]`. If no even number exists within this range, the function returns `-1`.

- **Parameters**:
  - `x` (int): The lower bound of the range.
  - `y` (int): The upper bound of the range.

- **Returns**:
  - The largest even integer within the range `[x, y]`, or `-1` if no such number exists.

- **Examples**:
  - `choose_num(12, 15)` returns `14`.
  - `choose_num(13, 12)` returns `-1`.

## Installation

This software does not require any external dependencies, making it simple to install and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

## Usage

To use the `choose_num` function, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory containing the `main.py` file.

3. Run the Python interpreter and import the function:

   ```bash
   python
   ```

   ```python
   from main import choose_num
   ```

4. Call the `choose_num` function with your desired parameters:

   ```python
   result = choose_num(12, 15)
   print(result)  # Output: 14
   ```

5. You can modify the parameters to test different ranges as needed.

## Documentation

For further information or assistance, please refer to the comments within the `main.py` file. The code is documented to provide clarity on the function's purpose and usage.

This manual provides all the necessary information to understand, install, and use the `choose_num` function effectively. If you have any questions or need further assistance, please feel free to reach out to our support team.