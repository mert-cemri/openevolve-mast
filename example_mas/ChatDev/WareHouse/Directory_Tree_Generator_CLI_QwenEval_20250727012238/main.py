'''
This module contains the command-line interface for the directory tree generator.
It parses command-line arguments and generates the directory tree structure.
'''
import os
import argparse
from directory_tree_generator import DirectoryTreeGenerator
def main():
    '''
    Main function to parse command-line arguments and generate the directory tree structure.
    '''
    parser = argparse.ArgumentParser(description='Generate a visual tree structure of a given directory.')
    parser.add_argument('path', type=str, help='The directory path to generate the tree for.')
    parser.add_argument('--max-depth', type=int, default=None, help='The maximum depth of the tree (optional).')
    args = parser.parse_args()
    try:
        generator = DirectoryTreeGenerator()
        tree = generator.generate_tree(args.path, args.max_depth)
        print(tree)
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()