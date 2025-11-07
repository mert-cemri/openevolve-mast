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
def check_if_last_char_is_a_letter(txt):
    # Remove trailing spaces
    txt = txt.rstrip()
    # Check if the string is empty after stripping
    if not txt:
        return False
    # Split the string into words
    words = txt.split()
    # Check if there are no words
    if not words:
        return False
    # Get the last word
    last_word = words[-1]
    # Check if the last character of the last word is a letter
    if last_word[-1].isalpha() and len(last_word) == 1:
        return True
    else:
        return False