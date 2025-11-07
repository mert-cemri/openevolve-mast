'''
This module contains functions to evaluate a polynomial and find its zero using Newton's method.
'''
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def derivative(xs: list, x: float):
    """
    Evaluates the derivative of a polynomial with coefficients xs at point x.
    return xs[1] + 2 * xs[2] * x + .... n * xs[n] * x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
def find_zero(xs: list, initial_guess: float = 0.0, tolerance: float = 1e-7, max_iterations: int = 1000):
    """
    Finds a zero of the polynomial with coefficients xs using Newton's method.
    Assumes the polynomial has a real root and the initial guess is important for convergence.
    Returns one zero point, even if there are many, or raises an error if no solution is found.
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    if max(xs) == 0:
        raise ValueError("The list of coefficients must have a largest non-zero coefficient.")
    x = initial_guess
    for _ in range(max_iterations):
        fx = poly(xs, x)
        f_prime_x = derivative(xs, x)
        if abs(fx) < tolerance:
            return x
        if f_prime_x == 0:
            raise ValueError("Derivative is zero. Try a different initial guess.")
        x -= fx / f_prime_x
    raise ValueError("No solution found after maximum iterations.")