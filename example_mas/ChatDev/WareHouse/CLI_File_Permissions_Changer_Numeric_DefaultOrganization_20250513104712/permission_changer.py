'''
Module to change file permissions using the os module.
'''
import os
def change_file_permissions(path, mode):
    '''
    Change the file permissions of a given file or directory.
    :param path: The path to the file or directory.
    :param mode: The permission mode in octal notation.
    :raises: OSError if the file or directory does not exist or permissions cannot be changed.
    '''
    if not os.path.exists(path):
        raise OSError(f"The path '{path}' does not exist.")
    os.chmod(path, mode)