# Checksum Utility CLI

A command-line interface (CLI) utility to calculate and display the MD5 and SHA256 checksums of a given file. This utility is designed to be simple, efficient, and easy to use for verifying file integrity.

## Quick Install

To install the Checksum Utility CLI, you need to have Python installed on your system. The utility does not require any third-party dependencies.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ChatDev/checksum-utility-cli.git
   cd checksum-utility-cli
   ```

2. **Install the utility:**

   Since there are no external dependencies, you can simply run the script directly. However, if you prefer to install it as a package, you can use:

   ```bash
   pip install .
   ```

## 🤔 What is this?

Checksums are unique digital fingerprints of a file. They are used to verify the integrity of files, ensuring that the file has not been altered or corrupted during transmission or storage. The Checksum Utility CLI calculates and displays the MD5 and SHA256 checksums of a given file, allowing you to verify the file's integrity easily.

## 📖 Documentation

### Main Functions

- **Calculate MD5 Checksum:** Computes the MD5 checksum of the specified file.
- **Calculate SHA256 Checksum:** Computes the SHA256 checksum of the specified file.
- **Error Handling:** Provides informative error messages for common issues such as file not found or permission denied.

### How to Use

1. **Open a terminal or command prompt.**
2. **Navigate to the directory containing the `main.py` script.**
3. **Run the utility with the file path as an argument:**

   ```bash
   python main.py <file_path>
   ```

   Replace `<file_path>` with the actual path to the file you want to check.

#### Example

```bash
python main.py /path/to/your/file.txt
```

**Output:**

```
MD5: 3e25960a79dbc69b674cd4ec67a72c62
SHA256: 2c26b46b68ffc68ff99b453c1d30413413422384e7f708a0d63542a2194677b0
```

### Error Messages

- **File Not Found:**

  ```
  Error: The file '/path/to/your/file.txt' was not found.
  ```

- **Permission Denied:**

  ```
  Error: Permission denied when accessing the file '/path/to/your/file.txt'.
  ```

- **Unexpected Error:**

  ```
  An unexpected error occurred: <error_description>
  ```

### Additional Notes

- **Chunk Size:** The utility reads the file in chunks of 4096 bytes to efficiently handle large files without consuming excessive memory.
- **Cross-Platform:** The utility is designed to work on any platform that supports Python, including Windows, macOS, and Linux.

## 🛠️ Development

If you are interested in contributing to the development of the Checksum Utility CLI, you can find the source code on [GitHub](https://github.com/ChatDev/checksum-utility-cli).

### Contributing

1. **Fork the repository.**
2. **Create a new branch for your feature or bug fix.**
3. **Make your changes and commit them.**
4. **Push your changes to your fork.**
5. **Create a pull request to the main repository.**

We welcome contributions from the community to improve and expand the functionality of the Checksum Utility CLI.

---

This manual provides a comprehensive overview of the Checksum Utility CLI, including installation instructions, usage examples, and error handling. If you have any questions or encounter any issues, please feel free to reach out to our support team or contribute to the project on GitHub.