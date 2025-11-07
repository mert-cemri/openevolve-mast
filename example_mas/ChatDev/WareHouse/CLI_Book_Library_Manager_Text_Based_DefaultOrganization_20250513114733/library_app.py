'''
Handles the GUI for the library manager using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from library_manager import LibraryManager
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Manager")
        self.manager = LibraryManager()
        self.title_label = tk.Label(root, text="Title")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)
        self.author_label = tk.Label(root, text="Author")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)
        self.isbn_label = tk.Label(root, text="ISBN")
        self.isbn_label.grid(row=2, column=0)
        self.isbn_entry = tk.Entry(root)
        self.isbn_entry.grid(row=2, column=1)
        self.add_button = tk.Button(root, text="Add Book", command=self.add_book_gui)
        self.add_button.grid(row=3, column=0, columnspan=2)
        self.list_button = tk.Button(root, text="List Books", command=self.list_books_gui)
        self.list_button.grid(row=4, column=0, columnspan=2)
        self.search_label = tk.Label(root, text="Search")
        self.search_label.grid(row=5, column=0)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=5, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_books_gui)
        self.search_button.grid(row=6, column=0, columnspan=2)
    def add_book_gui(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        if title and author and isbn:
            self.manager.add_book(title, author, isbn)
            messagebox.showinfo("Success", "Book added successfully!")
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.isbn_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")
    def list_books_gui(self):
        books = self.manager.list_books()
        book_list = "\n".join([f"{book.title} by {book.author} (ISBN: {book.isbn}) - {'Read' if book.read else 'Unread'}" for book in books])
        messagebox.showinfo("Book List", book_list if book_list else "No books in the library.")
    def search_books_gui(self):
        query = self.search_entry.get()
        if query:
            books = self.manager.search_books(query)
            book_list = "\n".join([f"{book.title} by {book.author} (ISBN: {book.isbn}) - {'Read' if book.read else 'Unread'}" for book in books])
            messagebox.showinfo("Search Results", book_list if book_list else "No matching books found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a search query.")