'''
This module contains a function to calculate the number of even and odd integer palindromes
within a given range from 1 to n.
'''
def is_palindrome(num):
    """
    Check if a given number is a palindrome.
    :param num: Integer to check
    :return: True if num is a palindrome, False otherwise
    """
    return str(num) == str(num)[::-1]
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    :param n: A positive integer
    :return: A tuple (even_count, odd_count)
    """
    even_count = 0
    odd_count = 0
    for num in range(1, n + 1):
        if is_palindrome(num):
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)