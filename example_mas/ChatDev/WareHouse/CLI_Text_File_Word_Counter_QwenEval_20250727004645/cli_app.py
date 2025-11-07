'''
Handles the command-line interface operations for the Word Count Tool.
'''
import sys
from word_counter import WordCounter
class CLIApp:
    def run_cli(self):
        # Get the file path from the command-line arguments
        file_path = sys.argv[1]
        # Create an instance of WordCounter
        word_counter = WordCounter()
        # Count the words in the file
        word_count = word_counter.count_words(file_path)
        # Print the total word count
        print(f"Total word count: {word_count}")