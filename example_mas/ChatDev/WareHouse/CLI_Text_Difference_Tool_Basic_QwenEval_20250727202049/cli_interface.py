'''
Handles command-line interactions.
'''
from file_reader import FileReader
from text_diff import TextDiff
class CLIInterface:
    def __init__(self, file1_path, file2_path):
        self.file1_reader = FileReader(file1_path)
        self.file2_reader = FileReader(file2_path)
    def run(self):
        file1_content = self.file1_reader.get_content()
        file2_content = self.file2_reader.get_content()
        text_diff = TextDiff(file1_content, file2_content)
        diff_lines = text_diff.compare()
        self.display_diff(diff_lines)
    def display_diff(self, diff_lines):
        if not diff_lines:
            print("No differences found.")
        else:
            print("Differences found:")
            for line_number, line1, line2 in diff_lines:
                print(f"Line {line_number}:")
                print(f"  File 1: {line1}")
                print(f"  File 2: {line2}")