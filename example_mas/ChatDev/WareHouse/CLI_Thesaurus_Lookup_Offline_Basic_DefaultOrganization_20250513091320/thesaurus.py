'''
Thesaurus data handling for loading and querying synonyms and antonyms.
'''
class Thesaurus:
    def __init__(self, file_path):
        self.data = self.load_thesaurus(file_path)
    def load_thesaurus(self, file_path):
        thesaurus_data = {}
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 3:
                    word, synonyms, antonyms = parts
                    thesaurus_data[word] = {
                        'synonyms': synonyms.split(',') if synonyms else [],
                        'antonyms': antonyms.split(',') if antonyms else []
                    }
        return thesaurus_data
    def get_synonyms(self, word):
        return self.data.get(word, {}).get('synonyms', [])
    def get_antonyms(self, word):
        return self.data.get(word, {}).get('antonyms', [])