'''
CLI module for the search application.
This script searches for a given string/pattern within all text files in a specified directory and its subdirectories.
It uses the argparse module to handle command-line arguments for the directory and pattern.
'''
import argparse
from search_engine import search_files
def main():
    '''
    Main function to handle command-line arguments and execute the search.
    '''
    parser = argparse.ArgumentParser(description='Search for a given string/pattern within all text files in a specified directory and its subdirectories.')
    parser.add_argument('directory', type=str, help='The directory to search in.')
    parser.add_argument('pattern', type=str, help='The string/pattern to search for.')
    args = parser.parse_args()
    try:
        results = search_files(args.directory, args.pattern)
        display_results(results)
    except FileNotFoundError:
        print(f"Error: The directory '{args.directory}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def display_results(results):
    '''
    Function to display the search results in the console.
    '''
    if not results:
        print("No matching lines found.")
        return
    for filename, lines in results.items():
        print(f"File: {filename}")
        for line in lines:
            print(line, end='')
        print("\n" + "-"*60 + "\n")
if __name__ == '__main__':
    main()