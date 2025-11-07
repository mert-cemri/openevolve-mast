'''
Main application file for the CSV to JSON converter CLI.
'''
import argparse
from converter import convert_csv_to_json
def main():
    parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file.')
    parser.add_argument('input_path', type=str, help='Path to the input CSV file.')
    parser.add_argument('output_path', type=str, help='Path to the output JSON file.')
    args = parser.parse_args()
    try:
        convert_csv_to_json(args.input_path, args.output_path)
        print("CSV file successfully converted to JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()