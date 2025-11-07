'''
Main entry point of the application. Handles the flow of the application based on whether the user is using the CLI or GUI.
'''
import sys
from cli_handler import parse_arguments
from file_reader import read_file
from column_extractor import extract_columns
from output_handler import output_data
from gui_handler import run_gui
if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = parse_arguments()
        data = read_file(args.file_path, args.delimiter)
        extracted_data = extract_columns(data, args.columns, args.delimiter)
        output_data(extracted_data, args.output, args.delimiter)
    else:
        run_gui()