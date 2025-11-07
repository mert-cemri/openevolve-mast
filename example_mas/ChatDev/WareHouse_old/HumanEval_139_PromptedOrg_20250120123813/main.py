'''
This module contains the implementation of the special_factorial function,
which calculates the Brazilian factorial of a given integer.
'''
def factorial(x):
    """Calculate the factorial of a number x."""
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    For example:
    >>> special_factorial(4)
    288
    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    special_fact = 1
    for i in range(1, n + 1):
        special_fact *= factorial(i)
    return special_fact
# Example usage:
# print(special_factorial(4))  # Output should be 288