'''
PalindromeDetector module to detect palindromes in text.
'''
import re
class PalindromeDetector:
    @staticmethod
    def is_palindrome(phrase):
        '''
        Checks if a given phrase is a palindrome.
        :param phrase: Phrase to check.
        :return: True if the phrase is a palindrome, False otherwise.
        '''
        # Normalize the phrase by removing non-alphanumeric characters and converting to lowercase
        normalized_phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()
        # Check if the phrase reads the same forwards and backwards
        return normalized_phrase == normalized_phrase[::-1]
    @staticmethod
    def find_palindromes(text):
        '''
        Finds and returns all palindromes in the given text.
        :param text: Text to search for palindromes.
        :return: List of detected palindromes.
        '''
        # Split the text into sentences or phrases
        sentences = re.split(r'[.!?]', text)
        # Filter and return sentences or phrases that are palindromes
        palindromes = []
        for sentence in sentences:
            if PalindromeDetector.is_palindrome(sentence):
                palindromes.append(sentence.strip())
        return palindromes