'''
This module contains the function `file_name_check` which validates a file name based on specified criteria.
'''
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphabet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphabet letter)
    """
    # Split the file name by the dot
    parts = file_name.split('.')
    # Check if there is exactly one dot
    if len(parts) != 2:
        return 'No'
    # Validate the part before the dot
    name_part = parts[0]
    if not name_part or not name_part[0].isalpha():
        return 'No'
    # Count digits in the name part
    digit_count = sum(c.isdigit() for c in name_part)
    if digit_count > 3:
        return 'No'
    # Validate the part after the dot
    extension_part = parts[1]
    if extension_part not in ['txt', 'exe', 'dll']:
        return 'No'
    # If all conditions are met, return 'Yes'
    return 'Yes'