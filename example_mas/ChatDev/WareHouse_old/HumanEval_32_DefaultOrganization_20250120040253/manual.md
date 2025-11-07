# Polynomial Solver User Manual

Welcome to the Polynomial Solver software! This tool is designed to evaluate polynomials and find their zeros using the Newton-Raphson method. This manual will guide you through the main functions of the software, how to install the necessary environment, and how to use the software effectively.

## Main Functions

The Polynomial Solver provides the following key functions:

1. **poly(xs: list, x: float) -> float**: 
   - Evaluates a polynomial at a given point `x`.
   - `xs` is a list of coefficients, where `xs[i]` is the coefficient for the term `x^i`.

2. **derivative(xs: list) -> list**:
   - Computes the derivative of the polynomial with coefficients `xs`.
   - Returns a list of coefficients for the derivative polynomial.

3. **find_zero(xs: list, initial_guess=0.0, tolerance=1e-7, max_iterations=1000) -> float**:
   - Finds a zero of the polynomial using the Newton-Raphson method.
   - `xs` is a list of coefficients of the polynomial.
   - `initial_guess` is the starting point for the iteration.
   - `tolerance` is the precision of the result.
   - `max_iterations` is the maximum number of iterations allowed.

## Installation

The software does not require any external packages beyond Python's standard library. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**:
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**:
   - Clone the repository to your local machine using:
     ```bash
     git clone <repository-url>
     ```

3. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the directory where the project is located.

## How to Use

1. **Running the Software**:
   - Open a terminal in the project directory.
   - Run the script using Python:
     ```bash
     python main.py
     ```

2. **Example Usage**:
   - The script includes example usage of the `find_zero` function:
     - For the polynomial `f(x) = 1 + 2x`, it should return `-0.5`.
     - For the polynomial `f(x) = -6 + 11x - 6x^2 + x^3`, it should return `1.0`.

3. **Custom Usage**:
   - You can modify the `main.py` file to test other polynomials by changing the coefficients in the `find_zero` function call.

## Troubleshooting

- **Derivative is Zero**: If the derivative of the polynomial at a point is zero, the Newton-Raphson method cannot proceed. Ensure the initial guess is not at a point where the derivative is zero.
- **Exceeded Maximum Iterations**: If the maximum number of iterations is exceeded, try increasing `max_iterations` or adjusting the `initial_guess`.

For further assistance, please contact our support team.

Thank you for using the Polynomial Solver!