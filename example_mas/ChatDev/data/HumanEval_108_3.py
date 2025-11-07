'''
This module contains the implementation of the count_nums function which
counts the number of integers in an array whose sum of digits is greater than 0.
'''
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def sum_of_digits(n):
        # Convert number to string to iterate over digits
        str_n = str(n)
        # Initialize sum of digits
        total = 0
        # Check if the number is negative
        if str_n[0] == '-':
            # Add the first digit as negative
            total += int(str_n[0:2])
            # Start from the third character
            str_n = str_n[2:]
        # Add the rest of the digits
        for char in str_n:
            total += int(char)
        return total
    # Count numbers with sum of digits > 0
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count