'''
Main module for the directory tree generator CLI utility.
Handles command-line arguments and calls the tree generator.
'''
import argparse
from tree_generator import generate_tree, print_tree
def parse_arguments():
    '''Parse command-line arguments.'''
    parser = argparse.ArgumentParser(description='Generate a visual tree structure of a given directory.')
    parser.add_argument('path', type=str, help='The directory path to generate the tree for.')
    parser.add_argument('--max-depth', type=int, default=None, help='The maximum depth of the tree.')
    return parser.parse_args()
def main():
    '''Main function to parse arguments and generate the tree.'''
    args = parse_arguments()
    try:
        tree = generate_tree(args.path, args.max_depth)
        print_tree(tree)
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()