'''
Dictionary module for the CLI dictionary lookup tool.
This module handles loading and searching the dictionary file.
'''
import sys
class Dictionary:
    def __init__(self, file_path):
        self.word_definitions = {}
        self.load_dictionary(file_path)
    def load_dictionary(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    word, definition = parse_dictionary_line(line, line_number)
                    if word:
                        self.word_definitions[word] = definition
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found. Please ensure the file is in the correct location.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while loading the dictionary: {e}")
            sys.exit(1)
    def get_definition(self, word):
        return self.word_definitions.get(word.lower(), None)
def parse_dictionary_line(line, line_number):
    parts = line.strip().split(':', 1)
    if len(parts) == 2:
        word = parts[0].strip().lower()
        definition = parts[1].strip()
        if not word or not definition:
            print(f"Warning: Line {line_number} is malformed and will be skipped.")
            return None, None
        return word, definition
    print(f"Warning: Line {line_number} is missing a colon (:) and will be skipped.")
    return None, None