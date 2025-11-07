# ChatDev Simple CLI Spell Checker

## Introduction

Welcome to the ChatDev Simple CLI Spell Checker! This application is designed to help you identify potential misspellings in your text files or string inputs by checking them against a local dictionary file. The tool is built using Python and is easy to use via the command line interface (CLI).

## Main Functions

1. **Load Dictionary**: The application loads a dictionary from a local file (`dictionary.txt`) to use as a reference for spell checking.
2. **Check Words**: It checks individual words against the dictionary to determine if they are spelled correctly.
3. **Check Text**: It processes entire blocks of text, identifying and listing any words that are not found in the dictionary.
4. **CLI Interface**: The tool provides a simple command line interface to input text files or directly type text for spell checking.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository**: If you haven't already, clone the repository to your local machine.
   ```bash
   git clone https://github.com/ChatDev/spell-checker.git
   cd spell-checker
   ```

2. **Install Dependencies**: This project currently has no external dependencies, so you don't need to install anything from `requirements.txt`. However, if you have a `requirements.txt` file in the future, you can install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Spell Checker

You can run the spell checker in two ways: by providing a text file or by entering text directly via the command line.

#### Option 1: Check a Text File

1. Ensure you have a text file ready for spell checking.
2. Run the application with the file path as an argument:
   ```bash
   python main.py path/to/your/textfile.txt
   ```

#### Option 2: Enter Text Directly

1. Run the application without any arguments:
   ```bash
   python main.py
   ```
2. Enter the text you want to check when prompted:
   ```
   Enter text to check for spelling: This is a smple text with a misspelled wrd.
   ```
3. The application will output any misspelled words:
   ```
   Misspelled words: smple, wrd
   ```

### Customizing the Dictionary

If you want to use a custom dictionary, simply replace the contents of `dictionary.txt` with your desired words. Ensure each word is on a new line.

## Troubleshooting

- **File Not Found Error**: If you encounter a "File not found" error, double-check the file path you provided.
- **IOError**: If there's an issue reading the file, ensure the file is not corrupted and that you have the necessary permissions to read it.

## Future Enhancements

- **GUI Interface**: A graphical user interface (GUI) is planned for future versions to provide a more user-friendly experience.
- **Advanced Spell Checking**: Incorporating more sophisticated spell checking algorithms to handle context and suggestions.

## Conclusion

Thank you for using the ChatDev Simple CLI Spell Checker! We hope this tool helps you catch those pesky spelling mistakes. If you have any feedback or suggestions, feel free to reach out to us.

---

This manual should provide a comprehensive guide for users to understand and use the ChatDev Simple CLI Spell Checker effectively.