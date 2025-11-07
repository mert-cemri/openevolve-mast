# File Encryption and Decryption Utility

## Introduction

This utility provides a simple command-line interface (CLI) for encrypting and decrypting files using a symmetric algorithm (AES). The tool takes an input file, an output file, a password, and a mode (encrypt/decrypt) as arguments. It uses AES in GCM mode for encryption and decryption, ensuring both confidentiality and integrity of the data.

## Quick Install

To use this utility, you need to have Python installed on your system. It is recommended to use Python 3.6 or later. You can download Python from [here](https://www.python.org/downloads/).

Once Python is installed, you need to install the `pycryptodome` package, which is used for cryptographic operations. You can install it using pip:

```bash
pip install pycryptodome
```

## 🤔 What is this?

This utility allows you to securely encrypt and decrypt files using a password. The encryption process ensures that the contents of the file are not readable without the correct password. The decryption process reverses the encryption, allowing you to retrieve the original file contents.

## 📖 Documentation

### Main Functions

- **Encrypt File**: Encrypts the contents of an input file and writes the encrypted data to an output file.
- **Decrypt File**: Decrypts the contents of an input file and writes the decrypted data to an output file.

### How to Use

#### Command-Line Interface (CLI)

The utility can be used from the command line. Here is the basic syntax:

```bash
python main.py --mode <encrypt/decrypt> --input <input_file_path> --output <output_file_path> --password <password>
```

- `--mode`: Specifies the mode of operation. It can be either `encrypt` or `decrypt`.
- `--input`: Specifies the path to the input file.
- `--output`: Specifies the path to the output file.
- `--password`: Specifies the password used for encryption or decryption.

#### Examples

1. **Encrypt a File**

   To encrypt a file named `example.txt` and save the encrypted data to `example.enc`, use the following command:

   ```bash
   python main.py --mode encrypt --input example.txt --output example.enc --password mysecretpassword
   ```

2. **Decrypt a File**

   To decrypt a file named `example.enc` and save the decrypted data to `example_decrypted.txt`, use the following command:

   ```bash
   python main.py --mode decrypt --input example.enc --output example_decrypted.txt --password mysecretpassword
   ```

### GUI Interface

In addition to the CLI, this utility also provides a graphical user interface (GUI) for ease of use. To run the GUI, use the following command:

```bash
python gui.py
```

The GUI allows you to select the input and output files, enter the password, and choose the mode of operation (encrypt/decrypt) using a simple and intuitive interface.

## 🛠️ Dependencies

- `pycryptodome`: A self-contained Python package of low-level cryptographic primitives.

## 🚀 Getting Started

1. **Install Python**: Ensure you have Python 3.6 or later installed.
2. **Install Dependencies**: Install the `pycryptodome` package using pip.
3. **Run the Utility**: Use the CLI or GUI to encrypt and decrypt files.

## 📝 Notes

- **Security**: The security of the encrypted files depends on the strength of the password. It is recommended to use a strong, unique password.
- **File Integrity**: The utility ensures the integrity of the encrypted files using AES in GCM mode. Any modification to the encrypted file will result in a decryption error.

## 🙋‍♂️ Support

For any issues or questions, please contact us at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual should provide a comprehensive guide for users to install, configure, and use the file encryption and decryption utility.