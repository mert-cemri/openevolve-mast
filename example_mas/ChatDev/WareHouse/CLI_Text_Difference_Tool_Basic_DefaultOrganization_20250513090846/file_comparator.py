'''
File comparator module to compare two text files line by line.
'''
def compare_text_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
    differences = []
    max_lines = max(len(file1_lines), len(file2_lines))
    for i in range(max_lines):
        line1 = file1_lines[i].strip() if i < len(file1_lines) else ""
        line2 = file2_lines[i].strip() if i < len(file2_lines) else ""
        if line1 != line2:
            if line1:
                differences.append(f"Line {i+1}:\n+ File 1: {line1}")
            if line2:
                differences.append(f"- File 2: {line2}")
            differences.append("")  # Add a blank line for better readability
    return differences