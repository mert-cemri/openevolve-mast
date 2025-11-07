'''
Main application file to handle command-line interactions for extracting columns from a file.
'''
import argparse
from file_handler import FileHandler
from column_extractor import ColumnExtractor
def main():
    parser = argparse.ArgumentParser(description='Extract specific columns from a CSV or space-delimited text file.')
    parser.add_argument('file_path', type=str, help='Path to the input file (CSV or space-delimited text).')
    parser.add_argument('columns', type=str, help='Comma-separated list of column numbers or headers to extract.')
    args = parser.parse_args()
    try:
        data = FileHandler.read_file(args.file_path)
        delimiter = ',' if args.file_path.endswith('.csv') else ' '
        parsed_data = FileHandler.parse_file(data, delimiter)
        if args.columns.replace(',', '').isdigit():
            column_numbers = list(map(int, args.columns.split(',')))
            extracted_data = ColumnExtractor.extract_by_number(parsed_data, column_numbers)
        else:
            column_headers = args.columns.split(',')
            extracted_data = ColumnExtractor.extract_by_header(parsed_data, column_headers)
        for row in extracted_data:
            print('\t'.join(row))
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()