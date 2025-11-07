'''
Checks if given string is a palindrome
>>> is_palindrome('')
True
>>> is_palindrome('aba')
True
>>> is_palindrome('aaaaa')
True
>>> is_palindrome('zbcd')
False
'''
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    """
    # A string is a palindrome if it reads the same forwards and backwards
    return text == text[::-1]