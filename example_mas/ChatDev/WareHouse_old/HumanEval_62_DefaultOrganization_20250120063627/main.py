'''
This module contains a function to compute the derivative of a polynomial
given its coefficients.
Function:
    derivative(xs: list) -> list: Computes the derivative of a polynomial.
'''
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.
    Parameters:
    xs (list): A list of coefficients where xs[i] is the coefficient for x^i.
    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a constant term (xs[0]) is 0, so we start from index 1
    return [i * xs[i] for i in range(1, len(xs))]