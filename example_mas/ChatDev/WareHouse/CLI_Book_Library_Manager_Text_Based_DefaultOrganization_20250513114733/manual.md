# Library Manager CLI

Welcome to the Library Manager CLI application! This tool allows you to manage a collection of books through a command-line interface. You can add books, list all books, search for books by title or author, and mark books as read or unread. All data is stored locally in a JSON file.

## Main Features

- **Add Books**: Add new books to your library by specifying the title, author, and ISBN.
- **List Books**: View all books currently in your library, along with their read/unread status.
- **Search Books**: Search for books by title or author.
- **Mark Books as Read/Unread**: Update the read status of books in your library.
- **Data Persistence**: All book data is stored locally in a JSON file, ensuring your library is saved between sessions.

## Installation

### Prerequisites

- Python 3.6 or higher

### Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have Python 3.6 or higher installed on your system.

## Usage

### Running the Application

To start the Library Manager CLI, run the following command in your terminal:

```bash
python main.py
```

### Using the CLI

Once the application is running, you will see a menu with the following options:

1. **Add Book**: Enter the book's title, author, and ISBN to add it to your library.
2. **List Books**: Display all books in your library with their details and read status.
3. **Search Books**: Enter a search query to find books by title or author.
4. **Mark Book as Read**: Enter the ISBN of a book to mark it as read.
5. **Mark Book as Unread**: Enter the ISBN of a book to mark it as unread.
6. **Exit**: Close the application.

### Example Commands

- **Add a Book**: Follow the prompts to enter the book's details.
- **List Books**: Simply select the option to view all books.
- **Search Books**: Enter a keyword related to the title or author.
- **Mark as Read/Unread**: Provide the ISBN of the book you wish to update.

## Data Storage

The application stores all book data in a file named `library.json` in the project directory. This file is automatically updated whenever you add, modify, or remove books.

## Support

For any issues or questions, please contact our support team or visit our documentation page for more information.

Enjoy managing your library with the Library Manager CLI!