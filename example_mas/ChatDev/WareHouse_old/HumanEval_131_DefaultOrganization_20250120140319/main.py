'''
This module contains the implementation of the function `digits(n)`.
The function calculates the product of the odd digits in a given positive integer `n`.
If all digits are even, it returns 0.
'''
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:  # Check if the digit is odd
            product *= digit
            has_odd = True
        n //= 10
    return product if has_odd else 0