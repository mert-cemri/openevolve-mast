'''
This module contains a function to separate groups of balanced parentheses from a string.
'''
from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    # Initialize variables
    groups = []
    current_group = ""
    balance = 0
    # Iterate through the string
    for char in paren_string:
        current_group += char
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        # When balance is zero, we have a complete group
        if balance == 0 and current_group:
            groups.append(current_group)
            current_group = ""
    return groups