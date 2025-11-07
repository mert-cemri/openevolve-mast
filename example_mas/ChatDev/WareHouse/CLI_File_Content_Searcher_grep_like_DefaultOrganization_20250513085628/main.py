'''
Main application file for the CLI program that searches for a given string/pattern within all text files in a specified directory and its subdirectories.
'''
import os
import sys
from search import search_in_files
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <directory> <pattern>")
        sys.exit(1)
    directory = sys.argv[1]
    pattern = sys.argv[2]
    results = search_in_files(directory, pattern)
    if results:
        for file, line in results:
            print(f"{file}: {line}")
    else:
        print("No matches found.")
if __name__ == "__main__":
    main()