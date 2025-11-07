'''
This function checks if a number x is a simple power of n.
A number x is a simple power of n if there exists an integer k such that n**k = x.
'''
def is_simple_power(x, n):
    # Edge case: if x is 1, it is a simple power of any n
    if x == 1:
        return True
    # Edge case: if n is 1, only x = 1 can be a simple power of n
    if n == 1:
        return x == 1
    # Check if x can be reduced to 1 by dividing by n
    while x % n == 0:
        x //= n
    # If x is reduced to 1, it is a simple power of n
    return x == 1