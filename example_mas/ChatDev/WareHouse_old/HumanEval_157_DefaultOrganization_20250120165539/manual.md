manual.md

```
# Right Angle Triangle Checker

This software provides a simple function to determine if three given side lengths can form a right-angled triangle. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The core functionality of this software is encapsulated in the `right_angle_triangle` function. This function takes three arguments, representing the lengths of the sides of a triangle, and returns a boolean value indicating whether these sides can form a right-angled triangle.

### Function Definition

```python
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Sort the sides so that the largest side is last
    sides = sorted([a, b, c])
    # Check if the square of the largest side is equal to the sum of the squares of the other two sides
    return sides[0]**2 + sides[1]**2 == sides[2]**2
```

## Installation

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   There are no additional dependencies required for this project beyond Python itself. Ensure you have Python installed on your system.

## Usage

To use the `right_angle_triangle` function, you can import it into your Python script and call it with the desired side lengths. Here is an example of how to use the function:

```python
from main import right_angle_triangle

# Example usage
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

## Testing

You can test the function by running the script and checking the output for various sets of side lengths. The function should return `True` for sets of lengths that form a right-angled triangle and `False` otherwise.

## Conclusion

This software provides a simple and efficient way to check if three side lengths can form a right-angled triangle. It is easy to integrate into other Python projects and requires no additional dependencies.
```