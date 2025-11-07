# Directory Synchronizer

## Overview

The Directory Synchronizer is a Python application designed to synchronize files from a source directory to a target directory in a one-way manner. It copies new or modified files from the source to the target directory without deleting any files from the target directory if they are removed from the source.

## Quick Install

Since the Directory Synchronizer does not have any external dependencies, you can simply clone the repository or download the source code. However, if you wish to install it in a virtual environment, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ChatDev/Directory-Synchronizer.git
   cd Directory-Synchronizer
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the requirements (if any):**

   ```bash
   pip install -r requirements.txt
   ```

   Note: The `requirements.txt` file is empty as there are no external dependencies required for this project.

## 🤔 What is this?

The Directory Synchronizer is a simple yet powerful tool for developers and system administrators who need to keep files in sync between two directories. It is particularly useful for backup purposes, mirroring data, or synchronizing files across different environments.

## 📖 Documentation

### Main Functions

The main function of the Directory Synchronizer is to copy new or modified files from a source directory to a target directory. It ensures that the target directory is an up-to-date copy of the source directory without removing any files from the target directory if they are deleted from the source.

### How to Use

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Enter the source and target directories:**

   When prompted, enter the full path to the source directory and the target directory.

   ```bash
   Enter the source directory: /path/to/source
   Enter the target directory: /path/to/target
   ```

3. **Wait for the synchronization to complete:**

   The application will scan the source directory, compare the files with the target directory, and copy any new or modified files to the target directory. It will also log the synchronization process in a file named `sync.log`.

### Error Handling

The Directory Synchronizer includes basic error handling to manage common issues such as permission errors and file not found errors. If an error occurs, it will be logged in the `sync.log` file with a detailed error message.

### Logging

The application uses Python's built-in `logging` module to log the synchronization process. The log file, `sync.log`, will be created in the same directory as the `main.py` file. You can view this file to monitor the synchronization process and troubleshoot any issues.

## 🛠️ Troubleshooting

If you encounter any issues while using the Directory Synchronizer, please check the `sync.log` file for detailed error messages. If you need further assistance, please contact the support team at support@chatdev.com.

## 📝 License

The Directory Synchronizer is released under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This manual should provide a comprehensive guide for users to understand and use the Directory Synchronizer effectively. If you have any further questions or need additional assistance, feel free to ask.