'''
Main module to run the CSV to JSON conversion application as a CLI utility.
'''
import argparse
from converter import CSVtoJSONConverter
def main():
    '''
    Start the CLI application.
    '''
    parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file.')
    parser.add_argument('csv_path', type=str, help='Path to the input CSV file')
    parser.add_argument('json_path', type=str, help='Path to the output JSON file')
    args = parser.parse_args()
    converter = CSVtoJSONConverter()
    try:
        converter.convert(args.csv_path, args.json_path)
        print("CSV file successfully converted to JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()