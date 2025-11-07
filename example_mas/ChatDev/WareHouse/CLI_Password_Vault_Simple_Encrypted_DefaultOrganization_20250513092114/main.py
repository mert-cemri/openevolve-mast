'''
Main file to run the password vault application with a CLI.
'''
from vault import PasswordVault
def main():
    # Initialize the password vault
    vault = PasswordVault('vault.enc')
    # Prompt for master password
    master_password = input("Enter Master Password: ")
    vault.create_master_key(master_password)
    vault.load_vault()
    while True:
        print("\nPassword Vault CLI")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            vault.add_entry(service, username, password)
            print("Entry added successfully.")
        elif choice == '2':
            entries = vault.get_entries()
            if entries:
                for service, credentials in entries.items():
                    print(f"{service}: {credentials['username']} / {credentials['password']}")
            else:
                print("No entries found.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()