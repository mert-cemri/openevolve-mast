'''
Module to change file permissions using numeric (octal) notation.
'''
import os
import re
def is_valid_octal(mode):
    """
    Check if the provided mode is a valid three-digit octal number.
    Args:
        mode (str): The permission mode as a string.
    Returns:
        bool: True if the mode is a valid three-digit octal number, False otherwise.
    """
    return re.match(r'^[0-7]{3}$', mode) is not None
def change_permissions(file_path, mode):
    """
    Change the permissions of a file or directory using numeric (octal) notation.
    Args:
        file_path (str): The path to the file or directory.
        mode (str): The permission mode (e.g., '755').
    Raises:
        ValueError: If the permission mode is invalid.
        FileNotFoundError: If the file or directory does not exist.
        PermissionError: If permission is denied to change permissions.
        Exception: For any other errors.
    """
    if not is_valid_octal(mode):
        raise ValueError("Invalid permission mode. Please use a three-digit numeric (octal) notation (e.g., 755, 644).")
    try:
        mode = int(mode, 8)
        os.chmod(file_path, mode)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file or directory '{file_path}' does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied to change permissions for '{file_path}'.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")