'''
This module contains the implementation of the count_nums function, which
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
        # Convert number to string to handle each digit
        digits = str(n)
        # Initialize sum
        total = 0
        # Iterate over each character in the string
        for i, char in enumerate(digits):
            # If it's the first character and the number is negative, skip the '-' sign
            if i == 0 and char == '-':
                continue
            # Convert character to integer
            digit = int(char)
            # If it's the first digit of a negative number, make it negative
            if i == 1 and digits[0] == '-':
                digit = -digit
            total += digit
        return total
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count