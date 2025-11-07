'''
CLIInterface class to run the spell checker from the command line.
'''
import sys
class CLIInterface:
    def __init__(self, spell_checker):
        self.spell_checker = spell_checker
    def run_cli(self):
        if len(sys.argv) > 1:
            # Handle file input
            file_path = sys.argv[1]
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
            except FileNotFoundError:
                print(f"Error: The file {file_path} was not found.")
                sys.exit(1)
            except IOError:
                print(f"Error: An error occurred while reading the file {file_path}.")
                sys.exit(1)
        else:
            # Handle string input
            text = input("Enter text to check for spelling: ")
        # Check for misspelled words
        misspelled_words = self.spell_checker.check_text(text)
        if misspelled_words:
            print("Misspelled words:", ', '.join(misspelled_words))
        else:
            print("No misspelled words found.")