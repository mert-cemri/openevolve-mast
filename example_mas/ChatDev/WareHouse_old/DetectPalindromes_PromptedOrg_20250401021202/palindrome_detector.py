'''
Module containing the PalindromeDetector class for detecting palindromes in a text file.
'''
import re
from typing import List
class PalindromeDetector:
    '''
    Class to detect palindromes in a given text file.
    '''
    def __init__(self, filepath: str):
        '''
        Initializes the PalindromeDetector with the path to the text file.
        Args:
            filepath (str): Path to the text file to analyze.
        '''
        self.filepath = filepath
    def is_palindrome(self, text: str) -> bool:
        '''
        Checks if the provided text is a palindrome.
        Args:
            text (str): The text to check.
        Returns:
            bool: True if the text is a palindrome, False otherwise.
        '''
        cleaned_text = re.sub(r'[^A-Za-z0-9]', '', text.lower())
        return cleaned_text == cleaned_text[::-1] and len(cleaned_text) > 1
    def extract_words(self, text: str) -> List[str]:
        '''
        Extracts words from the provided text.
        Args:
            text (str): The text from which to extract words.
        Returns:
            List[str]: A list of words extracted from the text.
        '''
        return re.findall(r'\b\w+\b', text)
    def extract_sentences(self, text: str) -> List[str]:
        '''
        Extracts sentences from the provided text.
        Args:
            text (str): The text from which to extract sentences.
        Returns:
            List[str]: A list of sentences extracted from the text.
        '''
        sentences = re.split(r'[.!?]', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]
    def find_palindromes(self) -> List[str]:
        '''
        Reads the file, extracts words and sentences, and finds palindromes.
        Returns:
            List[str]: A list of unique palindromes found in the file.
        '''
        palindromes_set = set()
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                # Check sentences/phrases
                sentences = self.extract_sentences(content)
                for sentence in sentences:
                    if self.is_palindrome(sentence):
                        palindromes_set.add(sentence.strip())
                # Check individual words
                words = self.extract_words(content)
                for word in words:
                    if self.is_palindrome(word):
                        palindromes_set.add(word.lower())
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        return sorted(list(palindromes_set))