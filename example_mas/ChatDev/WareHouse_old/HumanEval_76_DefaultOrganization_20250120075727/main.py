'''
This function checks if a number x is a simple power of n.
A number x is a simple power of n if there exists an integer k such that n**k = x.
'''
def is_simple_power(x, n):
    if x == 1:
        return True
    if n == 1:
        return x == 1
    power = 1
    while power < x:
        power *= n
    return power == x