'''
Main file to run the CLI-based Contact Book application.
'''
import csv
from contact import Contact
class ContactBookCLI:
    def __init__(self):
        # Initialize contact list
        self.contacts = []
        self.load_contacts()
    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        if name and phone and email:
            contact = Contact(name, phone, email)
            self.contacts.append(contact)
            self.save_contacts()
            print("Contact added successfully!")
        else:
            print("Error: Please fill all fields.")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(f"{contact.name} - {contact.phone} - {contact.email}")
    def search_contact(self):
        search_name = input("Enter name to search: ")
        found = False
        for contact in self.contacts:
            if search_name.lower() in contact.name.lower():
                print(f"{contact.name} - {contact.phone} - {contact.email}")
                found = True
        if not found:
            print("No contact found with that name.")
    def delete_contact(self):
        name_to_delete = input("Enter the name of the contact to delete: ")
        initial_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name_to_delete.lower()]
        if len(self.contacts) < initial_count:
            self.save_contacts()
            print("Contact deleted successfully!")
        else:
            print("No contact found with that name.")
    def load_contacts(self):
        try:
            with open("contacts.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                self.contacts = []
                for row in reader:
                    if len(row) == 3:  # Ensure the row has exactly three elements
                        self.contacts.append(Contact(row[0], row[1], row[2]))
        except FileNotFoundError:
            self.contacts = []
    def save_contacts(self):
        with open("contacts.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.email])
    def run(self):
        while True:
            print("\nContact Book CLI")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    app = ContactBookCLI()
    app.run()