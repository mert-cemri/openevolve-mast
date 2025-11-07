# CLI Thesaurus Lookup Tool

## Introduction

The CLI Thesaurus Lookup Tool is a command-line interface application designed to help users find synonyms and antonyms for words using a local, offline thesaurus file. This tool is built with Python and is easy to use, making it a convenient choice for anyone who needs quick access to thesaurus data without an internet connection.

## Main Functions

- **Word Lookup:** Users can input a word to find its synonyms and antonyms.
- **Exit Command:** Users can type 'exit' to quit the application.
- **Error Handling:** The tool handles errors gracefully, such as when the thesaurus file is not found or when a line in the file is malformed.

## Quick Install

To install the CLI Thesaurus Lookup Tool, you need to have Python installed on your system. The tool does not have any external dependencies, so you don't need to install anything else.

1. **Clone the Repository:**

   First, clone the repository from GitHub or download the source code.

   ```bash
   git clone https://github.com/your-repo/cli-thesaurus-lookup-tool.git
   cd cli-thesaurus-lookup-tool
   ```

2. **Run the Tool:**

   Navigate to the directory where `main.py` is located and run the script using Python.

   ```bash
   python main.py
   ```

## 🤔 What is this?

The CLI Thesaurus Lookup Tool is a simple yet powerful application that leverages Python's built-in capabilities for file handling and string manipulation. It reads a thesaurus file, parses the data, and provides a user-friendly interface for looking up synonyms and antonyms.

## 📖 Documentation

### Thesaurus File Format

The thesaurus file (`thesaurus.txt`) should be formatted as follows:

- Each line contains a word, followed by a comma, then a semicolon-separated list of synonyms, another comma, and a semicolon-separated list of antonyms.
- Example:

  ```txt
  happy,joyful;cheerful;content;delighted,unhappy;sad
  sad,unhappy;sorrowful;melancholy;dejected,happy;joyful
  ```

### Using the Tool

1. **Start the Tool:**

   Run the `main.py` script to start the CLI Thesaurus Lookup Tool.

   ```bash
   python main.py
   ```

2. **Lookup a Word:**

   Enter a word when prompted to see its synonyms and antonyms.

   ```bash
   Enter a word to look up (or 'exit' to quit): happy
   Word: happy
   Synonyms: joyful, cheerful, content, delighted
   Antonyms: unhappy, sad
   ```

3. **Exit the Tool:**

   Type 'exit' to quit the application.

   ```bash
   Enter a word to look up (or 'exit' to quit): exit
   Goodbye!
   ```

### Error Handling

- **File Not Found:**

  If the thesaurus file (`thesaurus.txt`) is not found, the tool will display an error message and exit.

  ```bash
  Error: The thesaurus file 'thesaurus.txt' was not found.
  ```

- **Malformed Line:**

  If a line in the thesaurus file is malformed, the tool will print a warning and skip that line.

  ```bash
  Warning: Skipping malformed line in thesaurus file: malformed,line
  ```

## Conclusion

The CLI Thesaurus Lookup Tool is a simple yet effective application for finding synonyms and antonyms using a local thesaurus file. It is easy to install and use, making it a convenient choice for anyone who needs quick access to thesaurus data without an internet connection. If you have any questions or need further assistance, feel free to contact us.

---

This manual should provide a comprehensive guide for users to understand and use the CLI Thesaurus Lookup Tool effectively.