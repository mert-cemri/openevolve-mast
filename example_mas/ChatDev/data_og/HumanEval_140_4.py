'''
Given a string text, replace all spaces in it with underscores,
and if a string has more than 2 consecutive spaces,
then replace all consecutive spaces with a hyphen.
fix_spaces("Example") == "Example"
fix_spaces("Example 1") == "Example_1"
fix_spaces(" Example 2") == "_Example_2"
fix_spaces(" Example   3") == "_Example-3"
'''
def fix_spaces(text):
    import re
    # Replace more than two consecutive spaces with a hyphen
    text = re.sub(r' {3,}', '-', text)
    # Replace single spaces with underscores
    text = text.replace(' ', '_')
    return text
# Example usage
if __name__ == "__main__":
    print(fix_spaces("Example"))          # Output: "Example"
    print(fix_spaces("Example 1"))        # Output: "Example_1"
    print(fix_spaces(" Example 2"))       # Output: "_Example_2"
    print(fix_spaces(" Example   3"))     # Output: "_Example-3"