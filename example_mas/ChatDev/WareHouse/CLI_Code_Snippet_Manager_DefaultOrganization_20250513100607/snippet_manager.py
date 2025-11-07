'''
Manages code snippets, including adding, searching, and retrieving snippets.
'''
import json
import os
class SnippetManager:
    def __init__(self, filename='snippets.json'):
        self.filename = filename
        self.snippets = []
        self.load_snippets()
    def add_snippet(self, language, description, code):
        snippet = {
            'language': language,
            'description': description,
            'code': code
        }
        self.snippets.append(snippet)
        self.save_snippets()
    def search_snippets(self, query):
        return [s for s in self.snippets if query.lower() in s['language'].lower() or query.lower() in s['description'].lower()]
    def retrieve_snippet(self, index):
        if 0 <= index < len(self.snippets):
            return self.snippets[index]
        return None
    def load_snippets(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.snippets = json.load(file)
    def save_snippets(self):
        with open(self.filename, 'w') as file:
            json.dump(self.snippets, file, indent=4)