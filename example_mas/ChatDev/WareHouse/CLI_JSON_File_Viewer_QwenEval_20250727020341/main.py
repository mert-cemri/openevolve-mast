'''
Module to create a CLI application for viewing JSON files in a human-readable, indented format.
'''
import sys
from json_module import read_json, format_json
def main():
    '''
    Main function to handle command line arguments and print formatted JSON.
    Checks if the correct number of arguments is provided.
    Calls read_json and format_json functions to process the file and print the result.
    '''
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>", file=sys.stderr)
        sys.exit(1)
    file_path = sys.argv[1]
    json_data = read_json(file_path)
    formatted_json = format_json(json_data)
    print(formatted_json)
if __name__ == '__main__':
    main()