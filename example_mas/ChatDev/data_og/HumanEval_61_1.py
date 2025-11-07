'''
This module contains a function to check if a string of brackets is correctly matched.
'''
def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # Initialize a counter for open brackets
    open_count = 0
    # Iterate over each character in the string
    for char in brackets:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
        # If at any point the count of closing brackets exceeds opening, return False
        if open_count < 0:
            return False
    # If all open brackets are closed, return True, otherwise False
    return open_count == 0