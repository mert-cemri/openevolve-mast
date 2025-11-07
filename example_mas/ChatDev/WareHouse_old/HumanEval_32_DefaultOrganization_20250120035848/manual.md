manual.md

```
# Polynomial Solver

This software provides functions to evaluate a polynomial at a given point and to find a zero of the polynomial using the Newton-Raphson method. It is designed to solve polynomial equations efficiently and accurately.

## Main Functions

### 1. `poly(xs: list, x: float) -> float`

This function evaluates a polynomial with given coefficients at a specified point.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial. The list should be ordered from the constant term to the highest degree term.
  - `x`: The point at which to evaluate the polynomial.

- **Returns:** The value of the polynomial at the given point `x`.

### 2. `find_zero(xs: list) -> float`

This function finds a zero of the polynomial using the Newton-Raphson method. It returns only one zero point, even if there are multiple.

- **Parameters:**
  - `xs`: A list of coefficients for the polynomial. The list should have an even number of coefficients and the largest non-zero coefficient to guarantee a solution.

- **Returns:** A zero of the polynomial.

- **Example Usage:**
  ```python
  >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
  -0.5
  >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
  1.0
  ```

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Installing Dependencies

This software does not have any external dependencies, so you do not need to install any additional packages.

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change into the directory where the code is located:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code:**

   You can run the code using Python. Open a terminal and execute the following command:

   ```bash
   python main.py
   ```

   This will evaluate the example polynomials and print the results.

## Documentation

For further documentation and detailed examples, please refer to the comments within the code. The code is designed to be self-explanatory with inline comments explaining each function and its usage.

```

This manual provides a comprehensive guide on how to use the polynomial solver software, including the main functions, installation instructions, and usage examples.