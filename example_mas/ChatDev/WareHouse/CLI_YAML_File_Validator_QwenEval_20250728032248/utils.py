'''
Utility functions for the YAML file validator.
'''
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def format_error_message(error):
    if hasattr(error, 'problem_mark'):
        line = error.problem_mark.line + 1
        column = error.problem_mark.column + 1
        return f"Line {line}, Column {column}: {error.problem}"
    return str(error)