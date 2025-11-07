'''
Main application file for the JSON to CSV converter with CLI.
'''
import argparse
from converter import convert_json_to_csv
def main():
    parser = argparse.ArgumentParser(description='Convert a JSON file to a CSV file.')
    parser.add_argument('input_path', help='Path to the input JSON file')
    parser.add_argument('output_path', help='Path to the output CSV file')
    parser.add_argument('--fields', nargs='+', help='Specify fields to include in the CSV')
    parser.add_argument('--list_handling', choices=['concatenate', 'index'], default='concatenate',
                        help='Specify how to handle lists: concatenate elements or use indices')
    args = parser.parse_args()
    try:
        convert_json_to_csv(args.input_path, args.output_path, args.fields, args.list_handling)
        print("File converted successfully!")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except json.JSONDecodeError:
        print("Error: The input file is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()