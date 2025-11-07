'''
Main entry point for the File Splitter CLI utility.
Handles command-line arguments and initializes the file splitting process.
'''
import sys
from file_splitter import FileSplitter
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <file_path> <chunk_size_in_mb>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        chunk_size_mb = int(sys.argv[2])
        if chunk_size_mb <= 0:
            raise ValueError("Chunk size must be a positive integer.")
    except ValueError as e:
        print(f"Invalid chunk size: {e}")
        sys.exit(1)
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    splitter = FileSplitter()
    splitter.split_file(file_path, chunk_size)
if __name__ == "__main__":
    main()