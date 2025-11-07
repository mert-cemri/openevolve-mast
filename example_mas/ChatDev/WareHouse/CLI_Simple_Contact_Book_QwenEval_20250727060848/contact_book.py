'''
Defines the ContactBook class which manages a collection of contacts.
Includes methods to add, view, search, and delete contacts.
'''
import contact
import file_manager
class ContactBook:
    def __init__(self):
        '''
        Initializes the ContactBook with an empty list of contacts and a FileManager.
        Loads existing contacts from the CSV file.
        '''
        self.contacts = []
        self.file_manager = file_manager.FileManager('contacts.csv')
        self.load_contacts()
    def load_contacts(self):
        '''
        Loads contacts from the CSV file into the contacts list.
        '''
        contacts_data = self.file_manager.read_contacts()
        for data in contacts_data:
            self.contacts.append(contact.Contact(data['name'], data['phone'], data['email']))
    def add_contact(self, name, phone, email):
        '''
        Adds a new contact to the contacts list and writes the updated list to the CSV file.
        '''
        new_contact = contact.Contact(name, phone, email)
        self.contacts.append(new_contact)
        self.file_manager.write_contacts(self.contacts)
        print(f"Contact {name} added successfully.")
    def view_contacts(self):
        '''
        Prints all contacts in the contacts list.
        If no contacts are found, it prints a message indicating that.
        '''
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
    def search_contact(self, name):
        '''
        Searches for contacts by name and prints the matching contacts.
        If no contacts are found, it prints a message indicating that.
        '''
        name = name.strip().lower()  # Strip leading/trailing spaces and convert to lowercase
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name]
        if not found_contacts:
            print(f"No contact found with name {name}.")
        else:
            print(f"Found {len(found_contacts)} contact(s) with name {name}:")
            for idx, contact in enumerate(found_contacts, start=1):
                print(f"{idx}. {contact}")
    def delete_contact(self, name):
        '''
        Deletes a contact by name from the contacts list and writes the updated list to the CSV file.
        If no contact is found, it prints a message indicating that.
        If multiple contacts are found, it asks the user which contact to delete.
        '''
        name = name.strip().lower()  # Strip leading/trailing spaces and convert to lowercase
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name]
        if not found_contacts:
            print(f"No contact found with name {name}.")
        elif len(found_contacts) == 1:
            self.contacts.remove(found_contacts[0])
            self.file_manager.write_contacts(self.contacts)
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Found {len(found_contacts)} contact(s) with name {name}:")
            for idx, contact in enumerate(found_contacts, start=1):
                print(f"{idx}. {contact}")
            try:
                choice = int(input("Enter the number of the contact to delete: ").strip())
                if 1 <= choice <= len(found_contacts):
                    self.contacts.remove(found_contacts[choice - 1])
                    self.file_manager.write_contacts(self.contacts)
                    print(f"Contact {name} deleted successfully.")
                else:
                    print("Invalid choice. No contact deleted.")
            except ValueError:
                print("Invalid input. No contact deleted.")