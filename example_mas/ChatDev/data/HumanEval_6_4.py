'''
This module contains a function to parse nested parentheses and determine the deepest level of nesting for each group of parentheses.
'''
from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into separate groups of parentheses
    groups = paren_string.split()
    # List to store the maximum nesting level for each group
    max_nesting_levels = []
    # Iterate over each group of parentheses
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
        # Append the maximum level for this group to the result list
        max_nesting_levels.append(max_level)
    return max_nesting_levels