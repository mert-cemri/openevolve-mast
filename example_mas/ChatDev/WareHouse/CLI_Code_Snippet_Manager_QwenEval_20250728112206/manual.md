# CLI Code Snippet Manager

## Overview

The CLI Code Snippet Manager is a powerful tool designed to help developers save, categorize, search, and retrieve frequently used code snippets. It allows users to store snippets in local files, making it easy to access and manage code across different projects and languages.

## Quick Install

To install the CLI Code Snippet Manager, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and install the required dependencies using pip:

```bash
git clone https://github.com/ChatDev/cli-code-snippet-manager.git
cd cli-code-snippet-manager
pip install -r requirements.txt
```

Alternatively, you can install the package directly from PyPI:

```bash
pip install cli-code-snippet-manager
```

## Main Functions

### 1. Add Snippet

To add a new code snippet, use the `Add Snippet` option in the CLI interface. You will be prompted to enter the language, code, and an optional description for the snippet.

### 2. Get Snippets by Language

To retrieve all snippets for a specific language, use the `Get Snippets by Language` option. Enter the language you are interested in, and the manager will display all snippets associated with that language.

### 3. Search Snippets

To search for snippets containing a specific query in their code or description, use the `Search Snippets` option. Enter your search query, and the manager will display all snippets that match the query.

### 4. List All Snippets

To view all snippets stored in the manager, use the `List All Snippets` option. This will display all snippets along with their language, code, and description.

## How to Use

### Running the CLI Interface

To start the CLI interface, run the following command in your terminal:

```bash
python main.py
```

This will display the main menu, where you can choose from the available options to manage your code snippets.

### Example Workflow

1. **Add a Snippet:**

   ```bash
   CLI Code Snippet Manager
   1. Add Snippet
   2. Get Snippets by Language
   3. Search Snippets
   4. List All Snippets
   5. Exit
   Enter your choice: 1
   Enter the language: Python
   Enter the code: print("Hello, World!")
   Enter the description (optional): A simple print statement
   Snippet added successfully.
   ```

2. **Get Snippets by Language:**

   ```bash
   Enter your choice: 2
   Enter the language: Python

   Snippet 1:
   Language: Python
   Code: print("Hello, World!")
   Description: A simple print statement
   ```

3. **Search Snippets:**

   ```bash
   Enter your choice: 3
   Enter the search query: print

   Snippet 1:
   Language: Python
   Code: print("Hello, World!")
   Description: A simple print statement
   ```

4. **List All Snippets:**

   ```bash
   Enter your choice: 4

   Snippet 1:
   Language: Python
   Code: print("Hello, World!")
   Description: A simple print statement
   ```

5. **Exit:**

   ```bash
   Enter your choice: 5
   ```

## Dependencies

The CLI Code Snippet Manager requires the following dependencies:

- `json`: For handling JSON data.
- `tkinter`: For the GUI interface (optional).

These dependencies are included in the `requirements.txt` file and will be installed automatically when you run `pip install -r requirements.txt`.

## Conclusion

The CLI Code Snippet Manager is a versatile tool for managing your code snippets efficiently. Whether you are a developer working on multiple projects or a student learning new programming languages, this tool can help you save time and stay organized. If you have any questions or need further assistance, feel free to reach out to our support team.

---

This manual provides a comprehensive overview of the CLI Code Snippet Manager, including installation instructions, main functions, and usage examples. It should help users get started with the tool and make the most of its features.