'''
This module contains a function to check the validity of a file name based on specific criteria.
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
    """
    # Split the file name by the dot
    parts = file_name.split('.')
    # Check if there is exactly one dot and valid substrings
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return 'No'
    # Check if the substring before the dot starts with a letter
    if not parts[0][0].isalpha():
        return 'No'
    # Check if the substring after the dot is valid
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    # Count the digits in the file name
    digit_count = sum(c.isdigit() for c in file_name)
    # Validate the number of digits
    if digit_count > 3:
        return 'No'
    return 'Yes'