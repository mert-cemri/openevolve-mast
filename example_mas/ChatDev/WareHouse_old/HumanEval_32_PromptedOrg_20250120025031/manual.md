# Polynomial Solver

This software provides functionality to evaluate polynomials and find their roots using the Newton-Raphson method. It is designed to handle polynomials with real coefficients and is implemented in Python.

## Main Functions

### 1. `poly(xs: list, x: float) -> float`
This function evaluates a polynomial at a given point `x`. The polynomial is defined by its coefficients `xs`, where `xs[i]` is the coefficient for the term `x^i`.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial.
  - `x`: The point at which to evaluate the polynomial.

- **Returns:**
  - The value of the polynomial at `x`.

### 2. `derivative(xs: list, x: float) -> float`
This function evaluates the derivative of a polynomial at a given point `x`. The polynomial is defined by its coefficients `xs`.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial.
  - `x`: The point at which to evaluate the derivative.

- **Returns:**
  - The value of the derivative of the polynomial at `x`.

### 3. `find_zero(xs: list) -> float`
This function finds a root of the polynomial using the Newton-Raphson method. It requires the polynomial to have an even number of coefficients and the largest non-zero coefficient to ensure a solution.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial.

- **Returns:**
  - A root of the polynomial.

- **Raises:**
  - `ValueError`: If the derivative is zero or if the maximum number of iterations is exceeded without finding a solution.

## Installation

No external dependencies are required for this software. It is implemented using Python's standard library.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Evaluate a Polynomial:**
   ```python
   from main import poly

   coefficients = [1, 2, 3]  # Represents the polynomial 1 + 2x + 3x^2
   x_value = 5
   result = poly(coefficients, x_value)
   print(f"The value of the polynomial at x={x_value} is {result}")
   ```

2. **Find a Root of a Polynomial:**
   ```python
   from main import find_zero

   coefficients = [-6, 11, -6, 1]  # Represents the polynomial -6 + 11x - 6x^2 + x^3
   root = find_zero(coefficients)
   print(f"A root of the polynomial is {root}")
   ```

## Documentation

For further details on how the functions work, refer to the docstrings provided in the source code. These provide examples and additional information on the expected input and output for each function.