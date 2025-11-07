'''
This script contains functions to evaluate a polynomial at a given point,
compute its derivative, and find a zero of the polynomial using the Newton-Raphson method.
'''
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def derivative(xs: list):
    """
    Computes the derivative of the polynomial with coefficients xs.
    """
    return [i * coeff for i, coeff in enumerate(xs)][1:]
def find_zero(xs: list, initial_guess=0.0, tolerance=1e-7, max_iterations=1000):
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    """
    x = initial_guess
    for _ in range(max_iterations):
        fx = poly(xs, x)
        if abs(fx) < tolerance:
            return x
        dfx = poly(derivative(xs), x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x -= fx / dfx
    raise ValueError("Exceeded maximum iterations. No solution found.")
# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x, should return -0.5
    print(round(find_zero([-6, 11, -6, 1]), 2))  # f(x) = -6 + 11x - 6x^2 + x^3, should return 1.0