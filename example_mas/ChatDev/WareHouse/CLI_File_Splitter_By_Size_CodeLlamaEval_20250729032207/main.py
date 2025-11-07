import sys
import os
import argparse
from splitter import Splitter
def main():
    '''
    Split a large file into smaller parts.
    '''
    parser = argparse.ArgumentParser(description='Split a large file into smaller parts.')
    parser.add_argument('-i', '--input', required=True, help='Input file')
    parser.add_argument('-o', '--output', required=True, help='Output directory')
    parser.add_argument('-s', '--size', required=True, help='Size of each output part')
    args = parser.parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    splitter = Splitter(args.input, args.output, args.size)
    splitter.split()
if __name__ == '__main__':
    main()