'''
Main application file for the CLI text difference tool.
'''
import argparse
from file_utils import compare_texts
def main():
    parser = argparse.ArgumentParser(description="CLI Text Difference Tool")
    parser.add_argument('file1', help='Path to the first text file')
    parser.add_argument('file2', help='Path to the second text file')
    args = parser.parse_args()
    differences = compare_texts(args.file1, args.file2)
    if differences:
        print("Differences found:")
        for line in differences:
            print(line)
    else:
        print("No differences found.")
if __name__ == "__main__":
    main()