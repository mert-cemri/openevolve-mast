'''
This module contains a function to calculate the deepest level of nesting of parentheses for each group in a given string.
'''
from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into individual groups of parentheses
    groups = paren_string.split()
    # Initialize a list to store the maximum nesting level for each group
    max_levels = []
    # Iterate over each group
    for group in groups:
        current_level = 0
        max_level = 0
        # Iterate over each character in the group
        for char in group:
            if char == '(':
                current_level += 1
                # Update the maximum level if the current level is greater
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                current_level -= 1
        # Append the maximum level for the current group to the result list
        max_levels.append(max_level)
    return max_levels