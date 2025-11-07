'''
Contains the TreeCLI class which handles command-line interactions.
'''
import argparse
from tree_generator import TreeGenerator
class TreeCLI:
    def run(self):
        '''
        Parses command-line arguments and generates the directory tree.
        '''
        parser = argparse.ArgumentParser(description="Generate a directory tree structure.")
        parser.add_argument("directory", help="The root directory to generate the tree from.")
        parser.add_argument("--max-depth", type=int, default=3, help="The maximum depth to traverse.")
        args = parser.parse_args()
        generator = TreeGenerator()
        tree = generator.generate_tree(args.directory, args.max_depth)
        print(tree)