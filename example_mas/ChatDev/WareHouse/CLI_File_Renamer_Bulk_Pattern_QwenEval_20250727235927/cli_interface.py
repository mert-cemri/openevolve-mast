'''
Handles the command-line interface for the File Renamer application.
'''
import argparse
from file_renamer import FileRenamer
class CLIInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Rename files in a directory based on a specified pattern.")
        self.parser.add_argument('directory', type=str, help='The directory containing the files to rename.')
        self.parser.add_argument('--prefix', type=str, help='Add a prefix to all filenames.')
        self.parser.add_argument('--replace', type=str, nargs=2, help='Replace a substring in all filenames. Usage: --replace old new')
        self.parser.add_argument('--sequential', type=int, help='Add sequential numbers to all filenames, starting from the specified number.')
    def parse_arguments(self):
        return self.parser.parse_args()
    def run(self):
        args = self.parse_arguments()
        try:
            renamer = FileRenamer(args.directory)
            if args.prefix:
                renamer.add_prefix(args.prefix)
            if args.replace:
                renamer.replace_substring(args.replace[0], args.replace[1])
            if args.sequential is not None:  # Check if --sequential is explicitly provided
                renamer.add_sequential_numbers(args.sequential)
        except ValueError as e:
            print(f"Error: {e}")