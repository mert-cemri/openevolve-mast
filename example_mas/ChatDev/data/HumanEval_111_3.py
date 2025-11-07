'''
This module contains the implementation of the histogram function which calculates
the frequency of each letter in a given string and returns the letters with the highest frequency.
'''
def histogram(test):
    """Given a string representing a space-separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
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
    # Dictionary to store the count of each letter
    count_dict = {}
    # Count the occurrences of each letter
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    # Find the maximum count value
    if count_dict:
        max_count = max(count_dict.values())
    else:
        return {}
    # Create a dictionary of letters with the maximum count
    result = {letter: count for letter, count in count_dict.items() if count == max_count}
    return result