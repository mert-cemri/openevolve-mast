'''
This module contains the VaultCLI class, which handles the command-line interface for the password vault.
'''
import getpass
class VaultCLI:
    def __init__(self, vault):
        self.vault = vault
    def start(self):
        while True:
            master_password = getpass.getpass("Enter master password: ")
            if self.vault.load_vault(master_password):
                print("Vault loaded successfully!")
                break
            else:
                print("Invalid master password! Please try again.")
        while True:
            print("\nOptions:")
            print("1. Add Entry")
            print("2. Get Entry")
            print("3. Remove Entry")
            print("4. Save Vault")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_entry()
            elif choice == '2':
                self.get_entry()
            elif choice == '3':
                self.remove_entry()
            elif choice == '4':
                self.save_vault(master_password)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
    def add_entry(self):
        service = input("Enter service name: ")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        self.vault.add_entry(service, username, password)
        print("Entry added successfully!")
    def get_entry(self):
        service = input("Enter service name: ")
        entry = self.vault.get_entry(service)
        if entry:
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
        else:
            print("Entry not found!")
    def remove_entry(self):
        service = input("Enter service name: ")
        self.vault.remove_entry(service)
        print("Entry removed successfully!")
    def save_vault(self, master_password):
        self.vault.save_vault(master_password)
        print("Vault saved successfully!")