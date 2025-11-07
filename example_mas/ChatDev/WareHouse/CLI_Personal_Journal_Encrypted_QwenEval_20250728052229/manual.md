# Personal Journal CLI Application

## Introduction

The Personal Journal CLI Application is a command-line interface tool designed to help you maintain a secure and timestamped personal journal. Entries are encrypted with a user-provided password and stored locally in a file. This ensures that your journal entries are private and secure.

## Main Functions

1. **Add Entry**: Users can add new journal entries. Each entry is timestamped and encrypted.
2. **View Entries**: Users can view all their journal entries. Entries are decrypted and displayed in a readable format.
3. **Exit**: Users can exit the application, and all changes are saved automatically.

## Quick Install

To install the Personal Journal CLI Application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can install the required dependencies using pip. Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

This command will install the `cryptography` library, which is used for encryption and decryption.

## 📖 Documentation

### Running the Application

To run the Personal Journal CLI Application, navigate to the directory where the `main.py` file is located and execute the following command:

```bash
python main.py
```

### Using the Application

1. **Enter Password**: When you first run the application, you will be prompted to enter a password. This password will be used to encrypt and decrypt your journal entries. Make sure to remember this password, as you will need it to access your entries.
2. **Add Entry**: To add a new entry, select option `1` from the main menu. Enter your journal entry when prompted. The entry will be timestamped and encrypted.
3. **View Entries**: To view your journal entries, select option `2` from the main menu. All entries will be decrypted and displayed in a readable format.
4. **Exit**: To exit the application, select option `3` from the main menu. All changes will be saved automatically.

### Example Usage

Here is an example of how to use the Personal Journal CLI Application:

```bash
$ python main.py
Enter your password to encrypt/decrypt entries: ********

Personal Journal CLI
1. Add Entry
2. View Entries
3. Exit
Choose an option: 1
Enter your journal entry: Today was a great day!
Entry added successfully.

Personal Journal CLI
1. Add Entry
2. View Entries
3. Exit
Choose an option: 2

Timestamp: 2023-10-01 12:34:56.789012
Content: Today was a great day!

Personal Journal CLI
1. Add Entry
2. View Entries
3. Exit
Choose an option: 3
Exiting...
```

## 🛠️ Troubleshooting

If you encounter any issues while using the Personal Journal CLI Application, please ensure that you have installed the required dependencies and that you are using the correct password to encrypt and decrypt your entries.

If you continue to experience issues, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

## 📝 License

The Personal Journal CLI Application is released under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This manual should provide users with a comprehensive understanding of how to use the Personal Journal CLI Application, including installation, main functions, and troubleshooting tips.