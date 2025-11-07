'''
This module contains the implementation of the compare function which compares two lists of scores and guesses.
'''
def compare(game, guess):
    """
    Compare two lists of scores and guesses and return a list of differences.
    Parameters:
    game (list): A list of integers representing the actual scores.
    guess (list): A list of integers representing the guessed scores.
    Returns:
    list: A list of integers representing the absolute difference between each score and guess, or zero if they match.
    Example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(g - s) if g != s else 0 for g, s in zip(game, guess)]