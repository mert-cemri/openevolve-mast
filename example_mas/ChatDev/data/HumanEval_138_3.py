'''
Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers.
A number can be expressed as the sum of four positive even numbers if and only if it is even and
greater than or equal to 8.
Example:
is_equal_to_sum_even(4) == False
is_equal_to_sum_even(6) == False
is_equal_to_sum_even(8) == True
'''
def is_equal_to_sum_even(n):
    # Check if n is even and greater than or equal to 8
    return n >= 8 and n % 2 == 0