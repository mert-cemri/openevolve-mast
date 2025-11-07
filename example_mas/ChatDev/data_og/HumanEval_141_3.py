'''
This module contains the function file_name_check which validates a file name based on specific criteria.
'''
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the Latin alphabet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    """
    # Split the file name by the dot
    parts = file_name.split('.')
    # Check if there is exactly one dot
    if len(parts) != 2:
        return 'No'
    # Validate the substring before the dot
    before_dot = parts[0]
    if not before_dot or not before_dot[0].isalpha():
        return 'No'
    # Count digits in the file name
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    # Validate the substring after the dot
    after_dot = parts[1]
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
# Example usage
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll")) # => 'No'