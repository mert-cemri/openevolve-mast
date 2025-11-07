'''
Contains the logic to change file permissions.
'''
import os
import stat
import re
def change_permissions(path, mode):
    '''
    Changes the permissions of a file or directory using the provided mode.
    :param path: File or directory path
    :param mode: Numeric (octal) permission mode (e.g., 755, 644)
    '''
    # Validate that the mode is a valid octal number (only contains digits 0-7) and has a length of 3 or 4
    if not re.match(r'^[0-7]{3,4}$', mode):
        raise ValueError(f"Invalid mode: {mode}. Please provide a valid octal number (3 or 4 digits, only 0-7).")
    try:
        numeric_mode = int(mode, 8)
        os.chmod(path, numeric_mode)
    except FileNotFoundError:
        raise FileNotFoundError(f"File or directory not found: {path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {path}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")