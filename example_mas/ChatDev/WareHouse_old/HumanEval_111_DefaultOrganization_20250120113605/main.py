'''
This module contains the implementation of the histogram function, which calculates
the frequency of each letter in a given string and returns the letter(s) with the highest
frequency along with their count.
'''
def histogram(test):
    """Given a string representing space-separated lowercase letters, return a dictionary
    of the letter(s) with the most repetition and their corresponding count.
    If several letters have the same occurrence, return all of them.
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    # Split the input string into a list of letters
    letters = test.split()
    # Dictionary to store the frequency of each letter
    frequency = {}
    # Count the occurrences of each letter
    for letter in letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    # Find the maximum frequency
    max_count = max(frequency.values(), default=0)
    # Create a dictionary of letters with the maximum frequency
    result = {letter: count for letter, count in frequency.items() if count == max_count}
    return result