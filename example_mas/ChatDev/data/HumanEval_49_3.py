'''
Return 2^n modulo p (be aware of numerics).
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
'''
def modp(n: int, p: int):
    result = 1
    base = 2 % p  # Initial base is 2, reduced by modulo p
    while n > 0:
        if n % 2 == 1:  # If n is odd, multiply the base with result
            result = (result * base) % p
        base = (base * base) % p  # Square the base
        n //= 2  # Divide n by 2
    return result