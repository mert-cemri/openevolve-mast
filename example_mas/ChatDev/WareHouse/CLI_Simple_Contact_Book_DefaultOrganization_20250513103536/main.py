'''
Main application file for the CLI contact book.
'''
import csv
from contact import Contact
class ContactBookApp:
    def __init__(self):
        self.contacts = []
        self.load_contacts()
    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        if name and phone and email:
            new_contact = Contact(name, phone, email)
            self.contacts.append(new_contact)
            self.save_contacts()
            print("Contact added successfully!")
        else:
            print("Please fill in all fields.")
    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("No contacts available.")
    def search_contact(self):
        name = input("Enter name to search: ")
        found_contacts = [c for c in self.contacts if c.name == name]
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("No contact found.")
    def delete_contact(self):
        name = input("Enter name to delete: ")
        found_contacts = [c for c in self.contacts if c.name == name]
        if not found_contacts:
            print("No contact found.")
            return
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        choice = input("Enter the number of the contact you want to delete: ")
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(found_contacts):
                confirm = input("Do you want to delete this contact? (yes/no): ")
                if confirm.lower() == 'yes':
                    self.contacts.remove(found_contacts[choice_index])
                    print("Contact deleted successfully!")
                    self.save_contacts()
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    def load_contacts(self):
        try:
            with open('contacts.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                self.contacts = [Contact(*row) for row in reader]
        except FileNotFoundError:
            self.contacts = []
    def save_contacts(self):
        with open('contacts.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.email])
    def run(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                print("Exiting Contact Book.")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    app = ContactBookApp()
    app.run()