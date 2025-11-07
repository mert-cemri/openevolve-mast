'''
Main application file for the CLI password vault.
'''
from vault_manager import VaultManager
from encryption_utility import EncryptionUtility
class MainApp:
    def __init__(self):
        self.vault_manager = VaultManager("vault.dat")
        self.encryption_utility = EncryptionUtility()
        self.master_password = input("Enter your master password: ")
        if not self.master_password:
            print("Error: Master password is required!")
            exit()
    def add_entry(self):
        website = input("Enter website/service name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if website and username and password:
            encrypted_data = self.encryption_utility.encrypt(f"{website},{username},{password}", self.master_password)
            self.vault_manager.add_entry(encrypted_data)
            print("Entry added successfully!")
    def view_entries(self):
        entries = self.vault_manager.get_entries()
        decrypted_entries = [self.encryption_utility.decrypt(entry, self.master_password) for entry in entries]
        print("Entries:")
        for entry in decrypted_entries:
            print(entry)
    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_entry()
            elif choice == '2':
                self.view_entries()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
if __name__ == "__main__":
    app = MainApp()
    app.run()