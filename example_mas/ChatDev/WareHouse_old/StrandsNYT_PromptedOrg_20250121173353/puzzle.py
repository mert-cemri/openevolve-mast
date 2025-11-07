'''
Puzzle class manages the collection of word segments and validates connections.
'''
from word_segment import WordSegment
# Load a local dictionary file with error handling
def load_dictionary(file_path):
    '''
    Load a set of valid words from a local dictionary file.
    :param file_path: Path to the dictionary file.
    :return: A set of valid words.
    '''
    try:
        with open(file_path, 'r') as file:
            return set(word.strip().lower() for word in file.readlines())
    except FileNotFoundError:
        print(f"Error: The dictionary file '{file_path}' was not found.")
        return set()  # Return an empty set if the file is not found
# Load the dictionary from a local file
valid_words = load_dictionary('dictionary.txt')
class Puzzle:
    def __init__(self, segments):
        '''
        Initialize the puzzle with a list of word segments.
        :param segments: A list of strings representing word segments.
        '''
        self.segments = [WordSegment(segment) for segment in segments]
    def is_valid_connection(self, segment1, segment2):
        '''
        Check if two segments can be connected to form a valid word or phrase.
        :param segment1: The first word segment.
        :param segment2: The second word segment.
        :return: True if the connection is valid, False otherwise.
        '''
        combined = segment1.segment + segment2.segment
        return combined.lower() in valid_words