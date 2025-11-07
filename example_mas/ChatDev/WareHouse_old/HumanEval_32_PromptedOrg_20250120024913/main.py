'''
This module contains functions to evaluate polynomials and find their zeros using the Newton-Raphson method.
'''
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def derivative(xs: list) -> list:
    """
    Computes the derivative of a polynomial with coefficients xs.
    """
    return [i * coeff for i, coeff in enumerate(xs)][1:]
def find_zero(xs: list, initial_guess: float = 0.0) -> float:
    """
    Finds a zero of the polynomial with coefficients xs using the Newton-Raphson method.
    Assumes the polynomial has a real root. Allows the user to specify an initial guess.
    """
    # Initial guess
    x = initial_guess
    # Maximum number of iterations
    max_iter = 1000
    # Tolerance for convergence
    tolerance = 1e-7
    # Small threshold to avoid division by a very small number
    derivative_threshold = 1e-10
    for _ in range(max_iter):
        # Evaluate the polynomial and its derivative at x
        fx = poly(xs, x)
        dfx = poly(derivative(xs), x)
        # Check if the derivative is close to zero to avoid division by a very small number
        if abs(dfx) < derivative_threshold:
            raise ValueError("Derivative is too small. Newton-Raphson method fails.")
        # Newton-Raphson iteration
        x_new = x - fx / dfx
        # Check for convergence
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Maximum iterations reached. No solution found. Consider providing a different initial guess.")
# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # Should output -0.5
    print(round(find_zero([-6, 11, -6, 1]), 2))  # Should output 1.0