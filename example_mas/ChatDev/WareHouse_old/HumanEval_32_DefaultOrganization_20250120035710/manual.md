manual.md

```
# Polynomial Solver

This software provides functionality to evaluate polynomials at a given point and find a zero of the polynomial using the bisection method. It is designed to handle polynomials with an even number of coefficients and guarantees a solution under these conditions.

## Main Functions

### 1. `poly(xs: list, x: float)`

- **Description**: Evaluates a polynomial with given coefficients at a specified point.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial. The list should be ordered from the constant term to the highest degree term.
  - `x`: The point at which the polynomial is to be evaluated.
- **Returns**: The value of the polynomial at the given point `x`.

### 2. `find_zero(xs: list)`

- **Description**: Finds a zero of the polynomial using the bisection method. It returns only one zero point, even if there are multiple.
- **Parameters**:
  - `xs`: A list of coefficients for the polynomial. The list should have an even number of coefficients.
- **Returns**: A float representing a zero of the polynomial.
- **Example Usage**:
  - `round(find_zero([1, 2]), 2)` returns `-0.5` for the polynomial `f(x) = 1 + 2x`.
  - `round(find_zero([-6, 11, -6, 1]), 2)` returns `1.0` for the polynomial `(x - 1) * (x - 2) * (x - 3)`.

## Installation

This software does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

## Usage

1. **Run the Script**: Execute the `main.py` script using Python.

   ```bash
   python main.py
   ```

2. **Example Output**: The script will print the zero points of example polynomials as specified in the code.

## Documentation

For further details on the implementation and usage, please refer to the comments within the `main.py` file. The code is documented to provide insights into the logic and methodology used for polynomial evaluation and zero finding.

```