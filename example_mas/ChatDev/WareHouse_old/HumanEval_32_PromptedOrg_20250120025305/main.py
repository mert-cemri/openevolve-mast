'''
This module provides functions to evaluate a polynomial and find its root using the Newton-Raphson method.
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
    Evaluates the derivative of the polynomial with coefficients xs at point x.
    return xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + .... n * xs[n] * x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
def find_zero(xs: list):
    """
    Finds a root of the polynomial with coefficients xs using the Newton-Raphson method.
    xs are coefficients of a polynomial.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an odd number of coefficients
    and the largest non-zero coefficient as it guarantees a solution.
    """
    if len(xs) % 2 == 0:
        raise ValueError("The list of coefficients must have an odd number of elements.")
    # Initial guess
    x0 = 0.0
    tolerance = 1e-7
    max_iterations = 1000
    for _ in range(max_iterations):
        fx = poly(xs, x0)
        if abs(fx) < tolerance:
            return x0
        dfx = derivative(xs, x0)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x0 = x0 - fx / dfx
    raise ValueError("Exceeded maximum iterations. No solution found.")