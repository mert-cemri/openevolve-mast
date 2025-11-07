'''
This module contains the function `check_if_last_char_is_a_letter` which checks if the last character of a given string is an alphabetical character and is not part of a word.
'''
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.
    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    # Trim the string to remove trailing spaces
    txt = txt.rstrip()
    # If the string is empty after trimming, return False
    if not txt:
        return False
    # Get the last character
    last_char = txt[-1]
    # Check if the last character is alphabetical
    if last_char.isalpha():
        # Check if the last character is not part of a word
        # This is true if there is a space before it
        if len(txt) > 1 and txt[-2] == ' ':
            return True
    return False