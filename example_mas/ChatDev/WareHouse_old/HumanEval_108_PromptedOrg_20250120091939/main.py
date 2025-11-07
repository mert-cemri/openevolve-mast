'''
This module contains the implementation of the count_nums function which
counts the number of integers in an array whose sum of digits is greater than zero.
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
    count = 0
    for num in arr:
        # Calculate the sum of digits considering the sign
        digit_sum = sum(int(d) for d in str(abs(num)))
        # Adjust for the sign of the number
        if num < 0:
            digit_sum -= 2 * int(str(abs(num))[0])
        # Check if the sum of digits is greater than zero
        if digit_sum > 0:
            count += 1
    return count