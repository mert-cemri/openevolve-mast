'''
Main application file for the Duplicate Line Remover CLI tool.
'''
import argparse
from duplicate_remover import remove_duplicates
def main():
    parser = argparse.ArgumentParser(description='Remove duplicate lines from a text file.')
    parser.add_argument('input_file', type=str, help='Path to the input text file.')
    parser.add_argument('-o', '--output', type=str, help='Path to the output text file. If not provided, output will be printed to standard output.')
    args = parser.parse_args()
    try:
        with open(args.input_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {args.input_file} was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file {args.input_file}.")
        return
    unique_lines = remove_duplicates(lines)
    if args.output:
        try:
            with open(args.output, 'w') as file:
                file.writelines(unique_lines)
            print(f"Output written to {args.output}")
        except IOError:
            print(f"Error: Could not write to the file {args.output}.")
    else:
        print(''.join(unique_lines))
if __name__ == "__main__":
    main()