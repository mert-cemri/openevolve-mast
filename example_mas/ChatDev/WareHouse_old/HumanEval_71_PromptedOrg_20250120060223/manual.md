# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and then computes the area using Heron's formula.

## Main Functionality

The main function of this software is:

- **triangle_area(a, b, c):** This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle. It returns the area of the triangle rounded to two decimal points if the sides form a valid triangle. If the sides do not form a valid triangle, it returns `-1`.

### Valid Triangle Condition

A set of three sides forms a valid triangle if the sum of any two sides is greater than the third side. This is checked using the conditions:
- \(a + b > c\)
- \(a + c > b\)
- \(b + c > a\)

### Area Calculation

If the sides form a valid triangle, the area is calculated using Heron's formula:
- Calculate the semi-perimeter: \(s = \frac{a + b + c}{2}\)
- Calculate the area: \(\text{area} = \sqrt{s \times (s - a) \times (s - b) \times (s - c)}\)

## Installation

No external dependencies are required for this software. It uses Python's built-in `math` library.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Import the Function:**

   To use the `triangle_area` function, you need to import it from the `main.py` file.

   ```python
   from main import triangle_area
   ```

2. **Calculate Triangle Area:**

   Call the `triangle_area` function with the lengths of the three sides as arguments.

   ```python
   area = triangle_area(3, 4, 5)
   print(area)  # Output: 6.00

   invalid_area = triangle_area(1, 2, 10)
   print(invalid_area)  # Output: -1
   ```

## Conclusion

This software provides a simple and efficient way to calculate the area of a triangle given its side lengths, ensuring the sides form a valid triangle before performing the calculation. It is a useful tool for educational purposes, geometry calculations, and quick validations of triangle properties.