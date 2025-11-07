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
    # Convert the text to lowercase to ensure case-insensitivity
    text = text.lower()
    # Compare the text with its reverse
    return text == text[::-1]