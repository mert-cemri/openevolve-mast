'''
Handles the command-line interface interactions.
'''
from snippet_manager import SnippetManager, Snippet
class CLIInterface:
    def __init__(self):
        self.manager = SnippetManager()
    def run(self):
        '''
        Main loop for the CLI interface. Displays menu options and handles user input.
        '''
        while True:
            print("\nCLI Code Snippet Manager")
            print("1. Add Snippet")
            print("2. Get Snippets by Language")
            print("3. Search Snippets")
            print("4. List All Snippets")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_snippet()
            elif choice == '2':
                self.get_snippets_by_language()
            elif choice == '3':
                self.search_snippets()
            elif choice == '4':
                self.list_all_snippets()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
    def add_snippet(self):
        '''
        Prompts the user to enter details for a new code snippet and adds it to the manager.
        '''
        language = input("Enter the language: ").strip()
        code = input("Enter the code: ").strip()
        description = input("Enter the description (optional): ").strip()
        if not language or not code:
            print("Language and code are required.")
            return
        snippet = Snippet(language, code, description)
        self.manager.add_snippet(snippet)
        print("Snippet added successfully.")
    def get_snippets_by_language(self):
        '''
        Prompts the user to enter a language and displays all snippets for that language.
        '''
        language = input("Enter the language: ").strip()
        snippets = self.manager.get_snippets_by_language(language)
        if snippets:
            for i, snippet in enumerate(snippets, 1):
                print(f"\nSnippet {i}:")
                print(f"Language: {snippet['language']}")
                print(f"Code: {snippet['code']}")
                print(f"Description: {snippet['description']}")
        else:
            print("No snippets found for this language.")
    def search_snippets(self):
        '''
        Prompts the user to enter a search query and displays all snippets matching the query.
        '''
        query = input("Enter the search query: ").strip()
        snippets = self.manager.search_snippets(query)
        if snippets:
            for i, snippet in enumerate(snippets, 1):
                print(f"\nSnippet {i}:")
                print(f"Language: {snippet['language']}")
                print(f"Code: {snippet['code']}")
                print(f"Description: {snippet['description']}")
        else:
            print("No snippets found matching the query.")
    def list_all_snippets(self):
        '''
        Displays all snippets stored in the manager.
        '''
        snippets = self.manager.get_all_snippets()
        if snippets:
            for i, snippet in enumerate(snippets, 1):
                print(f"\nSnippet {i}:")
                print(f"Language: {snippet['language']}")
                print(f"Code: {snippet['code']}")
                print(f"Description: {snippet['description']}")
        else:
            print("No snippets found.")