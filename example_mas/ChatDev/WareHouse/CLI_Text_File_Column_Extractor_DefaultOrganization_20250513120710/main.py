'''
Main application file for the CLI program to extract specific columns from a CSV or space-delimited text file.
'''
import argparse
from file_handler import FileHandler
def main():
    parser = argparse.ArgumentParser(description="Extract specific columns from a CSV or space-delimited text file.")
    parser.add_argument('filepath', type=str, help='Path to the CSV or text file.')
    parser.add_argument('columns', type=str, help='Comma-separated list of column numbers or headers to extract.')
    args = parser.parse_args()
    try:
        file_handler = FileHandler(args.filepath)
        extracted_data = file_handler.parse_file(args.columns)
        for line in extracted_data:
            print(line)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()