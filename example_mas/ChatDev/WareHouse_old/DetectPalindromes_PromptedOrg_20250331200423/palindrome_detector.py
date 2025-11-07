'''
Module containing the PalindromeDetector class for detecting palindromes at word and phrase levels in a text file.
'''
import re
from typing import List, Tuple
class PalindromeDetector:
    '''
    Class to detect palindromes at word and phrase levels in a given text file.
    '''
    def __init__(self, file_path: str):
        '''
        Initializes the PalindromeDetector with the path to the text file.
        :param file_path: Path to the text file to analyze.
        '''
        self.file_path = file_path
    def is_word_palindrome(self, word: str) -> bool:
        '''
        Checks if a given word is a palindrome.
        :param word: The word to check.
        :return: True if the word is a palindrome, False otherwise.
        '''
        cleaned_word = word.lower()
        return cleaned_word == cleaned_word[::-1] and len(cleaned_word) > 1
    def is_phrase_palindrome(self, phrase: str) -> bool:
        '''
        Checks if a given phrase or sentence is a palindrome, ignoring spaces, punctuation, and case.
        :param phrase: The phrase or sentence to check.
        :return: True if the phrase is a palindrome, False otherwise.
        '''
        cleaned_phrase = re.sub(r'[\W_]', '', phrase.lower())
        return cleaned_phrase == cleaned_phrase[::-1] and len(cleaned_phrase) > 1
    def extract_words(self, text: str) -> List[str]:
        '''
        Extracts words from the given text.
        :param text: The text to extract words from.
        :return: A list of words.
        '''
        return re.findall(r'\b\w+\b', text)
    def extract_phrases(self, text: str) -> List[str]:
        '''
        Extracts phrases/sentences from the given text.
        :param text: The text to extract phrases from.
        :return: A list of phrases/sentences.
        '''
        return re.split(r'[.!?]+', text)
    def find_palindromes(self) -> Tuple[List[str], List[str]]:
        '''
        Finds and returns sorted lists of unique word-level and phrase-level palindromes from the file.
        :return: A tuple containing two sorted lists: (word-level palindromes, phrase-level palindromes).
        :raises FileNotFoundError: If the file does not exist.
        :raises Exception: For other unexpected errors.
        '''
        word_palindromes_set = set()
        phrase_palindromes_set = set()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Word-level palindrome detection
            words = self.extract_words(content)
            for word in words:
                if self.is_word_palindrome(word):
                    word_palindromes_set.add(word.lower())
            # Phrase-level palindrome detection
            phrases = self.extract_phrases(content)
            for phrase in phrases:
                cleaned_phrase = phrase.strip()
                if cleaned_phrase and self.is_phrase_palindrome(cleaned_phrase):
                    phrase_palindromes_set.add(cleaned_phrase)
        return sorted(list(word_palindromes_set)), sorted(list(phrase_palindromes_set))