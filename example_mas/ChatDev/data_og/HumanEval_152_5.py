'''
This module contains the function `compare` which compares two lists of scores and guesses,
returning a list of the absolute differences between them.
'''
def compare(game, guess):
    """
    Compare two lists of scores and guesses, returning a list of the absolute differences.
    Parameters:
    game (list of int): The actual scores.
    guess (list of int): The guessed scores.
    Returns:
    list of int: A list of the absolute differences between the actual scores and guesses.
    Example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(g - s) for g, s in zip(game, guess)]