'''
Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers.
Args:
n (int): The number to evaluate.
Returns:
bool: True if n can be expressed as the sum of four positive even numbers, False otherwise.
Example:
is_equal_to_sum_even(4) == False
is_equal_to_sum_even(6) == False
is_equal_to_sum_even(8) == True
'''
def is_equal_to_sum_even(n):
    # The smallest sum of four positive even numbers is 2 + 2 + 2 + 2 = 8
    # Therefore, n must be at least 8 and even to be expressible as such a sum.
    return n >= 8 and n % 2 == 0