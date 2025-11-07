'''
Handles the storage, retrieval, categorization, and searching of code snippets.
'''
import json
from file_handler import FileHandler
class Snippet:
    def __init__(self, language, code, description=""):
        self.language = language
        self.code = code
        self.description = description
    def to_dict(self):
        '''
        Converts the Snippet object to a dictionary for storage.
        '''
        return {
            "language": self.language,
            "code": self.code,
            "description": self.description
        }
class SnippetManager:
    def __init__(self, file_path="snippets.json"):
        self.file_handler = FileHandler(file_path)
        self.snippets = self.file_handler.load_snippets()
    def add_snippet(self, snippet):
        '''
        Adds a new snippet to the manager and saves it to the file.
        '''
        self.snippets.append(snippet.to_dict())
        self.file_handler.save_snippets(self.snippets)
    def get_snippets_by_language(self, language):
        '''
        Retrieves all snippets for a given language.
        '''
        return [s for s in self.snippets if s['language'].lower() == language.lower()]
    def search_snippets(self, query):
        '''
        Searches for snippets containing the given query in their code or description.
        '''
        return [s for s in self.snippets if query.lower() in s['code'].lower() or query.lower() in s['description'].lower()]
    def get_all_snippets(self):
        '''
        Retrieves all snippets.
        '''
        return self.snippets