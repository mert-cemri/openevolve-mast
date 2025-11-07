'''
This module contains the implementation of the reverse_delete function.
The function removes characters from a string and checks if the result is a palindrome.
'''
def reverse_delete(s, c):
    """
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example:
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b", the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """
    # Remove characters from s that are in c
    result = ''.join([char for char in s if char not in c])
    # Check if the result is a palindrome
    is_palindrome = result == result[::-1]
    return (result, is_palindrome)
# Example usage
if __name__ == "__main__":
    print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
    print(reverse_delete("abcdef", "b"))  # Output: ('acdef', False)
    print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)