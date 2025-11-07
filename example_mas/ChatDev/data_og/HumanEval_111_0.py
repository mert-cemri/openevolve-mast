'''
Given a string representing space-separated lowercase letters, return a dictionary
of the letter(s) with the most repetition and their corresponding count.
If several letters have the same occurrence, return all of them.
Example:
histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
histogram('a b b a') == {'a': 2, 'b': 2}
histogram('a b c a b') == {'a': 2, 'b': 2}
histogram('b b b b a') == {'b': 4}
histogram('') == {}
'''
def histogram(test):
    if not test:
        return {}
    # Split the input string into individual letters
    letters = test.split()
    # Count occurrences of each letter
    count_dict = {}
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    # Find the maximum occurrence count
    max_count = max(count_dict.values())
    # Collect all letters with the maximum occurrence count
    result = {letter: count for letter, count in count_dict.items() if count == max_count}
    return result