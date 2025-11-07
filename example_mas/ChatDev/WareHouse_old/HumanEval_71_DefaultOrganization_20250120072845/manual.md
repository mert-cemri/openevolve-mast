manual.md

```
# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and then computes the area using Heron's formula.

## Main Functionality

The main function of this software is:

- **triangle_area(a, b, c)**: This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle. It returns the area of the triangle rounded to two decimal places if the sides form a valid triangle. If the sides do not form a valid triangle, it returns -1.

### How It Works

1. **Validation**: The function first checks if the given sides can form a valid triangle. A valid triangle satisfies the condition that the sum of any two sides is greater than the third side.

2. **Area Calculation**: If the sides form a valid triangle, the function calculates the semi-perimeter `s` using the formula:
   \[
   s = \frac{a + b + c}{2}
   \]
   Then, it calculates the area using Heron's formula:
   \[
   \text{area} = \sqrt{s \times (s - a) \times (s - b) \times (s - c)}
   \]
   The result is rounded to two decimal places.

3. **Invalid Triangle**: If the sides do not form a valid triangle, the function returns -1.

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python environment. Simply copy the code into your Python script or interactive environment.

## Usage

To use the `triangle_area` function, follow these steps:

1. Open your Python environment or script editor.
2. Copy the function code into your environment or script.
3. Call the function with the desired side lengths. For example:

```python
# Example usage
area1 = triangle_area(3, 4, 5)
print(area1)  # Output: 6.00

area2 = triangle_area(1, 2, 10)
print(area2)  # Output: -1
```

## Documentation

For further details on the mathematical concepts used, you may refer to resources on triangle geometry and Heron's formula.

```