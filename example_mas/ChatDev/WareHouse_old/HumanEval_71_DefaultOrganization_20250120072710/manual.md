manual.md

```
# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and then computes the area using Heron's formula.

## Main Functionality

- **triangle_area(a, b, c):** This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle. It returns the area of the triangle rounded to two decimal places if the sides form a valid triangle. If the sides do not form a valid triangle, it returns -1.

### Valid Triangle Condition

A valid triangle is formed if the sum of any two sides is greater than the third side. The function checks this condition before calculating the area.

### Heron's Formula

If the sides form a valid triangle, the area is calculated using Heron's formula:
\[ \text{Area} = \sqrt{s \times (s-a) \times (s-b) \times (s-c)} \]
where \( s \) is the semi-perimeter of the triangle:
\[ s = \frac{a + b + c}{2} \]

## Installation

No external dependencies are required for this software. It is implemented in pure Python.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change your current directory to the location of the cloned repository:
   ```
   cd <repository-directory>
   ```

3. **Run the Function:**

   You can use the `triangle_area` function in your Python scripts. Here's an example of how to use it:

   ```python
   from main import triangle_area

   # Example usage
   area1 = triangle_area(3, 4, 5)
   print(f"Area of triangle with sides 3, 4, 5: {area1}")  # Output: 6.00

   area2 = triangle_area(1, 2, 10)
   print(f"Area of triangle with sides 1, 2, 10: {area2}")  # Output: -1
   ```

4. **Testing:**

   You can test the function with different sets of side lengths to verify its correctness.

## Documentation

For more detailed documentation, please refer to the comments within the `main.py` file, which explain the logic and implementation of the `triangle_area` function.

```