manual.md

```
# Right Angle Triangle Checker

This software provides a simple function to determine if three given side lengths can form a right-angled triangle. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is `right_angle_triangle(a, b, c)`. This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle. It returns `True` if the sides form a right-angled triangle and `False` otherwise.

### Function Definition

```python
def right_angle_triangle(a, b, c):
    # Sort the sides to identify the hypotenuse
    sides = sorted([a, b, c])
    # Check if the square of the hypotenuse is equal to the sum of the squares of the other two sides
    return sides[2]**2 == sides[0]**2 + sides[1]**2
```

### Example Usage

```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

## Installation

Since this software does not require any external libraries, there is no need to install additional dependencies. You only need to have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Download the Code**: Copy the code provided above into a file named `main.py`.

2. **Run the Code**: Open a terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:

   ```bash
   python main.py
   ```

3. **Test the Function**: You can test the function by calling it with different sets of side lengths to see if they form a right-angled triangle.

## Conclusion

This software provides a straightforward way to check if three side lengths can form a right-angled triangle using Python. It leverages the Pythagorean theorem to perform this check efficiently and accurately.
```