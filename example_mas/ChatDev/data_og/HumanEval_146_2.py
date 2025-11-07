'''
This module contains the implementation of the specialFilter function, which filters numbers based on specific criteria.
'''
def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def is_odd_digit(digit):
        """Check if a digit is odd."""
        return digit in {1, 3, 5, 7, 9}
    def first_and_last_digits(n):
        """Extract the first and last digits of a number."""
        n = abs(n)  # Work with positive numbers for simplicity
        digits = str(n)
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        return first_digit, last_digit
    count = 0
    for num in nums:
        if num > 10:
            first_digit, last_digit = first_and_last_digits(num)
            if is_odd_digit(first_digit) and is_odd_digit(last_digit):
                count += 1
    return count