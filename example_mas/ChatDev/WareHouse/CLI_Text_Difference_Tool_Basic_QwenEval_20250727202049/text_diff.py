'''
Compares the contents of two files and identifies differences.
'''
class TextDiff:
    def __init__(self, file1_content, file2_content):
        self.file1_content = file1_content
        self.file2_content = file2_content
    def compare(self):
        diff_lines = []
        max_length = max(len(self.file1_content), len(self.file2_content))
        for i in range(max_length):
            line1 = self.file1_content[i].strip() if i < len(self.file1_content) else ""
            line2 = self.file2_content[i].strip() if i < len(self.file2_content) else ""
            if line1 != line2:
                diff_lines.append((i + 1, line1, line2))
        return diff_lines