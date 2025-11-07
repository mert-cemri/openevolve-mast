'''
Contains the SnippetApp class for the CLI application.
'''
from snippet_manager import SnippetManager
class SnippetApp:
    def __init__(self):
        self.manager = SnippetManager()
    def run(self):
        while True:
            command = input("Enter command (add/search/get/exit): ").strip().lower()
            if command == 'add':
                self.add_snippet_ui()
            elif command == 'search':
                self.search_snippets_ui()
            elif command == 'get':
                self.get_snippet_ui()
            elif command == 'exit':
                print("Exiting the application.")
                break
            else:
                print("Invalid command. Please try again.")
    def add_snippet_ui(self):
        language = input("Enter the language: ").strip()
        title = input("Enter the title: ").strip()
        code = input("Enter the code: ").strip()
        if language and title and code:
            self.manager.add_snippet(language, title, code)
    def search_snippets_ui(self):
        query = input("Enter search query: ").strip()
        if query:
            results = self.manager.search_snippets(query)
            if results:
                for snippet in results:
                    self.display_snippet(snippet)
            else:
                print("No snippets found.")
    def get_snippet_ui(self):
        title = input("Enter the title of the snippet to retrieve: ").strip()
        snippet = self.manager.get_snippet(title)
        if snippet:
            self.display_snippet(snippet)
        else:
            print("Snippet not found.")
    def display_snippet(self, snippet):
        print(f"Title: {snippet.title}\nLanguage: {snippet.language}\nCode:\n{snippet.code}\n")