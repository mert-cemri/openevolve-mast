'''
 xs represent coefficients of a polynomial.
 xs[0] + xs[1] * x + xs[2] * x^2 + ....
 Return derivative of this polynomial in the same form.
 >>> derivative([3, 1, 2, 4, 5])
 [1, 4, 12, 20]
 >>> derivative([1, 2, 3])
 [2, 6]
'''
def derivative(xs: list):
    # Initialize an empty list to store the derivative coefficients
    derivative_coeffs = []
    # Iterate over the coefficients starting from the first degree term
    for i in range(1, len(xs)):
        # Calculate the derivative coefficient for the current term
        derivative_coeffs.append(xs[i] * i)
    return derivative_coeffs