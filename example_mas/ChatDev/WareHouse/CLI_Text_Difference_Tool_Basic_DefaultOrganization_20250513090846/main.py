'''
Main application file for the CLI text difference tool.
'''
import argparse
from file_comparator import compare_text_files
def main():
    parser = argparse.ArgumentParser(description='CLI Text Difference Tool')
    parser.add_argument('file1', type=str, help='Path to the first text file')
    parser.add_argument('file2', type=str, help='Path to the second text file')
    args = parser.parse_args()
    differences = compare_text_files(args.file1, args.file2)
    if differences:
        for line in differences:
            print(line)
    else:
        print("The files are identical.")
if __name__ == "__main__":
    main()