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
'''
def is_bored(S):
    # Split the string into sentences using '.', '?', '!' as delimiters
    import re
    sentences = re.split(r'[.?!]', S)
    # Initialize boredom count
    boredom_count = 0
    # Iterate over each sentence
    for sentence in sentences:
        # Strip leading and trailing whitespace
        stripped_sentence = sentence.strip()
        # Check if the sentence starts with "I"
        if stripped_sentence.startswith("I"):
            boredom_count += 1
    return boredom_count
# Example usage
if __name__ == "__main__":
    print(is_bored("Hello world"))  # Output: 0
    print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1