'''
This module contains functions to evaluate a polynomial and find its zero.
'''
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list) -> float:
    """
    Finds a zero of the polynomial defined by coefficients xs.
    Uses the bisection method for simplicity and robustness.
    Assumes the polynomial has at least one real root.
    """
    def bisection_method(a, b, tol=1e-7):
        if poly(xs, a) * poly(xs, b) >= 0:
            raise ValueError("Bisection method requires a sign change over the interval.")
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0
            if poly(xs, midpoint) == 0:
                return midpoint
            elif poly(xs, a) * poly(xs, midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return (a + b) / 2.0
    # Dynamically expand the interval until a sign change is found
    a, b = -1, 1  # Start with a small interval
    while poly(xs, a) * poly(xs, b) >= 0:
        a *= 2
        b *= 2
        if a < -1e6 or b > 1e6:  # Prevent infinite loop
            raise ValueError("Unable to find a suitable interval for root finding.")
    return bisection_method(a, b)
# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # Example: f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # Example: f(x) = -6 + 11x - 6x^2 + x^3