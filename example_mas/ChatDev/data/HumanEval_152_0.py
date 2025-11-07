'''
This module contains a function to compare two lists of scores and guesses.
The function returns a list of absolute differences between the corresponding elements
of the two lists. If the elements are equal, the difference is 0.
'''
def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    :param game: List of actual scores
    :param guess: List of guessed scores
    :return: List of differences between actual scores and guessed scores
    """
    return [abs(g - s) for g, s in zip(game, guess)]