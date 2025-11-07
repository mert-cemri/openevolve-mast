'''
Manages the collection of books and handles data storage.
'''
import json
from book import Book
class LibraryManager:
    def __init__(self, data_file='library.json'):
        self.data_file = data_file
        self.books = []
        self.load_data()
    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                books_data = json.load(file)
                for book_data in books_data:
                    book = Book(book_data['title'], book_data['author'], book_data['isbn'])
                    book.read = book_data['read']
                    self.books.append(book)
        except FileNotFoundError:
            self.books = []
    def save_data(self):
        with open(self.data_file, 'w') as file:
            books_data = [{'title': book.title, 'author': book.author, 'isbn': book.isbn, 'read': book.read} for book in self.books]
            json.dump(books_data, file, indent=4)
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_data()
    def list_books(self):
        return self.books
    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
    def mark_book_as_read(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.mark_as_read()
                self.save_data()
                return True
        return False
    def mark_book_as_unread(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.mark_as_unread()
                self.save_data()
                return True
        return False