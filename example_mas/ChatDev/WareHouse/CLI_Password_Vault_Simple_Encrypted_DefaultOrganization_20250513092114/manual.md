```markdown
# Password Vault CLI

A simple command-line interface (CLI) application for securely storing and managing passwords using encryption.

## Overview

The Password Vault CLI application allows users to store website/service names, usernames, and passwords in an encrypted local file. The vault is secured with a master password, which is used to encrypt and decrypt the stored data.

## Main Features

- **Secure Storage**: Encrypts and stores passwords locally using a master password.
- **Add Entries**: Allows users to add new service credentials to the vault.
- **View Entries**: Displays stored credentials in a secure manner.
- **Graphical User Interface (GUI)**: An optional GUI is available for users who prefer a visual interface.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.

### Install Environment Dependencies

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

This will install the `cryptography` library, which is necessary for encryption and decryption operations.

## Usage

### Running the CLI Application

1. **Start the Application**:
   Run the main script to start the CLI application:

   ```bash
   python main.py
   ```

2. **Enter Master Password**:
   You will be prompted to enter a master password. This password is used to encrypt and decrypt your vault.

3. **Choose an Option**:
   - **Add Entry**: Enter the service name, username, and password to add a new entry.
   - **View Entries**: View all stored entries. The service name, username, and password will be displayed.
   - **Exit**: Exit the application.

### Running the GUI Application

For users who prefer a graphical interface, the GUI version can be run as follows:

1. **Start the GUI Application**:
   Run the GUI script:

   ```bash
   python gui.py
   ```

2. **Unlock the Vault**:
   Enter the master password to unlock the vault.

3. **Manage Entries**:
   - **Add Entry**: Use the "Add Entry" button to add new credentials.
   - **View Entries**: Entries will be displayed in a list box.

## Security Considerations

- **Master Password**: Choose a strong master password to ensure the security of your vault.
- **Local Storage**: The vault file is stored locally on your machine. Ensure your device is secure to prevent unauthorized access.

## Documentation

For more detailed documentation and support, please refer to the source code comments and the `vault.py` file, which handles encryption and decryption logic.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the source code.

```
