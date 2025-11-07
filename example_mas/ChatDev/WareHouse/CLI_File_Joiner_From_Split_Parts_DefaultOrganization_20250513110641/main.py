'''
Main entry point for the file joiner application. Initializes and runs the CLI.
'''
import argparse
from file_joiner import FileJoiner
def main():
    parser = argparse.ArgumentParser(description='Join file parts into a single file.')
    parser.add_argument('first_part_name', type=str, help='The first part of the file to join.')
    parser.add_argument('output_file_name', type=str, help='The name of the output file.')
    args = parser.parse_args()
    file_joiner = FileJoiner()
    try:
        file_joiner.join_files(args.first_part_name, args.output_file_name)
        print("Files joined successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()