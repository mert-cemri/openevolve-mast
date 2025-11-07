'''
This module contains the implementation of the unique_digits function.
'''
def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all 
    elements that haven't any even digit.
    Note: Returned list should be sorted in increasing order.
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []
    for number in x:
        # Convert number to string to check each digit
        str_num = str(number)
        # Check if any digit in the number is even
        if all(digit not in '02468' for digit in str_num):
            result.append(number)
    # Return the sorted result list
    return sorted(result)