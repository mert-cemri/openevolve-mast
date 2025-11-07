# Sum Squares Function

This software provides a simple Python function to calculate the sum of squared numbers from a given list. Each element in the list is first rounded up to the nearest integer (using the ceiling function) before squaring.

## Main Function

### `sum_squares(lst)`

- **Description**: This function takes a list of numbers as input, rounds each number up to the nearest integer, squares each rounded number, and returns the sum of these squared values.

- **Parameters**: 
  - `lst`: A list of numbers (integers or floats).

- **Returns**: 
  - An integer representing the sum of the squares of the rounded numbers.

- **Examples**:
  - `sum_squares([1, 2, 3])` returns `14`
  - `sum_squares([1, 4, 9])` returns `98`
  - `sum_squares([1, 3, 5, 7])` returns `84`
  - `sum_squares([1.4, 4.2, 0])` returns `29`
  - `sum_squares([-2.4, 1, 1])` returns `6`

## Installation

This software does not require any external dependencies beyond the Python standard library. The `math` module, which is part of the standard library, is used for the ceiling function.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function by importing it into your Python script or directly running it in a Python interactive shell.

   Example usage in a Python script:
   ```python
   from main import sum_squares

   result = sum_squares([1.4, 4.2, 0])
   print(result)  # Output: 29
   ```

4. **Testing**: You can test the function with different lists to ensure it works as expected.

## Documentation

For further information and examples, refer to the comments within the `main.py` file, which provide detailed explanations and usage examples.