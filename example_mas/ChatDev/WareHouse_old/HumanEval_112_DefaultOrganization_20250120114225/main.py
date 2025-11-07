'''
This module contains the implementation of the reverse_delete function.
The function takes two strings, s and c, removes all characters from s that are present in c,
and checks if the resulting string is a palindrome. It returns a tuple containing the resulting
string and a boolean indicating whether it is a palindrome.
'''
def reverse_delete(s, c):
    # Remove characters in s that are present in c
    result = ''.join([char for char in s if char not in c])
    # Check if the resulting string is a palindrome
    is_palindrome = result == result[::-1]
    # Return the result string and the palindrome check
    return (result, is_palindrome)
# Example usage
if __name__ == "__main__":
    print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
    print(reverse_delete("abcdef", "b"))  # Output: ('acdef', False)
    print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)