'''
Module for handling command line interface operations.
'''
import sys
from sorting import sort_lines, read_file, write_file
def cli():
    '''
    Handles command line arguments and invokes the sorting logic.
    Expected usage: python main.py <file_path> <asc|desc> [output_file]
    - file_path: Path to the input text file.
    - asc|desc: Sort order. 'asc' for ascending, 'desc' for descending.
    - output_file (optional): Path to the output text file. If not provided, output is printed to standard output.
    '''
    if len(sys.argv) < 3:
        print("Usage: python main.py <file_path> <asc|desc> [output_file]")
        sys.exit(1)
    file_path = sys.argv[1]
    order = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    try:
        lines = read_file(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file '{file_path}': {e}")
        sys.exit(1)
    try:
        sorted_lines = sort_lines(lines, order)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    try:
        if output_file:
            write_file(output_file, sorted_lines)
            print(f"Sorted lines written to {output_file}")
        else:
            print("Sorted Lines:")
            print("".join(line.strip() for line in sorted_lines))  # Strip newline characters for standard output
    except Exception as e:
        print(f"Error writing to the file '{output_file}': {e}")
        sys.exit(1)