# Polynomial Solver

This software provides functions to evaluate a polynomial and find its zero using Newton's method. It is designed to handle polynomials with real coefficients and find one of their roots.

## Main Functions

### 1. `poly(xs: list, x: float)`

- **Description**: Evaluates a polynomial with given coefficients at a specified point.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial. The coefficient at index `i` corresponds to the term with degree `i`.
  - `x`: The point at which to evaluate the polynomial.
- **Returns**: The value of the polynomial at point `x`.

### 2. `derivative(xs: list, x: float)`

- **Description**: Evaluates the derivative of a polynomial with given coefficients at a specified point.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial.
  - `x`: The point at which to evaluate the derivative.
- **Returns**: The value of the derivative at point `x`.

### 3. `find_zero(xs: list, initial_guess: float = 0.0, tolerance: float = 1e-7, max_iterations: int = 1000)`

- **Description**: Finds a zero of the polynomial using Newton's method.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial.
  - `initial_guess`: An initial guess for the root. Default is `0.0`.
  - `tolerance`: The tolerance for convergence. Default is `1e-7`.
  - `max_iterations`: The maximum number of iterations to perform. Default is `1000`.
- **Returns**: A root of the polynomial.
- **Raises**: 
  - `ValueError` if the list of coefficients does not have an even number of elements or if the largest coefficient is zero.
  - `ValueError` if the derivative is zero during iterations or if no solution is found after maximum iterations.

## Installation

This software does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can use the functions in `main.py` by importing them into your Python script or interactive session.

```python
from main import poly, find_zero

# Example usage
coefficients = [-6, 11, -6, 1]  # Coefficients for the polynomial (x - 1)(x - 2)(x - 3)
root = find_zero(coefficients)
print(f"Found root: {root}")
```

4. **Testing**: You can test the functions using the provided examples in the docstrings.

## Notes

- Ensure that the list of coefficients has an even number of elements and that the largest coefficient is non-zero to guarantee a solution.
- The initial guess is crucial for the convergence of Newton's method. Adjust it if the method fails to find a root.

This manual provides an overview of the software's functionality and usage. For further assistance, please refer to the code comments and docstrings within `main.py`.