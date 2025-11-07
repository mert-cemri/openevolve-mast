'''
Main application file to handle command-line interactions for removing duplicate lines from a text file.
'''
import argparse
from duplicate_remover import DuplicateRemover
def main():
    parser = argparse.ArgumentParser(description="Remove duplicate lines from a text file.")
    parser.add_argument('input_file', help="Path to the input text file.")
    parser.add_argument('-o', '--output', help="Path to the output text file. If not provided, output will be printed to standard output.")
    args = parser.parse_args()
    remover = DuplicateRemover()
    result = remover.remove_duplicates(args.input_file)
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Output written to {args.output}")
    else:
        print(result)
if __name__ == "__main__":
    main()