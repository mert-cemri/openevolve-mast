'''
This module contains the Thesaurus class which handles loading and querying the thesaurus data.
'''
import json
class Thesaurus:
    def __init__(self, file_path):
        '''
        Initializes the Thesaurus with data from a JSON file.
        :param file_path: Path to the thesaurus JSON file.
        '''
        with open(file_path, 'r') as file:
            self.data = json.load(file)
    def get_synonyms(self, word):
        '''
        Returns a list of synonyms for a given word.
        :param word: The word to find synonyms for.
        :return: A list of synonyms.
        '''
        return self.data.get(word, {}).get('synonyms', [])
    def get_antonyms(self, word):
        '''
        Returns a list of antonyms for a given word.
        :param word: The word to find antonyms for.
        :return: A list of antonyms.
        '''
        return self.data.get(word, {}).get('antonyms', [])