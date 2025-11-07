# Polynomial Solver

This software provides functions to evaluate a polynomial and find its root using the Newton-Raphson method. It is designed to solve polynomial equations by finding a zero point (root) of the polynomial.

## Main Functions

### 1. `poly(xs: list, x: float) -> float`

- **Description**: Evaluates a polynomial with given coefficients at a specified point.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial. The coefficient at index `i` corresponds to the term with degree `i`.
  - `x`: The point at which to evaluate the polynomial.
- **Returns**: The value of the polynomial at the given point `x`.

### 2. `poly_derivative(xs: list, x: float) -> float`

- **Description**: Evaluates the derivative of a polynomial with given coefficients at a specified point.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial.
  - `x`: The point at which to evaluate the derivative of the polynomial.
- **Returns**: The value of the derivative of the polynomial at the given point `x`.

### 3. `find_zero(xs: list) -> float`

- **Description**: Finds a root of the polynomial with given coefficients using the Newton-Raphson method.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial. The function assumes the list has an even number of coefficients and the largest non-zero coefficient guarantees a solution.
- **Returns**: A root of the polynomial.

## Installation

This project does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code**: You can run the code using a Python interpreter. For example, to find a root of a polynomial, you can use the following code snippet:

   ```python
   from main import find_zero

   # Example: Find a root of the polynomial f(x) = -6 + 11x - 6x^2 + x^3
   coefficients = [-6, 11, -6, 1]
   root = find_zero(coefficients)
   print(f"The root of the polynomial is: {root}")
   ```

4. **Modify and Test**: Feel free to modify the coefficients and test with different polynomials to find their roots.

## Example Usage

```python
from main import poly, find_zero

# Evaluate the polynomial f(x) = 1 + 2x at x = 3
coefficients = [1, 2]
value = poly(coefficients, 3)
print(f"The value of the polynomial at x = 3 is: {value}")

# Find a root of the polynomial f(x) = -6 + 11x - 6x^2 + x^3
coefficients = [-6, 11, -6, 1]
root = find_zero(coefficients)
print(f"The root of the polynomial is: {root}")
```

This software provides a straightforward way to evaluate polynomials and find their roots using efficient numerical methods.