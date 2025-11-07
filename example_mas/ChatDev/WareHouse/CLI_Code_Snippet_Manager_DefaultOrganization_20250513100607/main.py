'''
Main entry point for the CLI code snippet manager application.
'''
import argparse
from snippet_manager import SnippetManager
def main():
    parser = argparse.ArgumentParser(description='CLI Code Snippet Manager')
    parser.add_argument('action', choices=['add', 'search', 'retrieve'], help='Action to perform')
    parser.add_argument('--language', help='Programming language of the snippet')
    parser.add_argument('--description', help='Description of the snippet')
    parser.add_argument('--code', help='Code snippet')
    parser.add_argument('--query', help='Search query')
    parser.add_argument('--index', type=int, help='Index of the snippet to retrieve')
    args = parser.parse_args()
    manager = SnippetManager()
    if args.action == 'add':
        if args.language and args.description and args.code:
            manager.add_snippet(args.language, args.description, args.code)
            print("Snippet added successfully!")
        else:
            print("Error: Adding a snippet requires --language, --description, and --code arguments.")
    elif args.action == 'search':
        if args.query:
            snippets = manager.search_snippets(args.query)
            for i, snippet in enumerate(snippets):
                print(f"{i}: {snippet['language']} - {snippet['description']}")
        else:
            print("Error: Searching requires a --query argument.")
    elif args.action == 'retrieve':
        if args.index is not None:
            snippet = manager.retrieve_snippet(args.index)
            if snippet:
                print(f"Language: {snippet['language']}\nDescription: {snippet['description']}\nCode:\n{snippet['code']}")
            else:
                print("Error: Invalid index.")
        else:
            print("Error: Retrieving a snippet requires an --index argument.")
if __name__ == "__main__":
    main()