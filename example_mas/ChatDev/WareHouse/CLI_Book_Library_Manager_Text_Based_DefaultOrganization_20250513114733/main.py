'''
Main entry point for the CLI book library manager application.
'''
from library_manager import LibraryManager
def main():
    manager = LibraryManager()
    while True:
        print("\nLibrary Manager CLI")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Mark Book as Read")
        print("5. Mark Book as Unread")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            manager.add_book(title, author, isbn)
            print("Book added successfully!")
        elif choice == '2':
            books = manager.list_books()
            if books:
                for book in books:
                    print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {'Read' if book.read else 'Unread'}")
            else:
                print("No books in the library.")
        elif choice == '3':
            query = input("Enter search query (title/author): ")
            books = manager.search_books(query)
            if books:
                for book in books:
                    print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {'Read' if book.read else 'Unread'}")
            else:
                print("No matching books found.")
        elif choice == '4':
            isbn = input("Enter ISBN of the book to mark as read: ")
            if manager.mark_book_as_read(isbn):
                print("Book marked as read.")
            else:
                print("Book not found.")
        elif choice == '5':
            isbn = input("Enter ISBN of the book to mark as unread: ")
            if manager.mark_book_as_unread(isbn):
                print("Book marked as unread.")
            else:
                print("Book not found.")
        elif choice == '6':
            print("Exiting the Library Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()