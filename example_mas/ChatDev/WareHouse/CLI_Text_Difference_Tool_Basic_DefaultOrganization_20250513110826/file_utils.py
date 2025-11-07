'''
Utility functions for file operations.
'''
def read_file(file_path):
    '''Read the contents of a file and return as a list of lines.'''
    with open(file_path, 'r') as file:
        return file.readlines()
def compare_texts(file1_path, file2_path):
    '''Compare two files and return the lines that are different.'''
    lines1 = read_file(file1_path)
    lines2 = read_file(file2_path)
    differences = []
    max_lines = max(len(lines1), len(lines2))
    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else ""
        line2 = lines2[i] if i < len(lines2) else ""
        if line1 != line2:
            differences.append(f"Line {i+1}:\nFile 1: {line1.strip()}\nFile 2: {line2.strip()}")
    return differences