# Right Angle Triangle Checker

This software provides a simple function to determine if three given side lengths can form a right-angled triangle. It uses the Pythagorean theorem to verify if the triangle is right-angled.

## Main Function

The main function of this software is:

### `right_angle_triangle(a, b, c)`

- **Description**: This function takes three arguments, which are the lengths of the sides of a triangle. It returns `True` if the sides form a right-angled triangle and `False` otherwise.
- **Parameters**:
  - `a` (int or float): Length of the first side.
  - `b` (int or float): Length of the second side.
  - `c` (int or float): Length of the third side.
- **Returns**: `bool` - `True` if the sides form a right-angled triangle, `False` otherwise.
- **Example**:
  ```python
  right_angle_triangle(3, 4, 5)  # Returns: True
  right_angle_triangle(1, 2, 3)  # Returns: False
  ```

## Installation

This software does not require any external dependencies. It is implemented in pure Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can use the function in your Python scripts or interactive sessions. Here is an example of how to use it:
   ```python
   from main import right_angle_triangle

   # Example usage
   print(right_angle_triangle(3, 4, 5))  # Output: True
   print(right_angle_triangle(1, 2, 3))  # Output: False
   ```

## Documentation

For further details on how the function works, you can refer to the docstring provided in the `main.py` file. The function is straightforward and uses basic Python operations to determine if the triangle is right-angled.

## Support

If you encounter any issues or have questions, please feel free to reach out through the project's issue tracker on the repository page. We welcome feedback and contributions to improve the software.