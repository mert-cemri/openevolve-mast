import sys
import argparse
from sort import sort_lines
# Parse command-line arguments
parser = argparse.ArgumentParser(description='Sort lines of a text file alphabetically or reverse-alphabetically.')
parser.add_argument('input_file', help='Input text file')
parser.add_argument('output_file', help='Output text file')
parser.add_argument('--reverse', action='store_true', help='Sort lines in reverse alphabetical order')
args = parser.parse_args()
# Read input file
with open(args.input_file, 'r') as f:
    lines = f.readlines()
# Sort lines
sorted_lines = sort_lines(lines, reverse=args.reverse)
# Write output file
with open(args.output_file, 'w') as f:
    f.write('\n'.join(sorted_lines))