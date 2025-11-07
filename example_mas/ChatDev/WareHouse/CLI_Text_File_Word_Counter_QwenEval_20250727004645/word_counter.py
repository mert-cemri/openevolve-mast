'''
Handles the logic of counting words in a text file.
'''
import re
class WordCounter:
    def count_words(self, file_path):
        try:
            # Open the file in read mode with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                content = file.read()
                # Use regex to find sequences of alphanumeric characters as words
                words = re.findall(r'\b\w+\b', content)
                # Return the number of words found
                return len(words)
        except FileNotFoundError:
            # Print an error message if the file is not found
            print(f"Error: The file {file_path} does not exist.")
            return 0
        except Exception as e:
            # Print an error message for any other exceptions
            print(f"An error occurred: {e}")
            return 0