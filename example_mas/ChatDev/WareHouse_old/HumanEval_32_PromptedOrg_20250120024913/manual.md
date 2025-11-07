# Polynomial Solver

This software provides functionality to evaluate polynomials and find their zeros using the Newton-Raphson method. It is designed to handle polynomials with real coefficients and find one real root.

## Main Functions

### 1. `poly(xs: list, x: float) -> float`

This function evaluates a polynomial at a given point `x`. The polynomial is defined by its coefficients `xs`, where `xs[i]` is the coefficient for the term `x^i`.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial.
  - `x`: The point at which to evaluate the polynomial.

- **Returns:**
  - The value of the polynomial at the point `x`.

### 2. `derivative(xs: list) -> list`

This function computes the derivative of a polynomial given its coefficients.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial.

- **Returns:**
  - A list of coefficients representing the derivative of the polynomial.

### 3. `find_zero(xs: list, initial_guess: float = 0.0) -> float`

This function finds a zero of the polynomial using the Newton-Raphson method. It assumes the polynomial has a real root and allows the user to specify an initial guess for the root.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial.
  - `initial_guess`: An optional initial guess for the root (default is 0.0).

- **Returns:**
  - A real number representing a root of the polynomial.

- **Raises:**
  - `ValueError`: If the derivative is too small or if the maximum number of iterations is reached without finding a solution.

## Installation

This software does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

## Usage

To use the software, follow these steps:

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change into the directory containing the `main.py` file:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Script:**

   Execute the `main.py` script to evaluate polynomials and find their zeros:

   ```bash
   python main.py
   ```

   Example usage within the script:

   ```python
   print(round(find_zero([1, 2]), 2))  # Should output -0.5
   print(round(find_zero([-6, 11, -6, 1]), 2))  # Should output 1.0
   ```

## Documentation

For further details on the implementation and usage of each function, refer to the docstrings provided in the `main.py` file. The code is self-documented to assist with understanding the functionality and expected inputs/outputs.

## Support

For any issues or questions, please contact our support team or visit our community forums for assistance.