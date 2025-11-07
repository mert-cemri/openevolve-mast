'''
Defines the Book class representing a book in the library.
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
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Read' if self.read else 'Unread'}"