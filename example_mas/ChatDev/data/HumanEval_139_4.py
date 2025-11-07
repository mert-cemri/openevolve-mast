'''
The function special_factorial computes the Brazilian factorial of a given integer n.
The Brazilian factorial is defined as the product of all factorials from n! down to 1!.
'''
import math
def special_factorial(n):
    """Calculate the Brazilian factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result
# Example usage:
# print(special_factorial(4))  # Output: 288