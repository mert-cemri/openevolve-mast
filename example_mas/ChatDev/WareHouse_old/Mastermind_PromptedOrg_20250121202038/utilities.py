'''
This module contains utility functions for the Mastermind game.
'''
def validate_guess(guess, code_length):
    '''
    Validates the player's guess to ensure it matches the required format.
    '''
    valid_colors = 'RGBYOP'
    return len(guess) == code_length and all(c in valid_colors for c in guess)