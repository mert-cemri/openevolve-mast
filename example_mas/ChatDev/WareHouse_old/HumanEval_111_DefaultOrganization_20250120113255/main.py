'''
This module contains the implementation of the histogram function, which analyzes a string of space-separated lowercase letters and returns a dictionary of the letter(s) with the most repetitions and their corresponding count.
'''
def histogram(test):
    """Given a string representing space-separated lowercase letters, return a dictionary
    of the letter(s) with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    if not test:
        return {}
    # Split the input string into individual letters
    letters = test.split()
    # Count occurrences of each letter
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    # Find the maximum occurrence count
    max_count = max(letter_count.values())
    # Collect all letters with the maximum count
    result = {letter: count for letter, count in letter_count.items() if count == max_count}
    return result