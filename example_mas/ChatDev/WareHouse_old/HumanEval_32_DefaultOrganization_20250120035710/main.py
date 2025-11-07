'''
This module contains functions to evaluate a polynomial at a given point and to find a zero of the polynomial using the bisection method.
'''
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    """ 
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(xs, x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    Uses the bisection method to find a root.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    def f(x):
        return poly(xs, x)
    # Initial guesses
    a, b = -1000, 1000
    tol = 1e-7
    max_iter = 1000
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("Root not found within the given interval")
# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # Expected output: -0.5
    print(round(find_zero([-6, 11, -6, 1]), 2))  # Expected output: 1.0