'''
This module contains a function to filter words in a sentence based on the length of the words being prime numbers.
'''
def is_prime(n):
    """
    Check if a number is a prime number.
    :param n: Integer to check for primality.
    :return: True if n is a prime number, False otherwise.
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
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.
    :param sentence: A string representing the sentence.
    :return: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)
# Example usage:
# print(words_in_sentence("This is a test"))  # Output: "is"
# print(words_in_sentence("lets go for swimming"))  # Output: "go for"