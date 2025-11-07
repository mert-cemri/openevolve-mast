manual.md

```
# Simplify Function

This software provides a simple utility function to determine if the product of two fractions results in a whole number. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Function

### simplify(x, n)

- **Description**: The `simplify` function takes two string inputs representing fractions and checks if their product is a whole number.
- **Parameters**:
  - `x`: A string representing a fraction in the format `<numerator>/<denominator>`.
  - `n`: A string representing a fraction in the format `<numerator>/<denominator>`.
- **Returns**: A boolean value:
  - `True` if the product of the two fractions is a whole number.
  - `False` otherwise.

- **Example Usage**:
  ```python
  simplify("1/5", "5/1")  # Returns: True
  simplify("1/6", "2/1")  # Returns: False
  simplify("7/10", "10/2")  # Returns: False
  ```

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python, making it easy to integrate into any Python project.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository containing the `main.py` file.
3. No additional installation steps are required as there are no dependencies.

## How to Use

1. Open the `main.py` file in your preferred Python IDE or text editor.
2. Use the `simplify` function by passing two fraction strings as arguments.
3. Run the script to see the output.

## Example

Here's a quick example of how you might use the `simplify` function in a Python script:

```python
from main import simplify

# Example fractions
fraction1 = "1/5"
fraction2 = "5/1"

# Check if the product is a whole number
is_whole_number = simplify(fraction1, fraction2)
print(f"The product of {fraction1} and {fraction2} is a whole number: {is_whole_number}")
```

## Documentation

For further information and updates, please refer to the source code comments and examples provided within the `main.py` file.
```
