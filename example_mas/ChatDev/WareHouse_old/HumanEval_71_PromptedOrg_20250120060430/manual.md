# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and calculates the area using Heron's formula if they do.

## Main Functionality

The main function provided by this software is `triangle_area(a, b, c)`, which performs the following tasks:

- **Input**: Takes three arguments `a`, `b`, and `c`, which represent the lengths of the sides of a triangle.
- **Output**: Returns the area of the triangle rounded to two decimal points if the sides form a valid triangle. If the sides do not form a valid triangle, it returns `-1`.

### Valid Triangle Check

A valid triangle is determined by the triangle inequality theorem, which states that for any three sides to form a triangle, the sum of the lengths of any two sides must be greater than the length of the remaining side. This function checks:

- \( a + b > c \)
- \( a + c > b \)
- \( b + c > a \)

### Area Calculation

If the sides form a valid triangle, the area is calculated using Heron's formula:

1. Calculate the semi-perimeter \( s \):
   \[
   s = \frac{a + b + c}{2}
   \]

2. Calculate the area \( A \):
   \[
   A = \sqrt{s \cdot (s - a) \cdot (s - b) \cdot (s - c)}
   \]

3. Return the area rounded to two decimal places.

## Installation

This software does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

### Quick Install

No installation of additional packages is necessary. You can directly use the function in your Python environment.

## Usage

To use the `triangle_area` function, follow these steps:

1. Open your Python environment or script editor.
2. Import the function from the `main.py` file.
3. Call the function with the desired side lengths.

### Example

```python
from main import triangle_area

# Example 1: Valid triangle
area1 = triangle_area(3, 4, 5)
print(area1)  # Output: 6.00

# Example 2: Invalid triangle
area2 = triangle_area(1, 2, 10)
print(area2)  # Output: -1
```

## Documentation

For further information on the implementation and usage of this function, please refer to the comments within the `main.py` file. The code is self-explanatory and provides insights into the logic used for validation and area calculation.