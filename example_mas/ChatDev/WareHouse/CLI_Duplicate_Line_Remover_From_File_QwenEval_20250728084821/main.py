'''
Main entry point for the application. Handles command-line arguments.
'''
import sys
import argparse
from core import remove_duplicates
def main():
    parser = argparse.ArgumentParser(description='Remove duplicate lines from a text file.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    args = parser.parse_args()
    try:
        remove_duplicates(args.input, args.output)
        if args.output:
            print(f'Duplicates removed and saved to {args.output}')
        else:
            print('Duplicates removed and printed to standard output')
    except FileNotFoundError:
        print(f'Error: The file {args.input} was not found.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
if __name__ == '__main__':
    main()