manual.md

```
# Polynomial Solver

This software provides functions to evaluate polynomials and find their roots using the Newton-Raphson method. It is designed to handle polynomials with real coefficients and find a single root efficiently.

## Main Functions

### 1. `poly(xs: list, x: float) -> float`
This function evaluates a polynomial at a given point `x`. The polynomial is defined by its coefficients `xs`, where `xs[i]` is the coefficient for the term `x^i`.

#### Example Usage:
```python
coefficients = [1, 2, 3]  # Represents the polynomial 1 + 2x + 3x^2
value = poly(coefficients, 2)  # Evaluates the polynomial at x = 2
print(value)  # Output: 17.0
```

### 2. `derivative(xs: list) -> list`
This function computes the derivative of a polynomial given its coefficients `xs`. The result is a list of coefficients representing the derivative polynomial.

#### Example Usage:
```python
coefficients = [1, 2, 3]  # Represents the polynomial 1 + 2x + 3x^2
derivative_coeffs = derivative(coefficients)
print(derivative_coeffs)  # Output: [2, 6] which represents 2 + 6x
```

### 3. `find_zero(xs: list, initial_guess=0.0, tolerance=1e-7, max_iterations=1000) -> float`
This function finds a root of the polynomial defined by coefficients `xs` using the Newton-Raphson method. It starts from an `initial_guess` and iterates until the result is within the specified `tolerance` or the `max_iterations` is reached.

#### Example Usage:
```python
coefficients = [1, 2]  # Represents the polynomial 1 + 2x
root = find_zero(coefficients)
print(round(root, 2))  # Output: -0.5
```

## Installation

This project does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script:**
   You can directly run the `main.py` script to test the functionality:
   ```bash
   python main.py
   ```

## How to Use

1. **Evaluate a Polynomial:**
   Use the `poly` function to evaluate a polynomial at a specific point.

2. **Find a Root:**
   Use the `find_zero` function to find a root of the polynomial. Adjust the `initial_guess`, `tolerance`, and `max_iterations` parameters as needed for your specific use case.

## Documentation

For more detailed documentation, please refer to the comments within the code. Each function is documented with its purpose, parameters, and example usage.

This software is designed to be simple and efficient for solving polynomial equations using the Newton-Raphson method. It is suitable for educational purposes and basic computational tasks involving polynomials.
```