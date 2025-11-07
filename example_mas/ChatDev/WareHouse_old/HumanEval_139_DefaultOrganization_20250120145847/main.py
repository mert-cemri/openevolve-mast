'''
The function special_factorial computes the Brazilian factorial of a given integer n.
The Brazilian factorial is defined as the product of factorials from n! to 1!.
'''
def special_factorial(n):
    """Calculate the Brazilian factorial of n."""
    def factorial(x):
        """Helper function to calculate factorial of x."""
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
    brazilian_factorial = 1
    for i in range(1, n + 1):
        brazilian_factorial *= factorial(i)
    return brazilian_factorial
# Example usage:
# print(special_factorial(4))  # Output should be 288