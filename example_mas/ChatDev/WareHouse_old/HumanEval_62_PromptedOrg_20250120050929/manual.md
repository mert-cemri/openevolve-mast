# Polynomial Derivative Calculator

This software module provides a simple function to compute the derivative of a polynomial given its coefficients. The derivative is returned in the same form as the input, which is a list of coefficients.

## Main Functionality

The main function of this software is:

- **derivative(xs: list):** This function takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of that polynomial.

### Example Usage

Given a polynomial represented by its coefficients, such as:

- `3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4`

The function `derivative([3, 1, 2, 4, 5])` will return `[1, 4, 12, 20]`, which corresponds to the derivative:

- `1 + 4*x + 12*x^2 + 20*x^3`

## Installation

This software does not require any external dependencies. It is implemented in pure Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

Clone the repository or download the `main.py` file to your local machine.

## How to Use

1. **Open a Terminal or Command Prompt:**

   Navigate to the directory where `main.py` is located.

2. **Run the Script:**

   You can execute the script directly using Python. For example:

   ```bash
   python main.py
   ```

   This will run the example usage provided in the script, displaying the output of the derivative function.

3. **Modify for Custom Input:**

   To compute the derivative of a different polynomial, modify the list passed to the `derivative` function in the `main.py` file. For example, to compute the derivative of `1 + 2*x + 3*x^2`, change the function call to:

   ```python
   print(derivative([1, 2, 3]))
   ```

   Then run the script again to see the result.

## Documentation

The function is documented with a docstring that explains its purpose and provides example usage. For further understanding, you can refer to the comments within the code for a step-by-step explanation of how the derivative is calculated.

This module is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone tool for polynomial derivative calculations.