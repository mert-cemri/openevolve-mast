'''
Main application file for the File Splitter utility as a CLI tool.
'''
import os
import argparse
from file_splitter import split_file
def main():
    parser = argparse.ArgumentParser(description='Split a large file into smaller parts.')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    parser.add_argument('output_dir', type=str, help='Directory to save the output parts')
    parser.add_argument('chunk_size', type=int, help='Chunk size in MB')
    args = parser.parse_args()
    try:
        split_file(args.file_path, args.chunk_size, args.output_dir)
        print("File split successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()