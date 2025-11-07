'''
The function special_factorial calculates the Brazilian factorial of a given integer n.
The Brazilian factorial is defined as the product of all factorials from n! to 1!.
'''
def special_factorial(n):
    from math import factorial
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result