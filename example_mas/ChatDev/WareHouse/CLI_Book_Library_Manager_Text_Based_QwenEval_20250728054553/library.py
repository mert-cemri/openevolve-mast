library.py
'''
Library class to manage book operations.
Handles adding, listing, searching, and marking books as read/unread.
'''
from book import Book
from storage import Storage
class Library:
    def __init__(self):
        self.storage = Storage()
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.storage.add_book(book)
        print(f"Book '{title}' added successfully.")
    def list_books(self):
        books = self.storage.get_books()
        if not books:
            print("No books in the library.")
        else:
            for book in books:
                print(book)
    def search_by_title(self, title):
        books = self.storage.search_books_by_title(title)
        if not books:
            print(f"No books found with title '{title}'.")
        else:
            for book in books:
                print(book)
    def search_by_author(self, author):
        books = self.storage.search_books_by_author(author)
        if not books:
            print(f"No books found by author '{author}'.")
        else:
            for book in books:
                print(book)
    def mark_book_status(self, isbn, status):
        if status.lower() not in ['read', 'unread']:
            print("Invalid status. Please enter 'read' or 'unread'.")
            return
        self.storage.mark_book_status(isbn, status)
        print(f"Book with ISBN '{isbn}' marked as {status}.")