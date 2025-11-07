# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and then computes the area using Heron's formula. The result is rounded to two decimal places.

## Main Function

### `triangle_area(a, b, c)`

- **Description**: 
  - This function calculates the area of a triangle using the lengths of its three sides.
  - It first checks if the given sides can form a valid triangle. A valid triangle is one where the sum of any two sides is greater than the third side.
  - If the sides form a valid triangle, it calculates the area using Heron's formula and returns the area rounded to two decimal places.
  - If the sides do not form a valid triangle, it returns -1.

- **Parameters**:
  - `a` (float): Length of the first side of the triangle.
  - `b` (float): Length of the second side of the triangle.
  - `c` (float): Length of the third side of the triangle.

- **Returns**:
  - `float`: The area of the triangle rounded to two decimal places, or -1 if the sides do not form a valid triangle.

- **Example Usage**:
  ```python
  area = triangle_area(3, 4, 5)
  print(area)  # Output: 6.00

  area = triangle_area(1, 2, 10)
  print(area)  # Output: -1
  ```

## Installation

No external dependencies are required for this software. It is implemented in pure Python.

## How to Use

1. **Ensure Python is Installed**: 
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Create a Python File**:
   - Create a file named `main.py` and copy the function code provided into this file.

3. **Run the Function**:
   - You can call the `triangle_area` function with the desired side lengths to calculate the area of a triangle.
   - Use a Python interpreter or any Python IDE to run your script.

4. **Example**:
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
   print(triangle_area(1, 2, 10)) # Output: -1
   ```

This manual provides all the necessary information to use the Triangle Area Calculator function effectively. Enjoy calculating triangle areas with ease!