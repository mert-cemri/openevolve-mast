'''
Module containing the CLI implementation for converting a CSV file to a JSON file.
'''
import argparse
import os
from csv_to_json_converter import convert_csv_to_json
def main():
    parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file.')
    parser.add_argument('input_csv', type=str, help='Path to the input CSV file')
    parser.add_argument('output_json', type=str, help='Path to the output JSON file')
    args = parser.parse_args()
    input_csv_path = args.input_csv
    output_json_path = args.output_json
    # Check if the input CSV file exists
    if not os.path.isfile(input_csv_path):
        print(f"Error: The input file '{input_csv_path}' does not exist.")
        return
    # Check if the output JSON file can be written
    output_dir = os.path.dirname(output_json_path)
    if output_dir and not os.path.isdir(output_dir):
        print(f"Error: The output directory '{output_dir}' does not exist.")
        return
    try:
        convert_csv_to_json(input_csv_path, output_json_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_csv_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_csv_path}' or writing to '{output_json_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    main()