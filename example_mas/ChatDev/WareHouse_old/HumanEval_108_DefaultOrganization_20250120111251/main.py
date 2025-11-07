'''
This module contains the function count_nums which calculates the number of integers
in a list that have a sum of digits greater than zero.
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
        # Initialize sum
        total = 0
        # Convert number to string of its absolute value to iterate over digits
        s = str(abs(n))
        # Apply the sign to the first digit
        sign = -1 if n < 0 else 1
        # Add the first digit with its sign
        total += sign * int(s[0])
        # Iterate over each character in the string except the first
        for char in s[1:]:
            total += int(char)
        return total
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count