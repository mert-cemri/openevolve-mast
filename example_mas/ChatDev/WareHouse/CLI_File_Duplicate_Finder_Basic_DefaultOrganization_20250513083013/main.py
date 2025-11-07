'''
Main application file for the Duplicate File Finder CLI.
'''
import argparse
from file_utils import find_duplicate_files
def main():
    parser = argparse.ArgumentParser(description='Find duplicate files in a directory based on their content.')
    parser.add_argument('directory', type=str, help='The directory to search for duplicate files.')
    args = parser.parse_args()
    duplicates = find_duplicate_files(args.directory)
    if duplicates:
        print("Duplicate files found:")
        for files in duplicates:
            print("\n".join(files))
            print()
    else:
        print("No duplicate files found.")
if __name__ == "__main__":
    main()