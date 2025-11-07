'''
Given a list of positive integers x, return a sorted list of all 
elements that haven't any even digit.
Note: Returned list should be sorted in increasing order.
For example:
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
'''
def unique_digits(x):
    def has_even_digit(n):
        """Check if the number has any even digit."""
        return any(digit in '02468' for digit in str(n))
    # Filter out numbers with even digits and sort the result
    result = sorted(num for num in x if not has_even_digit(num))
    return result