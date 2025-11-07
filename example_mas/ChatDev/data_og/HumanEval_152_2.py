'''
This module contains the function to compare game scores with guesses and return the differences.
'''
def compare(game, guess):
    """
    Compare two lists of scores and guesses, returning a list of differences.
    Parameters:
    game (list): A list of actual scores.
    guess (list): A list of guessed scores.
    Returns:
    list: A list containing the absolute differences between each corresponding element in game and guess.
          If the guess is correct, the difference is 0.
    Example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(g - s) for g, s in zip(game, guess)]