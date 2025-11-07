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
    def sum_of_digits(n):
        # Convert number to string to iterate over each digit
        s = str(n)
        total = 0
        # Iterate over each character in the string
        for i, char in enumerate(s):
            if char == '-':
                continue
            digit = int(char)
            # If the number is negative, the first digit should be negative
            if i == 0 and s[0] == '-':
                digit = -digit
            total += digit
        return total
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count