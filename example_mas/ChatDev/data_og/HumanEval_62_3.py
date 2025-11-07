'''
DOCSTRING
This module contains a function to compute the derivative of a polynomial given its coefficients.
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
    """
    # The derivative of a constant term (xs[0]) is 0, so we start from the first degree term.
    return [i * xs[i] for i in range(1, len(xs))]
# Example usage
if __name__ == "__main__":
    print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))        # Output: [2, 6]