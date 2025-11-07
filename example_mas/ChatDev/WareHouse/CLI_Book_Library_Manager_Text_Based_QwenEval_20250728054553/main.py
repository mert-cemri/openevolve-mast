main.py
'''
Main entry point for the CLI book library manager.
Handles user interactions and manages the library operations.
'''
from library import Library
def main():
    lib = Library()
    while True:
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search by Title")
        print("4. Search by Author")
        print("5. Mark Book as Read/Unread")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            lib.add_book(title, author, isbn)
        elif choice == '2':
            lib.list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            lib.search_by_title(title)
        elif choice == '4':
            author = input("Enter book author to search: ")
            lib.search_by_author(author)
        elif choice == '5':
            isbn = input("Enter book ISBN to mark as read/unread: ")
            status = input("Enter 'read' or 'unread': ")
            lib.mark_book_status(isbn, status)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()