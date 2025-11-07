'''
This is the main file for the CLI sorting application. It handles command-line arguments for sorting text files.
'''
import sys
from sorter import sort_lines
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <output_file> [reverse]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    reverse = len(sys.argv) > 3 and sys.argv[3] == "reverse"
    try:
        sort_lines(input_file, output_file, reverse)
        print("File sorted successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
if __name__ == "__main__":
    main()