'''
Regex engine module that handles regex matching.
'''
import re
def match_regex(regex, test_string):
    # Try to compile the provided regex pattern
    try:
        pattern = re.compile(regex)
        # Search for the pattern in the test string
        match = pattern.search(test_string)  # Use search instead of match
        return match
    except re.error as e:
        # Return an error message if the regex is invalid
        return f"Regex error: {e}"