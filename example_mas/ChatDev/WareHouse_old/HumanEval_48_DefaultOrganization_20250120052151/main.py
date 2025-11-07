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
    # A string is a palindrome if it is equal to its reverse
    return text == text[::-1]