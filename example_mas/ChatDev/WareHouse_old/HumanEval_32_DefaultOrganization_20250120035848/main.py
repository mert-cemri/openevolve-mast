'''
This module provides functions to evaluate a polynomial at a given point and to find a zero of the polynomial using the Newton-Raphson method.
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
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Using the Newton-Raphson method to find a root
    def derivative(xs, x):
        """Calculate the derivative of the polynomial at x."""
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
    x0 = 0  # Initial guess
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
# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # Should print -0.5
    print(round(find_zero([-6, 11, -6, 1]), 2))  # Should print 1.0