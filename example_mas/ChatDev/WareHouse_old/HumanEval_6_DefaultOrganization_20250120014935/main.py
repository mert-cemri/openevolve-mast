'''
This module contains a function to parse nested parentheses and determine the maximum depth of nesting for each group.
'''
from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(paren_group: str) -> int:
        depth = 0
        max_depth = 0
        for char in paren_group:
            if char == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif char == ')':
                depth -= 1
        return max_depth
    groups = paren_string.split()
    return [max_depth(group) for group in groups]