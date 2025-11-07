'''
Main entry point for the CLI Thesaurus Lookup Tool.
This script initializes the Thesaurus and CLI components and starts the user interaction.
'''
from cli import CLI
from thesaurus import Thesaurus
def main():
    thesaurus = Thesaurus()
    try:
        thesaurus.load_thesaurus('thesaurus.txt')
    except FileNotFoundError:
        print("Error: The thesaurus file 'thesaurus.txt' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while loading the thesaurus: {e}")
        return
    cli = CLI(thesaurus)
    cli.run()
if __name__ == "__main__":
    main()