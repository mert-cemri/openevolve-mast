'''
This module contains the fix_spaces function which replaces spaces in a string
according to specific rules: single spaces are replaced with underscores, and
sequences of more than two spaces are replaced with a hyphen.
'''
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with a hyphen.
    Examples:
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = []
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
        else:
            if space_count == 1:
                result.append('_')
            elif space_count > 2:
                result.append('-')
            elif space_count == 2:
                result.extend(['_', '_'])
            result.append(char)
            space_count = 0
    # Handle trailing spaces
    if space_count == 1:
        result.append('_')
    elif space_count > 2:
        result.append('-')
    elif space_count == 2:
        result.extend(['_', '_'])
    return ''.join(result)
# Example usage
if __name__ == "__main__":
    print(fix_spaces("Example"))         # Output: "Example"
    print(fix_spaces("Example 1"))       # Output: "Example_1"
    print(fix_spaces(" Example 2"))      # Output: "_Example_2"
    print(fix_spaces(" Example   3"))    # Output: "_Example-3"