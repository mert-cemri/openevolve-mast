'''
Defines the Library class for managing a collection of books.
'''
from book import Book
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        return self.books
    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
    def get_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None