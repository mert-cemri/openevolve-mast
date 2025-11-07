'''
Main module for the word count CLI tool.
This module handles command-line arguments and calls the word count function.
'''
import sys
import word_count
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python main.py <file_path> [encoding]")
        sys.exit(1)
    file_path = sys.argv[1]
    encoding = sys.argv[2] if len(sys.argv) == 3 else 'utf-8'
    try:
        word_count = word_count.count_words(file_path, encoding)
        print(f"Total word count: {word_count}")
    except OSError as e:
        print(f"Error: An error occurred while reading the file '{file_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()