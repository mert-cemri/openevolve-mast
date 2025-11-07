'''
This module contains the implementation of the is_bored function, which counts the number of sentences starting with the word "I".
'''
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the string into sentences using '.', '?', and '!' as delimiters
    import re
    sentences = re.split(r'[.?!]', S)
    # Initialize a counter for sentences starting with "I"
    boredom_count = 0
    # Iterate over each sentence
    for sentence in sentences:
        # Strip leading and trailing whitespace
        sentence = sentence.strip()
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            boredom_count += 1
    return boredom_count