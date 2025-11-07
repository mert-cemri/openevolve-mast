manual.md

```
# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and returns the area rounded to two decimal points. If the sides do not form a valid triangle, it returns -1.

## Main Function

### `triangle_area(a, b, c)`

- **Description**: 
  - Calculates the area of a triangle using Heron's formula.
  - Validates if the given sides can form a triangle.
  - Returns the area rounded to two decimal places if valid, otherwise returns -1.

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

  invalid_area = triangle_area(1, 2, 10)
  print(invalid_area)  # Output: -1
  ```

## Installation

This software does not require any external dependencies beyond the Python standard library. However, it uses the `math` module, which is included with Python.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

To check if Python is installed, run the following command in your terminal or command prompt:

```bash
python --version
```

## How to Use

1. **Clone the Repository**: 
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Directory**:
   - Change into the directory where the `main.py` file is located:
     ```bash
     cd <repository-directory>
     ```

3. **Run the Code**:
   - You can run the `main.py` file directly to test the `triangle_area` function:
     ```bash
     python main.py
     ```

4. **Integrate into Your Project**:
   - You can copy the `triangle_area` function into your own Python project and use it as needed.

## Notes

- Ensure that the input values for the sides are positive numbers.
- The function uses Heron's formula, which is suitable for calculating the area of a triangle when the lengths of all three sides are known.

```