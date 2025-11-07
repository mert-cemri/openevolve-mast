# Polynomial Solver User Manual

Welcome to the Polynomial Solver software! This application is designed to evaluate polynomials and find their zero points using a simple bisection method. This manual will guide you through the main functions of the software, how to set up the environment, and how to use the software effectively.

## Main Functions

### 1. `poly(xs: list, x: float)`

This function evaluates a polynomial at a given point `x`. The polynomial is defined by its coefficients provided in the list `xs`.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial. The first element is the constant term, the second is the coefficient of `x`, the third is the coefficient of `x^2`, and so on.
  - `x`: The point at which the polynomial is to be evaluated.

- **Returns:** The value of the polynomial at the point `x`.

### 2. `find_zero(xs: list)`

This function finds a zero of the polynomial defined by the coefficients in `xs`. It uses a bisection method to find a root.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial. The list must have an even number of coefficients, and the largest non-zero coefficient guarantees a solution.

- **Returns:** A single zero point of the polynomial.

## Installation

### Environment Setup

This software does not require any external dependencies, making it straightforward to set up. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py` in your terminal or command prompt.

## How to Use

1. **Run the Script:**

   Open your terminal or command prompt, navigate to the directory containing `main.py`, and run the following command:

   ```bash
   python main.py
   ```

2. **Example Usage:**

   The script includes example usage of the `find_zero` function. When you run the script, it will output the zero points for the example polynomials:

   - For the polynomial `f(x) = 1 + 2x`, it will output `-0.5`.
   - For the polynomial `(x - 1) * (x - 2) * (x - 3)`, it will output `1.0`.

3. **Custom Usage:**

   You can modify the `main.py` file to evaluate different polynomials by changing the coefficients in the `find_zero` function calls. Simply replace the lists `[1, 2]` or `[-6, 11, -6, 1]` with your desired coefficients.

## Documentation

For further details on how the functions work, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the program.

Thank you for using the Polynomial Solver software! If you have any questions or need further assistance, please feel free to reach out.