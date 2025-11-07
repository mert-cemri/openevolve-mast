'''
Main application file for the CSV to Markdown converter CLI tool.
'''
import argparse
from converter import CSVToMarkdownConverter
def main():
    '''
    The entry point of the application that handles command-line arguments and outputs the Markdown table.
    '''
    parser = argparse.ArgumentParser(description='Convert CSV to Markdown table.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    args = parser.parse_args()
    try:
        converter = CSVToMarkdownConverter()
        markdown_table = converter.convert(args.csv_file)
        print(markdown_table)
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()