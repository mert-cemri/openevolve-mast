'''
This module contains the function `file_name_check` which validates a file name based on specific criteria.
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
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    # Split the file name into name and extension
    name, extension = file_name.rsplit('.', 1)
    # Check if the extension is valid
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    # Check if the name is not empty and starts with a letter
    if not name or not name[0].isalpha():
        return 'No'
    # Check for the number of digits in the name
    digit_count = sum(c.isdigit() for c in name)
    if digit_count > 3:
        return 'No'
    return 'Yes'