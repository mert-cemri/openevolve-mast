'''
This module contains a function to compute the derivative of a polynomial
given its coefficients.
'''
def derivative(xs: list):
    """ 
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    >>> derivative([5])
    []
    """
    # If the polynomial is a constant, its derivative is an empty list
    if len(xs) <= 1:
        return []
    # The derivative of a constant term (xs[0]) is zero, so we start from xs[1]
    return [i * xs[i] for i in range(1, len(xs))]