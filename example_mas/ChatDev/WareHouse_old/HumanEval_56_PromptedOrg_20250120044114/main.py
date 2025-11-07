'''
This module contains a function to check if a string of brackets is correctly matched.
'''
def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # Initialize a counter for unmatched opening brackets
    open_brackets = 0
    # Iterate through each character in the string
    for char in brackets:
        if char == "<":
            open_brackets += 1
        elif char == ">":
            if open_brackets > 0:
                open_brackets -= 1
            else:
                return False
    # If all opening brackets are matched, return True
    return open_brackets == 0