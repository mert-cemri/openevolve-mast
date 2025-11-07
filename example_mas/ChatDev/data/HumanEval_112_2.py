'''
This module contains the implementation of the reverse_delete function.
The function removes characters from a string and checks if the result is a palindrome.
'''
def reverse_delete(s, c):
    """
    Remove all characters from s that are present in c, then check if the result is a palindrome.
    Parameters:
    s (str): The original string.
    c (str): The string containing characters to be removed from s.
    Returns:
    tuple: A tuple containing the resulting string and a boolean indicating if it is a palindrome.
    Example:
    reverse_delete("abcde", "ae") -> ('bcd', False)
    reverse_delete("abcdef", "b") -> ('acdef', False)
    reverse_delete("abcdedcba", "ab") -> ('cdedc', True)
    """
    # Remove characters from s that are in c
    filtered_string = ''.join(char for char in s if char not in c)
    # Check if the filtered string is a palindrome
    is_palindrome = filtered_string == filtered_string[::-1]
    # Return the result as a tuple
    return (filtered_string, is_palindrome)