'''
This module contains the implementation of the special_factorial function,
which calculates the Brazilian factorial of a given integer.
'''
def factorial(x):
    """Calculate the factorial of a given number x."""
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
def special_factorial(n):
    """Calculate the Brazilian factorial of a given number n."""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result
# Example usage:
# print(special_factorial(4))  # Output: 288