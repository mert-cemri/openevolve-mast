# Triangle Area Calculator

This software provides a function to calculate the area of a triangle given the lengths of its three sides. It checks if the sides form a valid triangle and returns the area rounded to two decimal places if valid, otherwise returns -1.

## Main Function

### `triangle_area(a, b, c)`

- **Description**: This function calculates the area of a triangle using Heron's formula. It first checks if the given sides form a valid triangle. If they do, it computes the area and returns it rounded to two decimal places. If not, it returns -1.
  
- **Parameters**:
  - `a` (float): Length of the first side of the triangle.
  - `b` (float): Length of the second side of the triangle.
  - `c` (float): Length of the third side of the triangle.

- **Returns**: 
  - `float`: The area of the triangle rounded to two decimal places if the sides form a valid triangle.
  - `int`: -1 if the sides do not form a valid triangle.

- **Example Usage**:
  ```python
  print(triangle_area(3, 4, 5))  # Output: 6.00
  print(triangle_area(1, 2, 10)) # Output: -1
  ```

## Installation

This project does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: 
   - Clone the repository to your local machine using:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Project Directory**:
   - Change into the project directory:
     ```bash
     cd <project-directory>
     ```

3. **Run the Code**:
   - You can run the code directly using Python:
     ```bash
     python main.py
     ```

## Usage

To use the `triangle_area` function, simply import it into your Python script and call it with the lengths of the three sides of the triangle you wish to evaluate.

```python
from main import triangle_area

# Example usage
area1 = triangle_area(3, 4, 5)
print(f"The area of the triangle is: {area1}")

area2 = triangle_area(1, 2, 10)
print(f"The area of the triangle is: {area2}")
```

## Documentation

For further information on the implementation and usage of the function, please refer to the comments within the `main.py` file. The code is straightforward and well-documented to facilitate understanding and modification if necessary.