'''
Main entry point for the JSON to CSV converter application.
Handles command-line arguments and performs the conversion.
'''
import argparse
import sys
from converter import convert_json_to_csv
def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert JSON to CSV')
    parser.add_argument('--input', type=str, required=True, help='Path to the input JSON file')
    parser.add_argument('--output', type=str, required=True, help='Path to the output CSV file')
    parser.add_argument('--fields', type=str, help='Comma-separated fields to include in the CSV')
    return parser.parse_args()
def main():
    args = parse_arguments()
    fields = args.fields.split(',') if args.fields else None
    try:
        convert_json_to_csv(args.input, args.output, fields)
        print("Conversion completed successfully.")
    except FileNotFoundError:
        print(f"Error: The file {args.input} does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {args.input} is not a valid JSON file.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
if __name__ == '__main__':
    main()