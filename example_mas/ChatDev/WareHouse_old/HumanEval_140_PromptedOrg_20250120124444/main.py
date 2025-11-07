'''
This module contains the function fix_spaces which processes a string to replace spaces with underscores and more than two consecutive spaces with a hyphen.
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
    import re
    # Replace more than two consecutive spaces with a hyphen
    text = re.sub(r'\s{3,}', '-', text)
    # Replace remaining spaces with underscores
    text = text.replace(' ', '_')
    return text