'''
This function checks if the last character of a given string is an alphabetical character
and is not part of a word. A "word" is defined as a group of characters separated by space.
Examples:
check_if_last_char_is_a_letter("apple pie") ➞ False
check_if_last_char_is_a_letter("apple pi e") ➞ True
check_if_last_char_is_a_letter("apple pi e ") ➞ False
check_if_last_char_is_a_letter("") ➞ False
'''
def check_if_last_char_is_a_letter(txt):
    # Strip trailing spaces
    txt = txt.rstrip()
    # Check if the string is empty after stripping
    if not txt:
        return False
    # Check if the last character is an alphabetical character
    if txt[-1].isalpha():
        # Check if it is not part of a word
        if len(txt) == 1 or txt[-2] == ' ':
            return True
    return False