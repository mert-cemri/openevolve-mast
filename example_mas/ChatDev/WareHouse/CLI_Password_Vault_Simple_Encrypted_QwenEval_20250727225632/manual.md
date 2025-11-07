# Password Vault CLI User Manual

## Overview

The Password Vault CLI is a simple command-line interface application designed to securely store and manage your website/service credentials. It uses a master password to encrypt and decrypt the stored data, ensuring that your sensitive information remains safe.

## Features

- **Add Entry:** Store new website/service credentials.
- **Get Entry:** Retrieve stored credentials for a specific website/service.
- **Remove Entry:** Delete stored credentials for a specific website/service.
- **Save Vault:** Save all changes to the encrypted vault file.
- **Load Vault:** Load the encrypted vault file using the master password.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repository/password-vault-cli.git
   cd password-vault-cli
   ```

2. **Install Dependencies:**

   The project requires the `cryptography` library for encryption and decryption. Install it using pip:

   ```bash
   pip install cryptography
   ```

## Usage

### Starting the Application

To start the Password Vault CLI, run the following command in your terminal:

```bash
python main.py
```

### Main Menu

Upon starting the application, you will be prompted to enter the master password. If the vault file does not exist, it will be created upon saving for the first time.

Once the vault is loaded successfully, you will see the main menu with the following options:

```
Options:
1. Add Entry
2. Get Entry
3. Remove Entry
4. Save Vault
5. Exit
```

### Adding an Entry

To add a new entry, select option `1` from the main menu. You will be prompted to enter the service name, username, and password.

### Getting an Entry

To retrieve an entry, select option `2` from the main menu. You will be prompted to enter the service name. If the entry exists, the username and password will be displayed.

### Removing an Entry

To remove an entry, select option `3` from the main menu. You will be prompted to enter the service name. If the entry exists, it will be deleted from the vault.

### Saving the Vault

To save all changes to the vault file, select option `4` from the main menu. The vault will be encrypted using the master password and saved to the local file.

### Exiting the Application

To exit the application, select option `5` from the main menu. All unsaved changes will be lost.

## Security Considerations

- **Master Password:** Choose a strong and unique master password to protect your vault. Avoid using easily guessable passwords.
- **File Security:** Ensure that the vault file (`vault.dat`) is stored in a secure location and is not accessible to unauthorized users.
- **Backup:** Regularly back up your vault file to prevent data loss.

## Troubleshooting

- **Invalid Master Password:** If you enter an incorrect master password, the vault will not load, and you will be prompted to try again.
- **File Not Found:** If the vault file does not exist, it will be created upon saving for the first time.
- **IO Errors:** If there are issues reading from or writing to the vault file, an error message will be displayed.

## Contributing

We welcome contributions to the Password Vault CLI project. If you have any ideas for improvements or bug fixes, please feel free to submit a pull request.

## License

The Password Vault CLI is open-source software licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This manual provides a comprehensive guide on how to install, use, and manage the Password Vault CLI application. If you have any questions or encounter any issues, please refer to the troubleshooting section or contact the support team.