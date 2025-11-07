manual.md

```
# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. The function checks if the sides form a valid triangle and, if so, calculates the area using Heron's formula. The result is rounded to two decimal places.

## Main Function

### `triangle_area(a, b, c)`

- **Description**: 
  - This function takes three arguments, `a`, `b`, and `c`, which represent the lengths of the sides of a triangle.
  - It checks if the given sides can form a valid triangle. A valid triangle is one where the sum of any two sides is greater than the third side.
  - If the sides form a valid triangle, the function calculates the area using Heron's formula and returns the area rounded to two decimal places.
  - If the sides do not form a valid triangle, the function returns `-1`.

- **Parameters**:
  - `a` (float): Length of the first side of the triangle.
  - `b` (float): Length of the second side of the triangle.
  - `c` (float): Length of the third side of the triangle.

- **Returns**:
  - `float`: The area of the triangle rounded to two decimal places if the sides form a valid triangle.
  - `int`: `-1` if the sides do not form a valid triangle.

- **Example Usage**:
  ```python
  area1 = triangle_area(3, 4, 5)  # Returns 6.00
  area2 = triangle_area(1, 2, 10) # Returns -1
  ```

## Installation

There are no external dependencies required for this software. It uses Python's built-in `math` library.

### Environment Setup

1. **Python Installation**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```bash
   cd <repository-directory>
   ```

4. **Run the Code**: You can run the code directly using Python:
   ```bash
   python main.py
   ```

## Usage

To use the `triangle_area` function, simply import it into your Python script and call it with the lengths of the triangle sides as arguments. Ensure that the values provided are positive numbers.

```python
from main import triangle_area

# Example usage
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10)) # Output: -1
```

## Documentation

For further information and examples, please refer to the inline comments within the `main.py` file. The code is straightforward and well-documented to assist in understanding its functionality.
```