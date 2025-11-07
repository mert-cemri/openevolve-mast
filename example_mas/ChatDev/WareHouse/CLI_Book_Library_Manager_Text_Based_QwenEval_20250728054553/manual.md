# Book Library Manager CLI

## Overview

The Book Library Manager CLI is a command-line interface application designed to help you manage your personal book library. You can add books, list all books, search for books by title or author, and mark books as read or unread. All data is stored locally on your device.

## Quick Install

To install the Book Library Manager CLI, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and install the required dependencies:

1. Clone the repository:
   ```bash
   git clone https://github.com/ChatDev/BookLibraryManager.git
   cd BookLibraryManager
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Note: Currently, there are no external dependencies required for this project, so `requirements.txt` is empty.

## 📖 Documentation

### Main Functions

1. **Add Book**
   - Command: `1`
   - Description: Add a new book to the library.
   - Steps:
     1. Enter the book title.
     2. Enter the book author.
     3. Enter the book ISBN.

2. **List All Books**
   - Command: `2`
   - Description: List all books in the library.
   - Steps:
     1. Select option `2` from the main menu.

3. **Search by Title**
   - Command: `3`
   - Description: Search for books by title.
   - Steps:
     1. Select option `3` from the main menu.
     2. Enter the book title to search.

4. **Search by Author**
   - Command: `4`
   - Description: Search for books by author.
   - Steps:
     1. Select option `4` from the main menu.
     2. Enter the book author to search.

5. **Mark Book as Read/Unread**
   - Command: `5`
   - Description: Mark a book as read or unread.
   - Steps:
     1. Select option `5` from the main menu.
     2. Enter the book ISBN.
     3. Enter 'read' or 'unread' to update the book status.

6. **Exit**
   - Command: `6`
   - Description: Exit the application.

### How to Use/Play

1. **Start the Application**
   - Run the following command in your terminal:
     ```bash
     python main.py
     ```

2. **Interact with the Application**
   - Follow the on-screen prompts to perform various operations.
   - Use the numbers `1` to `6` to select the desired action.

3. **Data Storage**
   - All book data is stored locally in a file named `books.json`.
   - You can manually edit this file if needed, but it's recommended to use the application to manage your library.

## 🛠️ Development

If you're interested in contributing to the project, you can find the source code on [GitHub](https://github.com/ChatDev/BookLibraryManager).

Feel free to open issues, submit pull requests, or suggest new features.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the Book Library Manager CLI effectively. If you have any specific questions or need further assistance, feel free to reach out!