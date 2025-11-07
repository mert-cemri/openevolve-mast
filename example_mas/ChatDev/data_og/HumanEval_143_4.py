'''
This module contains a function to filter words in a sentence based on the length of the words being prime numbers.
'''
def is_prime(n):
    """
    Check if a number is a prime number.
    Args:
    n (int): The number to check.
    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def words_in_sentence(sentence):
    """
    Return a string containing words from the original sentence whose lengths are prime numbers.
    Args:
    sentence (str): The input sentence.
    Returns:
    str: A string of words with prime lengths, in the same order as the original sentence.
    """
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)
# Example usage:
# print(words_in_sentence("This is a test"))  # Output: "is"
# print(words_in_sentence("lets go for swimming"))  # Output: "go for"