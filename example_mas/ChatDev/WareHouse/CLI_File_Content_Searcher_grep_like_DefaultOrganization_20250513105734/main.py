'''
Main module to run the search application as a CLI.
'''
import argparse
from filesearcher import FileSearcher
def main():
    '''
    Entry point of the application. Parses command-line arguments and performs the search.
    '''
    parser = argparse.ArgumentParser(description='Search for a pattern in text files within a directory.')
    parser.add_argument('directory', type=str, help='The directory to search in.')
    parser.add_argument('pattern', type=str, help='The pattern to search for.')
    args = parser.parse_args()
    searcher = FileSearcher()
    results = searcher.search_files(args.directory, args.pattern)
    for filename, lines in results.items():
        print(f"File: {filename}")
        for line in lines:
            print(f"  {line}")
        print()
if __name__ == "__main__":
    main()