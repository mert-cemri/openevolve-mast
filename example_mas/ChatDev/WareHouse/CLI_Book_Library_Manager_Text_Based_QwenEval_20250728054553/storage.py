storage.py
'''
Storage class to handle local storage of books.
Uses a simple list to store books and provides methods to add, retrieve, and update books.
'''
import json
import os
class Storage:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self.load_books()
    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Book(**data) for data in json.load(file)]
        return []
    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)
    def add_book(self, book):
        self.books.append(book)
        self.save_books()
    def get_books(self):
        return self.books
    def search_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    def search_books_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]
    def mark_book_status(self, isbn, status):
        for book in self.books:
            if book.isbn == isbn:
                book.read = (status.lower() == 'read')
                self.save_books()
                return
        print(f"No book found with ISBN '{isbn}'.")