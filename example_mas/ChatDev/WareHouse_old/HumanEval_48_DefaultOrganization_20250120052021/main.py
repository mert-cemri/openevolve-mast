'''
This module contains a function to check if a given string is a palindrome.
'''
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    A palindrome is a string that reads the same forward and backward.
    Parameters:
    text (str): The string to check.
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # A string is a palindrome if it is equal to its reverse
    return text == text[::-1]