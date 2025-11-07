'''
Main entry point for the CLI code snippet manager application.
'''
from snippet_app import SnippetApp
def main():
    app = SnippetApp()
    app.run()
if __name__ == "__main__":
    main()