'''
This module contains the implementation of the count_nums function which
calculates the number of elements in an array of integers where the sum of
the digits is greater than zero.
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
    def digit_sum(n):
        # Convert number to string to iterate over digits
        s = str(n)
        # Calculate the sum of digits, considering the sign of the first digit
        if n < 0:
            return -int(s[1]) + sum(int(char) for char in s[2:])
        else:
            return sum(int(char) for char in s)
    # Count numbers with digit sum > 0
    return sum(1 for num in arr if digit_sum(num) > 0)