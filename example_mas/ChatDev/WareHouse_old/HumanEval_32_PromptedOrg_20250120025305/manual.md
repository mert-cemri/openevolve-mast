# Polynomial Solver

This software provides functions to evaluate a polynomial and find its root using the Newton-Raphson method. It is designed to solve polynomial equations by finding a zero point of the polynomial.

## Main Functions

### 1. `poly(xs: list, x: float)`

- **Description**: Evaluates a polynomial with given coefficients at a specific point.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial.
  - `x`: The point at which the polynomial is evaluated.
- **Returns**: The value of the polynomial at point `x`.

### 2. `derivative(xs: list, x: float)`

- **Description**: Evaluates the derivative of the polynomial with given coefficients at a specific point.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial.
  - `x`: The point at which the derivative is evaluated.
- **Returns**: The value of the derivative of the polynomial at point `x`.

### 3. `find_zero(xs: list)`

- **Description**: Finds a root of the polynomial using the Newton-Raphson method.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial. The list must have an odd number of coefficients.
- **Returns**: A zero point of the polynomial.
- **Raises**:
  - `ValueError`: If the list of coefficients does not have an odd number of elements or if the derivative is zero during the iteration process.

## Installation

This software does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code**: You can use the functions defined in `main.py` by importing them into your Python script or interactive session.

   Example usage:

   ```python
   from main import poly, find_zero

   # Evaluate a polynomial
   coefficients = [1, 2, 3]  # Represents 1 + 2x + 3x^2
   x_value = 1.5
   result = poly(coefficients, x_value)
   print(f"Polynomial value at x={x_value}: {result}")

   # Find a zero of the polynomial
   zero = find_zero([1, -3, 2])  # Represents x^2 - 3x + 2
   print(f"Zero of the polynomial: {zero}")
   ```

4. **Error Handling**: Be aware of potential `ValueError` exceptions if the list of coefficients does not meet the requirements or if the derivative becomes zero during the iteration.

## Documentation

For further details on the implementation and examples, please refer to the comments within the `main.py` file. The code is self-documented to provide insights into the logic and usage of each function.