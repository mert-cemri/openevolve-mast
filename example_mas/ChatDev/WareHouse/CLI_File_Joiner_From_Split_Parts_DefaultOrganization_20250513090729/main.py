'''
Main application file for the File Joiner program using a command-line interface.
'''
import sys
from file_joiner import join_file_parts
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <first_part_path>")
        sys.exit(1)
    first_part_path = sys.argv[1]
    try:
        join_file_parts(first_part_path)
    except Exception as e:
        print(f"An error occurred: {e}")