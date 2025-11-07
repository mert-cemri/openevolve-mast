'''
Main entry point for the CLI contact book application.
Handles user input and interacts with the ContactBook class.
'''
import contact_book
def main():
    contact_book_instance = contact_book.ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            if name and phone and email:
                contact_book_instance.add_contact(name, phone, email)
            else:
                print("Name, phone number, and email are required.")
        elif choice == '2':
            contact_book_instance.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ").strip()
            if name:
                contact_book_instance.search_contact(name)
            else:
                print("Name is required.")
        elif choice == '4':
            name = input("Enter name to delete: ").strip()
            if name:
                contact_book_instance.delete_contact(name)
            else:
                print("Name is required.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()