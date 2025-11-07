'''
Main entry point for the Line Number Utility application.
Handles command-line arguments.
'''
import sys
import argparse
from line_number_utility import LineNumberUtility
def main():
    parser = argparse.ArgumentParser(description='Add line numbers to a text file.')
    parser.add_argument('input_file', help='Input text file')
    parser.add_argument('-o', '--output_file', help='Output text file (optional)')
    args = parser.parse_args()
    utility = LineNumberUtility(args.input_file, args.output_file)
    utility.process_file()
if __name__ == '__main__':
    main()