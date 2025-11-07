'''
DOCSTRING
This module contains a function to compute the derivative of a polynomial given its coefficients.
'''
def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to store the derivative coefficients
    derivative_coeffs = []
    # Iterate over the coefficients starting from the first power (index 1)
    for power, coeff in enumerate(xs):
        if power == 0:
            continue  # Skip the constant term as its derivative is zero
        # Calculate the derivative for the current term and append to the list
        derivative_coeffs.append(power * coeff)
    return derivative_coeffs
# Example usage
if __name__ == "__main__":
    print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))        # Output: [2, 6]