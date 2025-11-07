'''
Module for the command-line interface.
'''
import getpass
from journal import Journal, JournalEntry
from encryption import Encryption
class CLI:
    def __init__(self):
        password = getpass.getpass("Enter your password to encrypt/decrypt entries: ")
        self.encryption = Encryption(password)
        self.journal = Journal('journal.json', self.encryption)  # Update this line
        self.journal.load()
    def run(self):
        while True:
            print("\nPersonal Journal CLI")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_entry()
            elif choice == '2':
                self.view_entries()
            elif choice == '3':
                self.journal.save()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    def add_entry(self):
        content = input("Enter your journal entry: ")
        entry = JournalEntry(content, self.encryption, self.encryption.salt)
        self.journal.add_entry(entry)
        print("Entry added successfully.")
    def view_entries(self):
        if not self.journal.entries:
            print("No entries found.")
            return
        for entry in self.journal.entries:
            print(f"\nTimestamp: {entry.timestamp}")
            try:
                decrypted_content = self.encryption.decrypt(entry.content)
                print(f"Content: {decrypted_content}")
            except Exception as e:
                print("Failed to decrypt entry. Incorrect password?")