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
    def has_even_digit(number):
        """Check if the number contains any even digit."""
        for digit in str(number):
            if digit in '02468':
                return True
        return False
    # Filter numbers that do not have any even digits
    result = [num for num in x if not has_even_digit(num)]
    # Return the sorted result
    return sorted(result)