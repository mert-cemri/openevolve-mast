'''
xs represent coefficients of a polynomial.
xs[0] + xs[1] * x + xs[2] * x^2 + ....
Return derivative of this polynomial in the same form.
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
'''
def derivative(xs: list) -> list:
    # The derivative of a constant term is 0, so we skip xs[0].
    # For each term xs[i] * x^i, the derivative is i * xs[i] * x^(i-1).
    return [i * xs[i] for i in range(1, len(xs))]