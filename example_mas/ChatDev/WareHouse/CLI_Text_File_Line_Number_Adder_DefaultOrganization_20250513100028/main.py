'''
Main application file for the CLI utility to add line numbers to a text file.
'''
import argparse
from file_operations import read_file, add_line_numbers, write_to_file
def main():
    parser = argparse.ArgumentParser(description="Add line numbers to a text file.")
    parser.add_argument('input_file', help="Path to the input text file.")
    parser.add_argument('-o', '--output', help="Path to the output text file. If not provided, output will be printed to standard output.")
    args = parser.parse_args()
    try:
        content = read_file(args.input_file)
        numbered_content = add_line_numbers(content)
        if args.output:
            write_to_file(numbered_content, args.output)
            print(f"File saved to {args.output}")
        else:
            print(numbered_content)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()