```markdown
# Contact Book CLI

A simple command-line interface (CLI) application for managing your contacts. This application allows you to add, view, search, and delete contacts, storing them in a CSV file for persistence.

## Main Functions

1. **Add Contact**: Input a new contact's name, phone number, and email to add them to your contact list.
2. **View Contacts**: Display all contacts currently stored in the contact book.
3. **Search Contact**: Find a contact by name.
4. **Delete Contact**: Remove a contact from the contact book by name.
5. **Exit**: Close the application.

## Quick Install

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: Download the source code from the repository.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Environment**: Ensure you have the required Python version.
   ```bash
   python --version
   ```

3. **Install Dependencies**: Install the necessary dependencies using pip.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Application**: Execute the main script to start the CLI application.
   ```bash
   python main.py
   ```

2. **Navigate the Menu**: Use the menu options to interact with your contact book:
   - Press `1` to add a new contact.
   - Press `2` to view all contacts.
   - Press `3` to search for a contact by name.
   - Press `4` to delete a contact by name.
   - Press `5` to exit the application.

3. **Follow Prompts**: The application will prompt you for necessary inputs (e.g., name, phone, email) when required.

## Notes

- Contacts are stored in a `contacts.csv` file in the same directory as the application.
- Ensure the CSV file is not open in another program while using the application to avoid file access issues.
- The application is designed to be simple and straightforward, focusing on essential contact management features.

## Troubleshooting

- **File Not Found Error**: If the `contacts.csv` file is missing, the application will create a new one upon saving contacts.
- **Invalid Input**: Ensure all fields are filled when adding a contact. The application will prompt you to correct any missing information.

For further assistance, please contact our support team.
```
