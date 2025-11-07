'''
Handles command-line arguments using the argparse library.
'''
import argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description='Extract specific columns from a CSV or space-delimited text file.')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    parser.add_argument('columns', type=str, help='Column numbers or headers to extract (comma-separated)')
    parser.add_argument('--delimiter', type=str, default=',', help='Delimiter for the input file (default: comma)')
    parser.add_argument('--output', type=str, default=None, help='Path to the output file (default: stdout)')
    return parser.parse_args()