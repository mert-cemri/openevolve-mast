'''
This module contains a function to evaluate whether a given number can be written as the sum of exactly four positive even numbers.
'''
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers.
    Args:
    n (int): The number to evaluate.
    Returns:
    bool: True if n can be expressed as the sum of four positive even numbers, False otherwise.
    Example:
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # The smallest sum of four positive even numbers is 8 (2 + 2 + 2 + 2).
    # Therefore, any number less than 8 cannot be expressed as such a sum.
    # Additionally, the number must be even to be expressed as a sum of even numbers.
    return n >= 8 and n % 2 == 0