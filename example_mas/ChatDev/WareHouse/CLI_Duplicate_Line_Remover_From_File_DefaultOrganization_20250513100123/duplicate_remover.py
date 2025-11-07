'''
Module to remove duplicate lines from a list of lines.
'''
def remove_duplicates(lines):
    '''
    Remove duplicate lines from the list, preserving the order of first occurrence.
    :param lines: List of lines from the text file.
    :return: List of unique lines.
    '''
    seen = set()
    unique_lines = []
    for line in lines:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)
    return unique_lines