'''
Puzzle module to manage the word segments and game state.
'''
from word_segment import WordSegment
from game_engine import GameEngine
class Puzzle:
    def __init__(self, segments, word_list):
        '''
        Initialize the puzzle with a list of word segments and a word list.
        '''
        self.segments = [WordSegment(segment) for segment in segments]
        self.game_engine = GameEngine(self.segments, word_list)
    def connect_segments(self, indices):
        '''
        Connect segments based on provided indices and return the result.
        '''
        return self.game_engine.connect(indices)
    def is_valid_solution(self, word):
        '''
        Check if the formed word is a valid solution.
        '''
        return self.game_engine.is_valid_solution(word)