'''
Module to handle thesaurus data for the CLI Thesaurus Lookup Tool.
This module defines the Thesaurus class which loads and provides access to thesaurus data.
The thesaurus data file should be formatted as follows:
Each line contains a word, followed by a comma, then a semicolon-separated list of synonyms,
another comma, and a semicolon-separated list of antonyms.
Example:
happy,joyful;cheerful;content;delighted,unhappy;sad
'''
class Thesaurus:
    def __init__(self):
        self.data = {}
    def load_thesaurus(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print(f"Warning: Skipping malformed line in thesaurus file: {line.strip()}")
                    continue
                word = parts[0].strip()
                synonyms = [s.strip() for s in parts[1].split(';') if s.strip()]
                antonyms = [a.strip() for a in parts[2].split(';') if a.strip()]
                self.data[word] = {'synonyms': synonyms, 'antonyms': antonyms}
    def get_synonyms(self, word):
        return self.data.get(word, {}).get('synonyms', [])
    def get_antonyms(self, word):
        return self.data.get(word, {}).get('antonyms', [])