'''
This module contains the implementation of the reverse_delete function, which removes specified characters from a string and checks if the result is a palindrome.
'''
def reverse_delete(s, c):
    """
    Removes all characters from string s that are present in string c,
    then checks if the resulting string is a palindrome.
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
    # Remove characters in c from s
    result = ''.join(char for char in s if char not in c)
    # Check if the result is a palindrome
    is_palindrome = result == result[::-1]
    return (result, is_palindrome)
# Example usage
if __name__ == "__main__":
    print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
    print(reverse_delete("abcdef", "b"))  # Output: ('acdef', False)
    print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)