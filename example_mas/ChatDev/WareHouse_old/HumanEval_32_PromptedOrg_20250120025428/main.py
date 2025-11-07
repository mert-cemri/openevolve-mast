'''
This module contains functions to evaluate a polynomial and find its root using the Newton-Raphson method.
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
    return xs[1] + 2 * xs[2] * x + .... n * xs[n] * x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
def find_zero(xs: list):
    """ 
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients
    and the largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Initial guess
    x = 0.0
    # Tolerance level
    tolerance = 1e-7
    # Maximum number of iterations
    max_iterations = 1000
    for _ in range(max_iterations):
        fx = poly(xs, x)
        if abs(fx) < tolerance:
            return x
        dfx = derivative(xs, x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x -= fx / dfx
    raise ValueError("Exceeded maximum iterations. No solution found.")