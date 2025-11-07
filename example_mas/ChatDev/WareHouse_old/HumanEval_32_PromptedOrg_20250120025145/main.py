'''
This module contains functions to evaluate a polynomial and find its root using the Newton-Raphson method.
'''
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def poly_derivative(xs: list, x: float) -> float:
    """
    Evaluates the derivative of a polynomial with coefficients xs at point x.
    return xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + .... n * xs[n] * x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
def find_zero(xs: list) -> float:
    """
    Finds a root of the polynomial with coefficients xs using the Newton-Raphson method.
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    """
    # Initial guess
    x = 0.0
    # Tolerance level
    tolerance = 1e-7
    # Maximum number of iterations
    max_iterations = 1000
    for _ in range(max_iterations):
        # Evaluate the polynomial and its derivative at the current guess
        fx = poly(xs, x)
        f_prime_x = poly_derivative(xs, x)
        # Check if the derivative is zero to avoid division by zero
        if f_prime_x == 0:
            raise ValueError("Derivative is zero. No solution found.")
        # Update the guess using the Newton-Raphson formula
        x_new = x - fx / f_prime_x
        # Check for convergence
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Exceeded maximum iterations. No solution found.")