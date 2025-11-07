manual.md

```
# Right Angle Triangle Checker

This software provides a simple function to determine if three given side lengths can form a right-angled triangle. It uses the Pythagorean theorem to check if the triangle is right-angled.

## Main Functionality

The core functionality of this software is encapsulated in the `right_angle_triangle` function, which takes three arguments representing the lengths of the sides of a triangle and returns a boolean value indicating whether the triangle is right-angled.

### Function Definition

```python
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle, return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or 
    90 degrees.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
```

### How It Works

- The function first sorts the side lengths to identify the hypotenuse (the longest side).
- It then applies the Pythagorean theorem: \(a^2 + b^2 = c^2\), where \(c\) is the hypotenuse.
- If the equation holds true, the function returns `True`, indicating that the sides form a right-angled triangle. Otherwise, it returns `False`.

## Installation

This software is written in Python and does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system.

### Quick Install

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Download the Code**: Save the `main.py` file containing the function to your local machine.

## Usage

To use the `right_angle_triangle` function, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the Python interpreter by typing `python` (or `python3` depending on your installation).
4. Import the function by typing `from main import right_angle_triangle`.
5. Call the function with the desired side lengths. For example:
   ```python
   print(right_angle_triangle(3, 4, 5))  # Output: True
   print(right_angle_triangle(1, 2, 3))  # Output: False
   ```

## Documentation

For further information and examples, refer to the comments within the `main.py` file. The function is straightforward and designed for ease of use.

```