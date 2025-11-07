# Right Angle Triangle Checker

This software provides a simple function to determine if three given side lengths can form a right-angled triangle. It uses the Pythagorean theorem to verify the condition for a right-angled triangle.

## Main Functionality

The main function provided by this software is:

- `right_angle_triangle(a, b, c)`: This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle. It returns `True` if the sides form a right-angled triangle, and `False` otherwise.

### Example Usage

```python
right_angle_triangle(3, 4, 5)  # Returns: True
right_angle_triangle(1, 2, 3)  # Returns: False
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## How to Use

1. **Clone or Download the Repository**: Start by cloning or downloading the repository containing the `main.py` file.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Python Script**: You can run the script using Python to test the function. For example:

   ```bash
   python main.py
   ```

4. **Use the Function in Your Code**: You can import the `right_angle_triangle` function into your own Python scripts to use it as needed.

   ```python
   from main import right_angle_triangle

   # Example usage
   print(right_angle_triangle(3, 4, 5))  # Output: True
   ```

## Documentation

The function uses the Pythagorean theorem to determine if the given sides form a right-angled triangle. The sides are first sorted to ensure the largest side is treated as the hypotenuse. The function then checks if the sum of the squares of the two smaller sides equals the square of the largest side.

For further information or questions, please refer to the comments within the `main.py` file or contact our support team.