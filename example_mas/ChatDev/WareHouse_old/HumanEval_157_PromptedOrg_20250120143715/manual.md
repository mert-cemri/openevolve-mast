manual.md

```
# Right Angle Triangle Checker

This software provides a simple function to determine if three given side lengths can form a right-angled triangle. It uses the Pythagorean theorem to verify if the triangle is right-angled.

## Main Function

The main function provided by this software is `right_angle_triangle(a, b, c)`. This function takes three arguments, which are the lengths of the sides of a triangle, and returns `True` if these sides form a right-angled triangle, and `False` otherwise.

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
    # Sort the sides to ensure the largest is considered as the hypotenuse
    sides = sorted([a, b, c])
    # Check the Pythagorean theorem
    return sides[0]**2 + sides[1]**2 == sides[2]**2
```

## Installation

This software does not require any external dependencies, making it simple and easy to use. You can directly use the function in your Python environment.

### Quick Start

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function directly in a Python script or an interactive Python session.

## Usage

To use the `right_angle_triangle` function, simply call it with three numerical arguments representing the lengths of the sides of a triangle. For example:

```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

## How It Works

The function works by first sorting the three side lengths to ensure the largest is considered as the hypotenuse. It then checks if the sum of the squares of the two smaller sides equals the square of the largest side, as per the Pythagorean theorem. If this condition is met, the function returns `True`, indicating that the sides form a right-angled triangle.

## Documentation

For further information and examples, please refer to the comments within the code. The function is straightforward and designed to be easily integrated into larger projects or used standalone for quick checks.

```