'''
Main application file for the Log Analyzer CLI tool.
'''
import argparse
from log_analyzer import analyze_log_file
def main():
    parser = argparse.ArgumentParser(description='Analyze a log file for a specific pattern.')
    parser.add_argument('file_path', type=str, help='Path to the log file')
    parser.add_argument('pattern', type=str, help='Pattern to search for in the log file')
    args = parser.parse_args()
    try:
        count = analyze_log_file(args.file_path, args.pattern)
        print(f"Lines containing '{args.pattern}': {count}")
    except FileNotFoundError:
        print(f"Error: The file '{args.file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()