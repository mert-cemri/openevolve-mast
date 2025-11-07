'''
This module contains a function to extract words from a sentence
whose lengths are prime numbers.
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
    Extract words from a sentence whose lengths are prime numbers.
    :param sentence: A string representing a sentence
    :return: A string containing words with prime lengths
    """
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)