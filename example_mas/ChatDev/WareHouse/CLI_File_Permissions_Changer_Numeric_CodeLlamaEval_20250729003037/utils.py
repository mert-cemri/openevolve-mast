import os
def validate_file_path(file_path):
    # Check if the file or directory exists
    if not os.path.exists(file_path):
        return False
    # Check if the file or directory is a file
    if not os.path.isfile(file_path):
        return False
    # Check if the file or directory is readable
    if not os.access(file_path, os.R_OK):
        return False
    return True
def validate_permissions(permissions):
    # Check if the permissions are a string
    if not isinstance(permissions, str):
        return False
    # Check if the permissions are in octal notation
    if not permissions.isdigit():
        return False
    # Check if the permissions are a valid octal number
    if int(permissions) < 0 or int(permissions) > 777:
        return False
    return True