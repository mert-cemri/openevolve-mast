'''
Defines the Contact class which represents a contact with name, phone number, and email.
'''
class Contact:
    def __init__(self, name, phone, email):
        '''
        Initializes a new Contact with the given name, phone number, and email.
        '''
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        '''
        Returns a string representation of the Contact.
        '''
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"