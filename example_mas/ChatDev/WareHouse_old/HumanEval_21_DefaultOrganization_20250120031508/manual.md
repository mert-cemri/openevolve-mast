```markdown
# Rescale to Unit

A simple Python utility to normalize a list of numbers such that the smallest number becomes 0 and the largest becomes 1.

## Overview

The `rescale_to_unit` function takes a list of floating-point numbers and applies a linear transformation to rescale the numbers. This transformation ensures that the smallest number in the list is transformed to 0 and the largest number is transformed to 1. This is useful in various data processing tasks where normalization of data is required.

## Main Function

### `rescale_to_unit(numbers: List[float]) -> List[float]`

- **Description**: This function normalizes a list of numbers.
- **Parameters**: 
  - `numbers`: A list of floating-point numbers with at least two elements.
- **Returns**: A list of floating-point numbers rescaled to the unit interval [0, 1].
- **Example**:
  ```python
  >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
  [0.0, 0.25, 0.5, 0.75, 1.0]
  ```

## Installation

This utility does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Function**: You can use the function by importing it into your Python script or by running it directly in an interactive Python session.

   ```python
   from main import rescale_to_unit

   numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   rescaled_numbers = rescale_to_unit(numbers)
   print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
   ```

3. **Modify and Test**: Feel free to modify the list of numbers to test the function with different inputs.

## No External Dependencies

This project does not require any external Python packages. It relies solely on Python's standard library.

## Conclusion

The `rescale_to_unit` function is a straightforward and efficient way to normalize data. It can be easily integrated into larger data processing pipelines or used as a standalone utility for data normalization tasks.
```
```