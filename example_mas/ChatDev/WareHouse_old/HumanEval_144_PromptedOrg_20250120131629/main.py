'''
This module contains the implementation of the simplify function, which checks if the product of two fractions results in a whole number.
'''
def parse_fraction(fraction):
    '''
    Parses a fraction string into a tuple of integers (numerator, denominator).
    :param fraction: A string representing a fraction in the form 'numerator/denominator'.
    :return: A tuple (numerator, denominator).
    '''
    numerator, denominator = map(int, fraction.split('/'))
    return numerator, denominator
def simplify(x, n):
    '''
    Determines if the product of two fractions x and n is a whole number.
    :param x: A string representing a fraction in the form 'numerator/denominator'.
    :param n: A string representing a fraction in the form 'numerator/denominator'.
    :return: True if the product x * n is a whole number, False otherwise.
    '''
    # Parse the fractions
    num1, denom1 = parse_fraction(x)
    num2, denom2 = parse_fraction(n)
    # Multiply the fractions
    product_numerator = num1 * num2
    product_denominator = denom1 * denom2
    # Check if the product is a whole number
    return product_numerator % product_denominator == 0
# Example usage:
# print(simplify("1/5", "5/1"))  # True
# print(simplify("1/6", "2/1"))  # False
# print(simplify("7/10", "10/2"))  # False