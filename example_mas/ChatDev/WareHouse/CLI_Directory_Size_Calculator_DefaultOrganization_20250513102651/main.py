'''
Main application file for the Directory Size Calculator CLI.
'''
import os
import argparse
from size_calculator import calculate_directory_size, convert_size
def main():
    '''
    Main function to parse arguments and calculate directory size.
    '''
    parser = argparse.ArgumentParser(description="Calculate the total size of a directory and its subdirectories.")
    parser.add_argument('directory', type=str, help='The path to the directory')
    args = parser.parse_args()
    try:
        total_size = calculate_directory_size(args.directory)
        human_readable_size = convert_size(total_size)
        print(f"Total Size: {human_readable_size}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()