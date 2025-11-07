manual.md

```
# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and returns the area rounded to two decimal places. If the sides do not form a valid triangle, it returns -1.

## Main Functionality

The main function provided by this software is:

- `triangle_area(a, b, c)`: This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle. It returns the area of the triangle rounded to two decimal places if the sides form a valid triangle. Otherwise, it returns -1.

### Valid Triangle Check

A triangle is valid if the sum of any two sides is greater than the third side. The function checks this condition before calculating the area.

### Area Calculation

If the sides form a valid triangle, the area is calculated using Heron's formula:

\[ \text{Area} = \sqrt{s \cdot (s - a) \cdot (s - b) \cdot (s - c)} \]

where \( s \) is the semi-perimeter of the triangle:

\[ s = \frac{a + b + c}{2} \]

## Installation

There are no external dependencies required for this software. You can directly use the function in your Python environment.

## Usage

1. **Import the Function**: Copy the `triangle_area` function into your Python script or interactive environment.

2. **Call the Function**: Use the function by passing the lengths of the three sides of the triangle as arguments. For example:

   ```python
   area = triangle_area(3, 4, 5)
   print(area)  # Output: 6.00

   invalid_area = triangle_area(1, 2, 10)
   print(invalid_area)  # Output: -1
   ```

3. **Interpret the Results**: The function will return the area of the triangle if the sides are valid, or -1 if they are not.

## Example

Here's a quick example to demonstrate how to use the function:

```python
def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1

# Example usage
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
```

This software is a simple utility for calculating the area of a triangle and can be easily integrated into larger projects or used for educational purposes.
```