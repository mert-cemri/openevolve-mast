# CLI Contact Book User Manual

## Introduction

The CLI Contact Book is a simple command-line application that allows you to manage your contacts efficiently. You can add, view, search, and delete contacts, with each contact having a name, phone number, and email address. Contacts are stored in a CSV file for persistence.

## Features

- **Add Contact:** Add a new contact with a name, phone number, and email.
- **View Contacts:** Display all contacts stored in the contact book.
- **Search Contact:** Search for a contact by name.
- **Delete Contact:** Remove a contact from the contact book by name.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository:**

   If you have `git` installed, you can clone the repository using the following command:

   ```bash
   git clone https://github.com/your-repo/cli-contact-book.git
   cd cli-contact-book
   ```

   If you don't have `git`, you can download the zip file from the repository and extract it.

2. **Install Dependencies:**

   This project has no external dependencies other than Python's built-in libraries. However, if you have a `requirements.txt` file, you can install dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

   For this project, the `requirements.txt` file is empty, but it's a good practice to include it for future scalability.

## Usage

### Running the Application

To start the CLI Contact Book application, run the following command in your terminal:

```bash
python main.py
```

### Main Menu

Upon running the application, you will be presented with a main menu:

```
Contact Book
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice:
```

### Adding a Contact

To add a new contact, select option `1` and provide the required information:

```
Enter name: John Doe
Enter phone number: 123-456-7890
Enter email: john.doe@example.com
```

### Viewing Contacts

To view all contacts, select option `2`. The application will display all stored contacts:

```
Name: John Doe, Phone: 123-456-7890, Email: john.doe@example.com
Name: Jane Smith, Phone: 987-654-3210, Email: jane.smith@example.com
```

### Searching for a Contact

To search for a contact by name, select option `3` and enter the name:

```
Enter name to search: John Doe
Found 1 contact(s) with name john doe:
1. Name: John Doe, Phone: 123-456-7890, Email: john.doe@example.com
```

### Deleting a Contact

To delete a contact by name, select option `4` and enter the name. If multiple contacts with the same name are found, you will be prompted to choose which one to delete:

```
Enter name to delete: John Doe
Found 1 contact(s) with name john doe:
1. Name: John Doe, Phone: 123-456-7890, Email: john.doe@example.com
Enter the number of the contact to delete: 1
Contact john doe deleted successfully.
```

### Exiting the Application

To exit the application, select option `5`.

## File Storage

All contacts are stored in a CSV file named `contacts.csv` in the same directory as the application. This file is automatically created and managed by the application.

## Conclusion

The CLI Contact Book is a simple yet powerful tool for managing your contacts from the command line. With its intuitive interface and basic functionalities, you can easily keep track of your contacts without the need for a graphical user interface.

If you have any suggestions or encounter any issues, feel free to reach out to the development team.

---

This manual should provide a clear and comprehensive guide for users to understand and use the CLI Contact Book application effectively.