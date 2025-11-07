'''
The Brazilian factorial is defined as:
brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
where n > 0
For example:
>>> special_factorial(4)
288
The function will receive an integer as input and should return the special
factorial of this integer.
'''
def factorial(x):
    """Calculate the factorial of a given number x."""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
def special_factorial(n):
    """Calculate the Brazilian factorial of a given number n."""
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result
# Example usage:
# print(special_factorial(4))  # Output should be 288