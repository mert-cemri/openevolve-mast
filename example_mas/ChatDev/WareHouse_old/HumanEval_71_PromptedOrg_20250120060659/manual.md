# Triangle Area Calculator

This software module provides a function to calculate the area of a triangle given the lengths of its sides. It verifies if the given sides can form a valid triangle and then computes the area using Heron's formula.

## Main Functionality

The main function in this module is `triangle_area(a, b, c)`, which:

- Takes three arguments `a`, `b`, and `c`, representing the lengths of the sides of a triangle.
- Checks if these sides can form a valid triangle. A triangle is valid if the sum of any two sides is greater than the third side.
- If the sides form a valid triangle, it calculates the area using Heron's formula and returns the area rounded to two decimal places.
- If the sides do not form a valid triangle, it returns `-1`.

### Example Usage

```python
from main import triangle_area

# Valid triangle
area = triangle_area(3, 4, 5)
print(area)  # Output: 6.00

# Invalid triangle
area = triangle_area(1, 2, 10)
print(area)  # Output: -1
```

## Installation

This module does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Ensure Python is installed** on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **No additional packages are required**, as the module only uses the `math` library, which is included in Python's standard library.

## How to Use

1. **Import the function**: Import the `triangle_area` function from the `main.py` file into your Python script.

2. **Call the function**: Pass the lengths of the three sides of the triangle as arguments to the `triangle_area` function.

3. **Receive the result**: The function will return the area of the triangle rounded to two decimal places if the sides form a valid triangle, or `-1` if they do not.

## Documentation

For further details on the implementation and examples, refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into larger projects where triangle area calculations are needed.