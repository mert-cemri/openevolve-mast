'''
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
'''
from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    def max_nesting_level(paren_group: str) -> int:
        max_level = 0
        current_level = 0
        for char in paren_group:
            if char == '(':
                current_level += 1
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                current_level -= 1
        return max_level
    groups = paren_string.split()
    return [max_nesting_level(group) for group in groups]
# Example usage
if __name__ == "__main__":
    example_input = '(()()) ((())) () ((())()())'
    print(parse_nested_parens(example_input))  # Output: [2, 3, 1, 3]