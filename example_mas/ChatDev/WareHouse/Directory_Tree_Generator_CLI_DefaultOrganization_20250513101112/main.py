'''
Main application file for the directory tree CLI utility.
'''
import argparse
from tree_generator import generate_tree_structure
def main():
    parser = argparse.ArgumentParser(description='Generate a visual tree structure of a directory.')
    parser.add_argument('directory', type=str, help='The directory path to generate the tree for.')
    parser.add_argument('--max-depth', type=int, default=None, help='Maximum depth of the tree.')
    args = parser.parse_args()
    # Handle max_depth being None as no limit
    max_depth = args.max_depth if args.max_depth is not None else float('inf')
    tree_structure = generate_tree_structure(args.directory, max_depth)
    print(tree_structure)
if __name__ == "__main__":
    main()