```markdown
# CLI Book Library Manager

A command-line interface (CLI) application for managing a personal book library. Users can add books, list all books, search by title or author, and mark books as read or unread. The library data is stored locally in a JSON file.

## Quick Install

To set up the environment and install the necessary dependencies, ensure you have Python 3.6 or higher installed. You can check your Python version by running:

```bash
python --version
```

### Installing Dependencies

1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.
3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The CLI Book Library Manager is a simple yet powerful tool for managing your personal book collection. It allows you to:

- **Add Books**: Enter the title, author, and ISBN to add a new book to your library.
- **List Books**: View all the books currently in your library.
- **Search Books**: Find books by searching for a title or author.
- **Mark Books as Read/Unread**: Keep track of which books you've read.

## 📖 How to Use

### Running the Application

To start the application, run the following command in your terminal:

```bash
python main.py
```

### Main Functions

1. **Add Book**: 
   - Select option 1 from the menu.
   - Enter the book's title, author, and ISBN when prompted.
   - The book will be added to your library.

2. **List Books**: 
   - Select option 2 from the menu.
   - All books in your library will be displayed with their read/unread status.

3. **Search Books**: 
   - Select option 3 from the menu.
   - Enter a search query (title or author).
   - Matching books will be displayed.

4. **Mark Book as Read/Unread**: 
   - Select option 4 from the menu.
   - Enter the ISBN of the book you wish to mark.
   - The book's status will toggle between read and unread.

5. **Exit**: 
   - Select option 5 to save your library data and exit the application.

### Data Storage

The library data is stored locally in a file named `library_data.json`. This file is automatically updated whenever you add, remove, or modify books in your library.

## 📖 Documentation

For further documentation and support, please refer to the source code comments and docstrings. Each module and class is documented to help you understand the internal workings of the application.

```