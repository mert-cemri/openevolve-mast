# Sum Squares Function

This software provides a simple function to compute the sum of squares of numbers in a list after rounding each number to the nearest upper integer (ceiling). It is implemented in Python and does not require any external dependencies.

## Main Function

### `sum_squares(lst)`

- **Description**: This function takes a list of numbers as input, rounds each number to the nearest upper integer, squares each rounded number, and returns the sum of these squares.

- **Parameters**: 
  - `lst`: A list of numbers (integers or floats).

- **Returns**: 
  - An integer representing the sum of the squares of the ceiling values of the numbers in the list.

- **Examples**:
  - `sum_squares([1, 2, 3])` returns `14`
  - `sum_squares([1, 4, 9])` returns `98`
  - `sum_squares([1, 3, 5, 7])` returns `84`
  - `sum_squares([1.4, 4.2, 0])` returns `29`
  - `sum_squares([-2.4, 1, 1])` returns `6`

## Installation

This software does not require any external libraries or dependencies. It only requires Python to be installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: You can clone the repository using Git or download the ZIP file and extract it.

3. **Navigate to the project directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

## Usage

To use the `sum_squares` function, follow these steps:

1. **Open a Python environment**: You can use a Python interpreter, a Jupyter notebook, or any Python IDE.

2. **Import the function**: If you are using the function in another script, you can import it using:
   ```python
   from main import sum_squares
   ```

3. **Call the function**: Pass a list of numbers to the `sum_squares` function and print or store the result.
   ```python
   result = sum_squares([1.4, 4.2, 0])
   print(result)  # Output: 29
   ```

This software is designed to be simple and efficient, providing a straightforward solution to compute the sum of squares of numbers after rounding them up.