manual.md

```
# Polynomial Solver

This software provides a simple and efficient way to evaluate polynomials and find their roots using Python. It includes two main functions: `poly` for evaluating polynomials and `find_zero` for finding a root of a polynomial.

## Main Functions

### 1. `poly(xs: list, x: float) -> float`

This function evaluates a polynomial at a given point `x`. The polynomial is defined by its coefficients `xs`, where `xs[i]` is the coefficient for the term `x^i`.

**Usage Example:**

```python
import math

coefficients = [1, 2, 3]  # Represents the polynomial 1 + 2x + 3x^2
x_value = 5
result = poly(coefficients, x_value)
print(result)  # Output: 86.0
```

### 2. `find_zero(xs: list) -> float`

This function finds a zero of the polynomial defined by the coefficients `xs`. It uses the bisection method to find a root, assuming the polynomial has at least one real root.

**Usage Example:**

```python
coefficients = [-6, 11, -6, 1]  # Represents the polynomial -6 + 11x - 6x^2 + x^3
root = find_zero(coefficients)
print(round(root, 2))  # Output: 1.0
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Software:**

   You can run the software directly using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Evaluate a Polynomial:**

   Use the `poly` function to evaluate a polynomial at a specific point. Pass the list of coefficients and the point as arguments.

2. **Find a Root of a Polynomial:**

   Use the `find_zero` function to find a root of the polynomial. Pass the list of coefficients as an argument.

## Example Usage

The `main.py` file includes example usage of both functions. You can run this file to see the functions in action:

```bash
python main.py
```

This will output the results of evaluating and finding roots for example polynomials.

## Documentation

For further details and documentation, please refer to the comments within the code in `main.py`. The code is well-documented to help you understand the functionality and usage of each function.

```