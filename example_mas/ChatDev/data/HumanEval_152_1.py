'''
This module contains the implementation of the compare function which compares two lists of scores and guesses.
'''
def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    :param game: List of integers representing the actual scores.
    :param guess: List of integers representing the guessed scores.
    :return: List of integers representing the differences between actual scores and guessed scores.
    Example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(g - s) for g, s in zip(game, guess)]