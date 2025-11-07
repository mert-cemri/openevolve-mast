'''
Main application file for the Word Count CLI tool.
'''
import argparse
from utils import count_words_in_file
def main():
    '''
    Run the CLI tool to count words in a text file.
    '''
    parser = argparse.ArgumentParser(description='Count words in a text file.')
    parser.add_argument('file_path', type=str, help='Path to the text file')
    args = parser.parse_args()
    try:
        word_count = count_words_in_file(args.file_path)
        print(f"Total Words: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file at {args.file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()