manual.md

```
# Right Angle Triangle Checker

This software provides a simple function to determine if three given side lengths can form a right-angled triangle. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is `right_angle_triangle(a, b, c)`. This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle. It returns `True` if the sides form a right-angled triangle and `False` otherwise.

### Function Definition

```python
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Sort the sides to ensure the longest side is last
    sides = sorted([a, b, c])
    # Check if the square of the longest side is equal to the sum of the squares of the other two sides
    return sides[2]**2 == sides[0]**2 + sides[1]**2
```

## Installation

This software does not require any external libraries or dependencies. You only need to have Python installed on your system. 

### Installing Python

1. **Download Python**: Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the installation instructions provided on the website. Make sure to check the option to add Python to your system's PATH during installation.

3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## Usage

To use the `right_angle_triangle` function, follow these steps:

1. **Create a Python File**: Create a new Python file, e.g., `main.py`, and copy the function definition into this file.

2. **Call the Function**: In the same file, you can call the `right_angle_triangle` function with the desired side lengths. For example:

    ```python
    print(right_angle_triangle(3, 4, 5))  # Output: True
    print(right_angle_triangle(1, 2, 3))  # Output: False
    ```

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing your Python file, and run the script using the command `python main.py`.

## Conclusion

This software provides a straightforward way to check if three side lengths can form a right-angled triangle. It is easy to use and requires no additional setup beyond having Python installed on your system.
```