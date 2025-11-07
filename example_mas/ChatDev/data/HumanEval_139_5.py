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
def special_factorial(n):
    """Calculate the special factorial of n."""
    def factorial(x):
        """Calculate the factorial of x."""
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
    special_fact = 1
    for i in range(1, n + 1):
        special_fact *= factorial(i)
    return special_fact