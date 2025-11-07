'''
Contains the CodeCounter class and utility functions for counting lines of code.
'''
import os
class CodeCounter:
    def __init__(self):
        self.extensions = ['.py', '.js', '.c']
    def count_lines(self, directory):
        results = {ext: 0 for ext in self.extensions}
        for root, _, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in self.extensions:
                    file_path = os.path.join(root, file)
                    results[ext] += self.count_file_lines(file_path, ext)
        return results
    def count_file_lines(self, file_path, extension):
        count = 0
        in_multiline_comment = False
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                is_comment, in_multiline_comment = is_comment_or_blank(line, extension, in_multiline_comment)
                if not is_comment:
                    count += 1
        return count
def is_comment_or_blank(line, extension, in_multiline_comment):
    stripped_line = line.strip()
    if not stripped_line:
        return True, in_multiline_comment
    if extension in ['.js', '.c']:
        if in_multiline_comment:
            if '*/' in stripped_line:
                in_multiline_comment = False
            return True, in_multiline_comment
        if stripped_line.startswith('/*'):
            in_multiline_comment = True
            return True, in_multiline_comment
        if stripped_line.startswith('//'):
            return True, in_multiline_comment
    if extension == '.py':
        if in_multiline_comment:
            if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                in_multiline_comment = False
            return True, in_multiline_comment
        if stripped_line.startswith('#'):
            return True, in_multiline_comment
        if stripped_line.startswith("'''") or stripped_line.startswith('"""'):
            in_multiline_comment = True
            return True, in_multiline_comment
    return False, in_multiline_comment