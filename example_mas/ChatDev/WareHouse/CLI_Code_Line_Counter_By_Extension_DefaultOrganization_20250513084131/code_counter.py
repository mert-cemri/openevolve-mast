'''
Contains the logic for counting lines of code in files.
'''
import os
class CodeCounter:
    def __init__(self):
        self.extensions = {
            '.py': '#',
            '.js': '//',
            '.c': '//',
            '.cpp': '//',
            '.java': '//'
        }
        self.in_multiline_comment = False
    def count_lines(self, directory):
        results = {}
        for root, _, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in self.extensions:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        code_lines = sum(1 for line in lines if not self.is_comment_or_blank(line, ext))
                        results[ext] = results.get(ext, 0) + code_lines
        return results
    def is_comment_or_blank(self, line, extension):
        line = line.strip()
        if not line:
            return True
        # Single-line comment check
        comment_symbol = self.extensions.get(extension)
        if comment_symbol and line.startswith(comment_symbol):
            return True
        # Multi-line comment check
        if extension in ['.c', '.cpp', '.java']:
            if '/*' in line:
                self.in_multiline_comment = True
            if self.in_multiline_comment:
                if '*/' in line:
                    self.in_multiline_comment = False
                return True
        return False