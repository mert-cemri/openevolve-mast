'''
This module contains a function to separate groups of nested parentheses from a string.
The function `separate_paren_groups` takes a string with multiple groups of nested parentheses
and returns a list of separate strings, each representing a balanced group of parentheses.
Spaces in the input string are ignored.
Example:
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
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
    result = []
    current_group = []
    balance = 0
    for char in paren_string:
        if char == ' ':
            continue
        current_group.append(char)
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0 and current_group:
            result.append(''.join(current_group))
            current_group = []
    return result