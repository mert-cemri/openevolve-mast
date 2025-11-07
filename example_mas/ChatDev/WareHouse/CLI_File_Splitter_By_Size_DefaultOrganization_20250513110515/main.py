'''
Main application file for the File Splitter CLI utility.
'''
import os
import argparse
from file_splitter_logic import split_file
def main():
    parser = argparse.ArgumentParser(description='Split a large file into smaller parts.')
    parser.add_argument('file_path', type=str, help='Path to the file to be split.')
    parser.add_argument('chunk_size', type=int, help='Chunk size in MB.')
    parser.add_argument('--output_dir', type=str, default='.', help='Directory to save the split files.')
    args = parser.parse_args()
    file_path = args.file_path
    chunk_size = args.chunk_size * 1024 * 1024  # Convert MB to bytes
    output_dir = args.output_dir
    if not os.path.isfile(file_path):
        print("Error: Please select a valid file.")
        return
    if not os.path.isdir(output_dir):
        print("Error: Please select a valid output directory.")
        return
    try:
        split_file(file_path, chunk_size, output_dir)
        print("Success: File split successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()