'''
Main script to run the Duplicate File Finder application with a CLI.
'''
import argparse
from finder import DuplicateFileFinder
def main():
    parser = argparse.ArgumentParser(description="Find duplicate files in a specified directory.")
    parser.add_argument('directory', type=str, help='The directory to search for duplicate files.')
    args = parser.parse_args()
    finder = DuplicateFileFinder()
    duplicates = finder.find_duplicates(args.directory)
    if duplicates:
        print("Duplicate files found:")
        for dup in duplicates:
            print(f"Duplicate: {dup[0]} and {dup[1]}")
    else:
        print("No duplicates found.")
if __name__ == "__main__":
    main()