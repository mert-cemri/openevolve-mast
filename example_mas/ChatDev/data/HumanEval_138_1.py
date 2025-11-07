'''
Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers.
Example:
is_equal_to_sum_even(4) == False
is_equal_to_sum_even(6) == False
is_equal_to_sum_even(8) == True
'''
def is_equal_to_sum_even(n):
    # The smallest sum of four positive even numbers is 8 (2 + 2 + 2 + 2)
    # Therefore, n must be at least 8 and even to be expressed as the sum of four positive even numbers.
    return n >= 8 and n % 2 == 0