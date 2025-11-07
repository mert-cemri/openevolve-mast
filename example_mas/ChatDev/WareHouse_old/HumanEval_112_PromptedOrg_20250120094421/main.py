'''
This module contains the implementation of the reverse_delete function which removes specified characters from a string and checks if the resulting string is a palindrome.
'''
def reverse_delete(s, c):
    """Remove all characters from s that are present in c and check if the result is a palindrome.
    Args:
        s (str): The original string.
        c (str): The string containing characters to be removed from s.
    Returns:
        tuple: A tuple containing the resulting string and a boolean indicating if it is a palindrome.
    """
    # Remove characters from s that are present in c
    result = ''.join([char for char in s if char not in c])
    # Check if the resulting string is a palindrome
    is_palindrome = result == result[::-1]
    # Return the result string and the palindrome check
    return (result, is_palindrome)