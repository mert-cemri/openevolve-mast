'''
Manages the CLI and user interactions for the library application.
'''
from library import Library
from book import Book
from data_handler import DataHandler
class LibraryManager:
    def __init__(self):
        self.library = Library()
        self.data_handler = DataHandler('library_data.json')
        self.library.books = self.data_handler.load_data()
    def run(self):
        while True:
            print("\nBook Library Manager")
            print("1. Add Book")
            print("2. List Books")
            print("3. Search Books")
            print("4. Mark Book as Read/Unread")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_book_cli()
            elif choice == '2':
                self.list_books_cli()
            elif choice == '3':
                self.search_books_cli()
            elif choice == '4':
                self.mark_book_cli()
            elif choice == '5':
                self.data_handler.save_data(self.library.books)
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    def add_book_cli(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        if title and author and isbn:
            book = Book(title, author, isbn)
            self.library.add_book(book)
            print("Book added successfully!")
        else:
            print("Please fill all fields.")
    def list_books_cli(self):
        books = self.library.list_books()
        if books:
            for book in books:
                print(book)
        else:
            print("No books in the library.")
    def search_books_cli(self):
        query = input("Enter search query: ")
        results = self.library.search_books(query)
        if results:
            for book in results:
                print(book)
        else:
            print("No matching books found.")
    def mark_book_cli(self):
        isbn = input("Enter ISBN to mark: ")
        book = self.library.get_book(isbn)
        if book:
            if book.read:
                book.mark_as_unread()
                print(f"Marked '{book.title}' as unread.")
            else:
                book.mark_as_read()
                print(f"Marked '{book.title}' as read.")
        else:
            print("Book not found.")