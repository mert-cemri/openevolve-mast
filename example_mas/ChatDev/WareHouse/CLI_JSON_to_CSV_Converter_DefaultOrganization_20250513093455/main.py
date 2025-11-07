'''
Main application file for the JSON to CSV converter CLI tool.
'''
import argparse
from converter import convert_json_to_csv
def main():
    parser = argparse.ArgumentParser(description='Convert JSON file to CSV file.')
    parser.add_argument('json_path', type=str, help='Path to the input JSON file')
    parser.add_argument('csv_path', type=str, help='Path to the output CSV file')
    parser.add_argument('--fields', nargs='*', help='List of fields to flatten in the JSON file', default=[])
    parser.add_argument('--list_handling', type=str, choices=['index', 'concat'], default='index',
                        help='Method to handle lists: "index" to append indices, "concat" to concatenate list elements')
    args = parser.parse_args()
    try:
        convert_json_to_csv(args.json_path, args.csv_path, args.fields, args.list_handling)
        print("Conversion completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()