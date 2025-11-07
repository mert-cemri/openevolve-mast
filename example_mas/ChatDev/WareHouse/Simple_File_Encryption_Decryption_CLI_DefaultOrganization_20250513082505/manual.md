# File Encryptor CLI Utility

A command-line interface (CLI) utility for simple file encryption and decryption using a symmetric algorithm (AES) with a user-provided password.

## Introduction

The File Encryptor CLI Utility is designed to provide users with a straightforward method to encrypt and decrypt files using the AES encryption algorithm. This tool ensures that your sensitive data remains secure and accessible only to those with the correct password.

## Main Functions

- **Encrypt Files**: Secure your files by encrypting them with a password.
- **Decrypt Files**: Access your encrypted files by decrypting them with the same password used for encryption.

## Installation

### Environment Setup

To use the File Encryptor CLI Utility, you need to have Python installed on your system. Additionally, you'll need to install the required dependencies.

### Install Dependencies

1. **Using pip**: 
   Open your terminal or command prompt and run the following command to install the necessary Python package:

   ```bash
   pip install pycryptodome==3.18.0
   ```

2. **Using requirements.txt**:
   Alternatively, you can install the dependencies listed in the `requirements.txt` file by running:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface

The CLI utility can be used to encrypt or decrypt files by providing the necessary arguments.

#### Basic Command Structure

```bash
python main.py <mode> <input_file> <output_file> <password>
```

- `<mode>`: Specify `encrypt` to encrypt a file or `decrypt` to decrypt a file.
- `<input_file>`: Path to the input file you want to encrypt or decrypt.
- `<output_file>`: Path where the output file will be saved.
- `<password>`: Password used for encryption or decryption. Ensure it meets the password requirements.

#### Example Commands

- **Encrypt a File**:

  ```bash
  python main.py encrypt path/to/input.txt path/to/encrypted_output.txt YourPassword123!
  ```

- **Decrypt a File**:

  ```bash
  python main.py decrypt path/to/encrypted_output.txt path/to/decrypted_output.txt YourPassword123!
  ```

### Password Requirements

To ensure security, the password must meet the following criteria:

- At least 8 characters long
- Contains at least one digit
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one special character (e.g., `!@#$%^&*()-_+=`)

## Graphical User Interface (Optional)

For users who prefer a graphical interface, a simple GUI is available. To use the GUI, run the following command:

```bash
python gui.py
```

The GUI allows you to select files for encryption or decryption, input your password, and perform the desired operation with ease.

## Conclusion

The File Encryptor CLI Utility is a powerful yet simple tool for securing your files. By following the instructions above, you can easily encrypt and decrypt files to protect your sensitive information. Always remember to use a strong password to ensure the security of your data.