manual.md

```
# Triangle Area Calculator

This software provides a simple function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and then computes the area using Heron's formula.

## Main Functionality

The main function provided by this software is `triangle_area(a, b, c)`, which:

- Takes three arguments `a`, `b`, and `c`, representing the lengths of the sides of a triangle.
- Checks if the given sides can form a valid triangle using the triangle inequality theorem.
- If valid, calculates the area of the triangle using Heron's formula and returns the area rounded to two decimal places.
- If not valid, returns `-1`.

### Example Usage

```python
from main import triangle_area

# Example 1: Valid triangle
area = triangle_area(3, 4, 5)
print(area)  # Output: 6.00

# Example 2: Invalid triangle
area = triangle_area(1, 2, 10)
print(area)  # Output: -1
```

## Installation

This software does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

### Steps to Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```
   cd <repository-directory>
   ```

3. **Run the Code**: You can run the code directly using Python:
   ```
   python main.py
   ```

## Environment Dependencies

There are no external dependencies required for this software. It utilizes Python's built-in `math` library for calculations.

## Documentation

For further details on the implementation and usage, please refer to the inline comments within the `main.py` file. The code is straightforward and self-explanatory for users familiar with basic Python programming.

```