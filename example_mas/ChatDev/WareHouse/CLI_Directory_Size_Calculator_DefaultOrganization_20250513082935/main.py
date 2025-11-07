'''
CLI application for calculating and displaying the total size of a directory and its subdirectories.
'''
import os
import argparse
from utils import get_directory_size, format_size
def main():
    parser = argparse.ArgumentParser(description="Calculate the total size of a directory and its subdirectories.")
    parser.add_argument("directory", help="The path to the directory")
    args = parser.parse_args()
    directory = args.directory
    if os.path.isdir(directory):
        total_size = get_directory_size(directory)
        human_readable_size = format_size(total_size)
        print(f"Total Size: {human_readable_size}")
    else:
        print("The specified path is not a directory.")
if __name__ == "__main__":
    main()