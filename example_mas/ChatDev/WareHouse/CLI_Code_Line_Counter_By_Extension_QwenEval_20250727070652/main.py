'''
Main module for the CLI program that counts lines of code in a directory.
'''
import argparse
import sys
from cli import count_lines_of_code
from gui import create_gui
def parse_arguments():
    '''
    Parses command-line arguments for the program.
    '''
    parser = argparse.ArgumentParser(description="Count lines of code in a directory.")
    parser.add_argument('-d', '--directory', type=str, help='Directory to count lines of code.')
    parser.add_argument('-g', '--gui', action='store_true', help='Run the GUI version of the program.')
    return parser.parse_args()
def run_cli(directory):
    '''
    Runs the CLI version of the program to count lines of code in the specified directory.
    '''
    try:
        result = count_lines_of_code(directory)
        for ext, count in result.items():
            print(f"{ext}: {count} lines")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
def run_gui():
    '''
    Runs the GUI version of the program.
    '''
    create_gui()
def main():
    '''
    Main function to execute the program based on command-line arguments.
    '''
    args = parse_arguments()
    if args.gui:
        run_gui()
    elif args.directory:
        run_cli(args.directory)
    else:
        print("Please provide a directory or use the GUI.")
        sys.exit(1)
if __name__ == "__main__":
    main()