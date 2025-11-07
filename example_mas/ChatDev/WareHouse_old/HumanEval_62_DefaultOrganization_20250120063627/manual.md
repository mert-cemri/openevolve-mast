manual.md

```
# Polynomial Derivative Calculator

This software provides a simple function to compute the derivative of a polynomial given its coefficients. It is designed to be lightweight and efficient, requiring no external dependencies.

## Quick Install

No installation of external packages is required as this software does not depend on any third-party libraries. Simply ensure you have Python installed on your system.

## 🤔 What is this?

This software is a Python module that calculates the derivative of a polynomial. Given a list of coefficients, it returns a new list representing the coefficients of the derivative of the polynomial. This is useful in mathematical computations where derivatives are needed.

### Main Function

- **derivative(xs: list) -> list**: This function takes a list of coefficients as input, where each element at index `i` represents the coefficient for the term `x^i` in the polynomial. It returns a list of coefficients for the derivative of the polynomial.

  **Examples:**

  - `derivative([3, 1, 2, 4, 5])` returns `[1, 4, 12, 20]`
  - `derivative([1, 2, 3])` returns `[2, 6]`

## 📖 How to Use

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Python file**: Copy the provided code into a Python file, for example, `main.py`.

3. **Run the function**: You can call the `derivative` function by importing it into your Python script or directly in the Python interactive shell.

   ```python
   from main import derivative

   # Example usage
   result = derivative([3, 1, 2, 4, 5])
   print(result)  # Output: [1, 4, 12, 20]
   ```

4. **Test the function**: You can test the function using the examples provided in the docstring to ensure it works as expected.

## Additional Information

- **No external dependencies**: This software does not require any additional Python packages, making it easy to integrate into existing projects.

- **Lightweight and efficient**: The function is designed to be efficient, operating in linear time relative to the number of coefficients.

For any further questions or support, please contact our support team.
```