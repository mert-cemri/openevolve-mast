```markdown
# Rescale to Unit

A simple Python module to rescale a list of numbers such that the smallest number becomes 0 and the largest becomes 1.

## Overview

The `rescale_to_unit` function takes a list of floating-point numbers and applies a linear transformation to rescale the numbers. This transformation ensures that the smallest number in the list becomes 0 and the largest becomes 1, with all other numbers proportionally adjusted between these two values.

## Main Function

### `rescale_to_unit(numbers: List[float]) -> List[float]`

- **Parameters**: 
  - `numbers`: A list of floating-point numbers with at least two elements.

- **Returns**: 
  - A new list of floating-point numbers where the smallest number is 0 and the largest is 1, with all other numbers linearly transformed accordingly.

- **Example**:
  ```python
  >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
  [0.0, 0.25, 0.5, 0.75, 1.0]
  ```

## Installation

This module does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**: 
   - Clone or download the repository to your local machine.

2. **Navigate to the Directory**:
   - Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**:
   - You can use the function in a Python script or an interactive Python session.
   - Example usage in a Python script:
     ```python
     from main import rescale_to_unit

     numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
     rescaled_numbers = rescale_to_unit(numbers)
     print(rescaled_numbers)
     ```

4. **Testing**:
   - You can test the function using the provided example or by passing different lists of numbers to ensure it behaves as expected.

## Documentation

For further details and documentation, refer to the docstring within the `main.py` file, which provides a concise explanation of the function's purpose and usage.

## Support

For any issues or questions, please contact our support team or visit our website for more information.

```
```