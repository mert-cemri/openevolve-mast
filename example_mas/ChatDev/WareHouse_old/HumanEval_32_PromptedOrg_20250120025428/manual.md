# Polynomial Solver

This software provides functionality to evaluate polynomials and find their roots using the Newton-Raphson method. It is designed to handle polynomials with coefficients provided in a list format and can find a single root of the polynomial.

## Main Functions

### 1. `poly(xs: list, x: float) -> float`

This function evaluates a polynomial at a given point `x`. The polynomial is defined by its coefficients provided in the list `xs`, where each element corresponds to the coefficient of the term with the respective power.

- **Parameters:**
  - `xs`: A list of coefficients `[a0, a1, a2, ..., an]` for the polynomial `a0 + a1*x + a2*x^2 + ... + an*x^n`.
  - `x`: The point at which to evaluate the polynomial.

- **Returns:** The value of the polynomial at point `x`.

### 2. `derivative(xs: list, x: float) -> float`

This function evaluates the derivative of the polynomial at a given point `x`.

- **Parameters:**
  - `xs`: A list of coefficients `[a0, a1, a2, ..., an]` for the polynomial.
  - `x`: The point at which to evaluate the derivative.

- **Returns:** The value of the derivative of the polynomial at point `x`.

### 3. `find_zero(xs: list) -> float`

This function finds a root of the polynomial using the Newton-Raphson method. It assumes that the polynomial has an even number of coefficients and that the largest non-zero coefficient guarantees a solution.

- **Parameters:**
  - `xs`: A list of coefficients `[a0, a1, a2, ..., an]` for the polynomial.

- **Returns:** A root of the polynomial.

- **Exceptions:** Raises a `ValueError` if the derivative is zero or if the maximum number of iterations is exceeded without finding a solution.

## Installation

This software does not require any external dependencies. It uses Python's built-in `math` library.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

No additional packages are required, so you can directly run the software using Python.

## Usage

To use this software, you can create a Python script or use an interactive Python shell. Below are examples of how to use the main functions:

```python
import math

# Example usage of poly function
coefficients = [1, 2]  # Represents the polynomial f(x) = 1 + 2x
x_value = 3
result = poly(coefficients, x_value)
print(f"The value of the polynomial at x = {x_value} is {result}")

# Example usage of find_zero function
coefficients = [-6, 11, -6, 1]  # Represents the polynomial (x - 1) * (x - 2) * (x - 3)
root = find_zero(coefficients)
print(f"A root of the polynomial is {root}")
```

## Documentation

For further details on the functions and their usage, refer to the function docstrings in the code. The software is designed to be straightforward and easy to integrate into other Python projects.