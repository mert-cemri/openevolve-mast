'''
Contains the core logic for removing duplicate lines from a file.
'''
def remove_duplicates(input_file, output_file=None):
    '''
    Removes duplicate lines from the input file and writes the result to the output file.
    If output_file is None, the result is printed to standard output.
    Preserves the order of the first occurrence of each line.
    '''
    seen = set()
    unique_lines = []
    with open(input_file, 'r') as infile:
        for line in infile:
            if line not in seen:
                unique_lines.append(line)
                seen.add(line)
    if output_file:
        with open(output_file, 'w') as outfile:
            outfile.writelines(unique_lines)
    else:
        for line in unique_lines:
            print(line, end='')