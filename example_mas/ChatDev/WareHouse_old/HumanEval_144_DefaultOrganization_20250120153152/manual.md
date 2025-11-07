# Simplify Function User Manual

Welcome to the user manual for the `simplify` function. This software is designed to evaluate whether the product of two fractions results in a whole number. This document will guide you through the installation process, introduce the main functionality of the software, and provide instructions on how to use it.

## Quick Install

To use the `simplify` function, you need to have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

Once Python is installed, you can run the script directly as there are no additional dependencies required for this function.

## 🤔 What is this?

The `simplify` function is a utility that checks if the product of two fractions, provided as strings, results in a whole number. This can be particularly useful in mathematical computations where simplification of fractions is required.

### Main Functionality

- **Fraction Multiplication and Simplification**: The function takes two fractions in string format, multiplies them, and checks if the result is a whole number.

### Example Usage

The function is defined as follows:

```python
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.
    You can assume that x, and n are valid fractions, and do not have zero as denominator.
    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    # Parse the fractions
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    # Multiply the fractions
    numerator = num1 * num2
    denominator = denom1 * denom2
    # Check if the result is a whole number
    return numerator % denominator == 0
```

### How to Use

1. **Input**: Provide two fractions as strings in the format `<numerator>/<denominator>`.
   
2. **Output**: The function returns `True` if the product of the two fractions is a whole number, and `False` otherwise.

3. **Example**:
   - `simplify("1/5", "5/1")` returns `True` because the product is 1, which is a whole number.
   - `simplify("1/6", "2/1")` returns `False` because the product is 1/3, which is not a whole number.
   - `simplify("7/10", "10/2")` returns `False` because the product is 7/2, which is not a whole number.

## 📖 Documentation

For further information and updates, please refer to the official documentation or contact our support team. This function is designed to be simple and efficient, ensuring quick and accurate results for fraction multiplication and simplification tasks.