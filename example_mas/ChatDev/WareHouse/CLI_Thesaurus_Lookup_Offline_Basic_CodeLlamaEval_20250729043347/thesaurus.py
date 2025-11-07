#!/usr/bin/env python3
import json
class Thesaurus:
    def __init__(self):
        self.thesaurus_file = 'thesaurus.json'
        self.thesaurus = self.load_thesaurus()
    def load_thesaurus(self):
        with open(self.thesaurus_file, 'r') as f:
            thesaurus = json.load(f)
        return thesaurus
    def get_synonyms(self, word):
        if word not in self.thesaurus:
            return None
        return self.thesaurus[word]['synonyms']
    def get_antonyms(self, word):
        if word not in self.thesaurus:
            return None
        return self.thesaurus[word]['antonyms']