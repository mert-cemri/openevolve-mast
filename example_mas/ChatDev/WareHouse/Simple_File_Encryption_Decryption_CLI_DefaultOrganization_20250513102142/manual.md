```markdown
# File Encryption/Decryption Utility

A command-line and graphical user interface utility for simple file encryption and decryption using the AES symmetric algorithm with a user-provided password.

## Overview

This utility allows users to encrypt and decrypt files using the AES encryption algorithm. It supports both command-line interface (CLI) and graphical user interface (GUI) modes, providing flexibility for different user preferences.

## Main Functions

- **Encrypt a File**: Securely encrypts a file using AES encryption with a user-provided password.
- **Decrypt a File**: Decrypts a previously encrypted file using the correct password.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Quick Install

1. Clone the repository or download the source code.

2. Navigate to the directory containing the source code.

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)

To use the utility in CLI mode, open a terminal and run the following command:

```bash
python main.py <mode> <input_file> <output_file> <password>
```

- `<mode>`: Specify `encrypt` to encrypt a file or `decrypt` to decrypt a file.
- `<input_file>`: Path to the input file.
- `<output_file>`: Path to the output file.
- `<password>`: Password for encryption or decryption.

**Example:**

To encrypt a file:

```bash
python main.py encrypt myfile.txt myfile.enc mypassword
```

To decrypt a file:

```bash
python main.py decrypt myfile.enc myfile.txt mypassword
```

### Graphical User Interface (GUI)

To use the utility in GUI mode, simply run the following command without any arguments:

```bash
python main.py
```

#### GUI Instructions:

1. **Input File**: Click "Browse" to select the file you want to encrypt or decrypt.
2. **Output File**: Click "Browse" to select the destination for the output file.
3. **Password**: Enter the password for encryption or decryption.
4. **Mode**: Select either "Encrypt" or "Decrypt".
5. **Execute**: Click "Execute" to perform the operation.

## Troubleshooting

- Ensure that the correct password is used for decryption; otherwise, the process will fail.
- If running in GUI mode and no display is found, the application will default to CLI mode.

## Documentation

For further details and updates, please refer to the project documentation or contact support.

```
