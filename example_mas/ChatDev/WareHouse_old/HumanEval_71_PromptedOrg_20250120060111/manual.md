# Triangle Area Calculator

This software module provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and then calculates the area using Heron's formula.

## Main Function

### `triangle_area(a, b, c)`

- **Description**: 
  - This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle.
  - It returns the area of the triangle rounded to 2 decimal points if the three sides form a valid triangle.
  - If the sides do not form a valid triangle, the function returns `-1`.

- **Parameters**:
  - `a` (float): Length of the first side of the triangle.
  - `b` (float): Length of the second side of the triangle.
  - `c` (float): Length of the third side of the triangle.

- **Returns**:
  - `float`: The area of the triangle rounded to 2 decimal places if valid.
  - `int`: `-1` if the sides do not form a valid triangle.

- **Example Usage**:
  ```python
  area = triangle_area(3, 4, 5)
  print(area)  # Output: 6.00

  area = triangle_area(1, 2, 10)
  print(area)  # Output: -1
  ```

## Installation

This project does not require any external dependencies. It is implemented using standard Python libraries.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository**: 
   - Clone the repository to your local machine using `git` or download the ZIP file.

2. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the directory where the project files are located.

3. **Run the Code**:
   - You can run the code by executing the `main.py` file in a Python environment.
   - Example:
     ```bash
     python main.py
     ```

4. **Use the Function**:
   - Import the `triangle_area` function into your Python script or interactive session.
   - Call the function with the desired side lengths to calculate the area.

## Documentation

For further details on how the function works, refer to the docstring within the `main.py` file. The docstring provides a comprehensive explanation of the function's purpose, parameters, and return values.

This module is designed to be simple and efficient, providing a quick way to calculate the area of a triangle given its side lengths.