'''
Main entry point of the application. Initializes the CLI.
'''
import argparse
from code_counter import CodeCounter
def main():
    parser = argparse.ArgumentParser(description='Count lines of code in a directory.')
    parser.add_argument('directory', type=str, help='The directory to count lines of code in.')
    args = parser.parse_args()
    counter = CodeCounter()
    results = counter.count_lines(args.directory)
    for ext, count in results.items():
        print(f"{ext}: {count} lines")
if __name__ == "__main__":
    main()