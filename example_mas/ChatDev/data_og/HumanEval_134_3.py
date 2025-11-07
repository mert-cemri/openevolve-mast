'''
This module contains a function to check if the last character of a given string
is an alphabetical character and is not part of a word.
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
    # Remove trailing spaces
    txt = txt.rstrip()
    # Check if the string is empty after trimming
    if not txt:
        return False
    # Get the last character
    last_char = txt[-1]
    # Check if the last character is a letter
    if last_char.isalpha():
        # Check if it is not part of a word
        # It should be preceded by a space or be the only character
        if len(txt) == 1 or txt[-2] == ' ':
            return True
    return False