'''
This is the main module for running the CLI personal journal application.
'''
from journal import Journal
def main():
    journal = Journal()
    password = input("Enter your journal password: ")
    while True:
        print("\n1. Add Entry\n2. View Entries\n3. Save Entries\n4. Load Entries\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            content = input("Enter your journal entry: ")
            journal.add_entry(content, password)
        elif choice == '2':
            for entry in journal.entries:
                print(f"{entry.timestamp}: {entry.content}")
        elif choice == '3':
            journal.save_entries()
            print("Entries saved.")
        elif choice == '4':
            journal.load_entries(password)
            print("Entries loaded.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()