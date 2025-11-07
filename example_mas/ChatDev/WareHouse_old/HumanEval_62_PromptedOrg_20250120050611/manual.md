manual.md

```
# Polynomial Derivative Calculator

This software provides a simple function to compute the derivative of a polynomial given its coefficients. The function is implemented in Python and is designed to be easy to use for anyone familiar with basic programming concepts.

## Quick Install

This software does not require any external dependencies, so you can run it with a standard Python installation. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## 🤔 What is this?

The Polynomial Derivative Calculator is a small utility that calculates the derivative of a polynomial. The polynomial is represented by a list of coefficients, where each element in the list corresponds to the coefficient of a term in the polynomial. For example, the list `[3, 1, 2, 4, 5]` represents the polynomial \(3 + 1x + 2x^2 + 4x^3 + 5x^4\).

The function `derivative(xs: list)` returns a new list of coefficients representing the derivative of the input polynomial. The derivative of a polynomial is calculated by multiplying each coefficient by its corresponding power of x and reducing the power by one.

## Main Function

### `derivative(xs: list)`

- **Input:** A list of coefficients `xs` representing a polynomial.
- **Output:** A list of coefficients representing the derivative of the polynomial.

#### Example Usage

```python
# Import the derivative function
from main import derivative

# Calculate the derivative of a polynomial
result = derivative([3, 1, 2, 4, 5])
print(result)  # Output: [1, 4, 12, 20]

result = derivative([1, 2, 3])
print(result)  # Output: [2, 6]
```

## How to Use

1. **Clone the Repository:** Download or clone the repository to your local machine.

2. **Navigate to the Directory:** Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code:** You can run the code by importing the `derivative` function in your Python script or interactive session and passing a list of coefficients to it.

4. **View Results:** The function will return a list of coefficients representing the derivative of the polynomial.

## Documentation

For further information on how to use the function, refer to the docstring provided in the `main.py` file. The docstring includes examples and a brief explanation of the function's behavior.

```