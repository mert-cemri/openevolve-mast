'''
This module contains a function to compare two lists of scores and guesses.
'''
def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    Parameters:
    game (list of int): The actual scores of the matches.
    guess (list of int): The guessed scores of the matches.
    Returns:
    list of int: A list of differences between the actual scores and the guessed scores.
    Examples:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(g - s) for g, s in zip(game, guess)]