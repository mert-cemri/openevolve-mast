'''
Contains the SnippetManager and Snippet classes for managing code snippets.
'''
import json
import os
class Snippet:
    def __init__(self, language, title, code):
        self.language = language
        self.title = title
        self.code = code
class SnippetManager:
    def __init__(self, storage_file='snippets.json'):
        self.storage_file = storage_file
        self.snippets = []
        self.load_snippets()
    def add_snippet(self, language, title, code):
        existing_snippet = self.get_snippet(title)
        if existing_snippet:
            overwrite = input(f"A snippet with the title '{title}' already exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite != 'yes':
                print("Snippet not added.")
                return
        snippet = Snippet(language, title, code)
        self.snippets.append(snippet)
        self.save_snippets()
        print("Snippet added successfully!")
    def search_snippets(self, query):
        return [s for s in self.snippets if query.lower() in s.title.lower() or query.lower() in s.language.lower()]
    def get_snippet(self, title):
        for snippet in self.snippets:
            if snippet.title == title:
                return snippet
        return None
    def load_snippets(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                self.snippets = [Snippet(**snippet) for snippet in data]
    def save_snippets(self):
        with open(self.storage_file, 'w') as file:
            json.dump([s.__dict__ for s in self.snippets], file, indent=4)