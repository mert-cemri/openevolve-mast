'''
Module containing the CLIInterface class for handling the command-line interface.
'''
import sys
import os
from file_hasher import FileHasher
from duplicate_finder import DuplicateFinder
class CLIInterface:
    def run(self, args):
        '''Parse command-line arguments and execute the program.'''
        if len(args) != 1:
            print("Usage: python main.py <directory>")
            sys.exit(1)
        directory = args[0]
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a valid directory.")
            sys.exit(1)
        file_hasher = FileHasher()
        file_hashes = file_hasher.hash_directory(directory)
        duplicate_finder = DuplicateFinder(file_hashes)
        duplicates = duplicate_finder.find_duplicates()
        if duplicates:
            print("Duplicate files found:")
            for hash_value, paths in duplicates.items():
                print(f"Hash: {hash_value}")
                for path in paths:
                    print(f"  {path}")
        else:
            print("No duplicate files found.")