'''
Defines the Book class to represent a book in the library.
'''
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.read = False
    def mark_as_read(self):
        self.read = True
    def mark_as_unread(self):
        self.read = False