'''
This module contains a function to extract words from a sentence where the length of each word is a prime number.
'''
def is_prime(n):
    """
    Check if a number is a prime number.
    :param n: Integer to check for primality
    :return: True if n is a prime number, False otherwise
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
    Extract words from a sentence where the length of each word is a prime number.
    :param sentence: A string representing a sentence
    :return: A string containing words with prime lengths, in the original order
    """
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)
# Example usage:
# print(words_in_sentence("This is a test"))  # Output: "is"
# print(words_in_sentence("lets go for swimming"))  # Output: "go for"