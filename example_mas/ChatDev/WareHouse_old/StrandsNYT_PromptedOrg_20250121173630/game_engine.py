'''
GameEngine module to handle the logic for connecting segments and validating solutions.
'''
class GameEngine:
    def __init__(self, segments, word_list):
        '''
        Initialize the game engine with a list of word segments and a word list.
        '''
        self.segments = segments
        self.valid_words = set(word_list)  # Load a comprehensive word list
    def connect(self, indices):
        '''
        Connect segments based on provided indices and return the formed word.
        '''
        return ''.join(self.segments[i].text for i in indices)
    def is_valid_solution(self, word):
        '''
        Check if the formed word is a valid solution using the word list.
        '''
        return word in self.valid_words