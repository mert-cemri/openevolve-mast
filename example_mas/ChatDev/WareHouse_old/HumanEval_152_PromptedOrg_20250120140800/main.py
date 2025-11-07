'''
This module contains a function to compare two lists of scores and guesses.
The function returns a list of differences between the scores and guesses.
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
    Example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    # Ensure the lists are of the same length
    if len(game) != len(guess):
        raise ValueError("The length of game and guess lists must be the same.")
    # Calculate the differences
    differences = [abs(g - gs) for g, gs in zip(game, guess)]
    return differences