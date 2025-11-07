'''
Main application file for the CLI program to sort lines of a text file.
'''
import argparse
from sort_functions import sort_alphabetically, sort_reverse_alphabetically
from file_functions import read_file, write_file
def main():
    parser = argparse.ArgumentParser(description='Sort lines of a text file.')
    parser.add_argument('input_file', help='Path to the input text file')
    parser.add_argument('-o', '--output', help='Path to the output text file (optional)')
    parser.add_argument('-r', '--reverse', action='store_true', help='Sort in reverse alphabetical order')
    args = parser.parse_args()
    try:
        lines = read_file(args.input_file)
        if args.reverse:
            sorted_lines = sort_reverse_alphabetically(lines)
        else:
            sorted_lines = sort_alphabetically(lines)
        if args.output:
            write_file(args.output, sorted_lines)
        else:
            for line in sorted_lines:
                print(line, end='')
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()