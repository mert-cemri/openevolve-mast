'''
main.py
Main function to handle command-line input and output formatted JSON.
'''
import sys
from json_formatter import format_json_file
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_json_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        formatted_json = format_json_file(file_path)
        print(formatted_json)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()