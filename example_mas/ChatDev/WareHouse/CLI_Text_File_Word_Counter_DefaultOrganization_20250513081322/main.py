'''
This is the main file for the Word Count CLI tool.
It handles command-line arguments and outputs the word count.
'''
import sys
from utils import count_words_in_file
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        word_count = count_words_in_file(file_path)
        print(f"Total Words: {word_count}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()