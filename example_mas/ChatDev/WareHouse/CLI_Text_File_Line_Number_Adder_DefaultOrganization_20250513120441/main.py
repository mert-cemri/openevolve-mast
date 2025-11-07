'''
This is the main file for the CLI utility to add line numbers to a text file. It handles command-line arguments and processes the input file accordingly.
'''
import argparse
def add_line_numbers(input_file, output_file=None):
    """
    Reads the input file, adds line numbers to each line, and writes the result to the output file or prints to standard output.
    """
    with open(input_file, 'r') as file:
        content = file.readlines()
    numbered_content = [f"{i+1}: {line}" for i, line in enumerate(content)]
    if output_file:
        with open(output_file, 'w') as file:
            file.writelines(numbered_content)
    else:
        for line in numbered_content:
            print(line, end='')
def main():
    """
    Parses command-line arguments and invokes the line numbering function.
    """
    parser = argparse.ArgumentParser(description="Add line numbers to a text file.")
    parser.add_argument('input_file', help="Path to the input text file.")
    parser.add_argument('-o', '--output', help="Path to the output text file. If not provided, output will be printed to standard output.")
    args = parser.parse_args()
    add_line_numbers(args.input_file, args.output)
if __name__ == "__main__":
    main()