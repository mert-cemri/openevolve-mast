book.py
'''
Book class to represent a book in the library.
Contains attributes for title, author, ISBN, and read status.
'''
class Book:
    def __init__(self, title, author, isbn, read=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.read = read
    def __str__(self):
        read_status = "Read" if self.read else "Unread"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {read_status}"