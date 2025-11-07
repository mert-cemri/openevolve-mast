'''
Contains the GameLogic class for validating word formations in the NYT Strands puzzle game.
'''
class GameLogic:
    def __init__(self, valid_words):
        '''
        Initialize the GameLogic with a set of valid words.
        '''
        self.valid_words = set(valid_words)
    def validate(self, word):
        '''
        Validate if the formed word is in the set of valid words.
        '''
        return word in self.valid_words