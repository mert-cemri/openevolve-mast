'''
Module to handle command-line interface for the journal application.
'''
from journal import Journal
def main():
    journal = Journal('journal_entries.json')
    while True:
        print("1. Add new entry")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            content = input("Enter your journal entry: ")
            password = input("Enter a password to encrypt your entry: ")
            journal.add_entry(content, password)
            print("Entry added successfully!")
        elif choice == '2':
            break
        else:
            print("Invalid option. Please try again.")