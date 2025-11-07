'''
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
'''
from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the input string into groups
    groups = paren_string.split()
    # List to store the maximum nesting level for each group
    max_nesting_levels = []
    # Iterate over each group
    for group in groups:
        current_level = 0
        max_level = 0
        # Iterate over each character in the group
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        # Append the maximum level for this group to the result list
        max_nesting_levels.append(max_level)
    return max_nesting_levels