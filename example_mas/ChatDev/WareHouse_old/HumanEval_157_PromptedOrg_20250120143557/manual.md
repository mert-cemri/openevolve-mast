# Right Angle Triangle Checker

This software provides a simple function to determine if three given sides can form a right-angled triangle using the Pythagorean theorem.

## Main Functionality

The main function provided by this software is `right_angle_triangle(a, b, c)`. This function takes three arguments, which represent the lengths of the sides of a triangle. It returns `True` if the sides form a right-angled triangle and `False` otherwise.

### How It Works

The function works by sorting the sides to identify the hypotenuse (the longest side) and then checks if the Pythagorean theorem holds true for these sides. The Pythagorean theorem states that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.

## Installation

This project does not require any external dependencies, so there is no need to install additional packages. You only need to have Python installed on your system.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

To use the `right_angle_triangle` function, follow these steps:

1. Open your Python environment (e.g., IDLE, PyCharm, VSCode, or terminal).

2. Copy the function code into your Python script or interactive shell:

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
        # Sort the sides to identify the hypotenuse
        sides = sorted([a, b, c])
        # Check the Pythagorean theorem
        return sides[0]**2 + sides[1]**2 == sides[2]**2
    ```

3. Call the function with the side lengths you want to check. For example:

    ```python
    print(right_angle_triangle(3, 4, 5))  # Output: True
    print(right_angle_triangle(1, 2, 3))  # Output: False
    ```

## Conclusion

This software provides a straightforward method to check if three sides can form a right-angled triangle. It is easy to use and requires no additional setup beyond having Python installed.