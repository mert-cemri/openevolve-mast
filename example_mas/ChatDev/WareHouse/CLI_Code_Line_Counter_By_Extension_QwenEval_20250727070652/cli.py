'''
CLI module for counting lines of code in a directory.
'''
import os
from utils import get_file_extension, is_comment_line
def ignore_comments_and_blank_lines(file_path):
    '''
    Reads a file and returns a list of lines that are not comments or blank lines.
    Handles exceptions that may occur during file reading.
    '''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []
    cleaned_lines = []
    in_multiline_comment = False
    for line in lines:
        is_comment, in_multiline_comment = is_comment_line(line, get_file_extension(file_path), in_multiline_comment)
        if not is_comment and line.strip():
            cleaned_lines.append(line)
    return cleaned_lines
def count_lines_of_code(directory):
    '''
    Counts the total lines of code in a directory, categorized by file extension.
    Ignores comments and blank lines.
    Handles exceptions that may occur during directory traversal.
    '''
    result = {}
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                ext = get_file_extension(file_path)
                if ext:
                    cleaned_lines = ignore_comments_and_blank_lines(file_path)
                    result[ext] = result.get(ext, 0) + len(cleaned_lines)
    except Exception as e:
        print(f"Error traversing directory {directory}: {e}")
    return result