'''
Utility module for the CLI program that counts lines of code in a directory.
'''
import os
def get_file_extension(file_path):
    '''
    Extracts the file extension from the given file path.
    '''
    _, ext = os.path.splitext(file_path)
    return ext
def is_comment_line(line, extension, in_multiline_comment=False):
    '''
    Determines if a line is a comment or part of a multi-line comment based on the file extension.
    Handles single-line comments and multi-line comments that may start and end on the same line.
    '''
    line = line.strip()
    if not line:
        return True, in_multiline_comment
    if extension == '.py':
        if line.startswith('#'):
            return True, in_multiline_comment
    elif extension in ['.js', '.c', '.cpp', '.h']:
        if line.startswith('//'):
            return True, in_multiline_comment
        if '/*' in line and '*/' in line:
            return True, False
        if line.startswith('/*'):
            return True, True
        if line.endswith('*/'):
            return True, False
        if in_multiline_comment:
            return True, True
    return False, in_multiline_comment