'''
Defines the FileManager class which handles reading from and writing to a CSV file.
'''
import csv
class FileManager:
    def __init__(self, filename):
        '''
        Initializes the FileManager with the specified filename.
        '''
        self.filename = filename
    def read_contacts(self):
        '''
        Reads contacts from a CSV file and returns a list of dictionaries.
        Each dictionary represents a contact with keys 'name', 'phone', and 'email'.
        If the file does not exist, it returns an empty list.
        '''
        contacts = []
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contacts.append(row)
        except FileNotFoundError:
            pass
        return contacts
    def write_contacts(self, contacts):
        '''
        Writes a list of Contact objects to a CSV file.
        Each contact is represented as a dictionary with keys 'name', 'phone', and 'email'.
        '''
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['name', 'phone', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in contacts:
                writer.writerow({'name': contact.name, 'phone': contact.phone, 'email': contact.email})