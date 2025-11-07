# CLI Thesaurus Lookup Tool

Welcome to the CLI Thesaurus Lookup Tool! This tool allows you to quickly find synonyms and antonyms for any word using a local, offline thesaurus file. It's a simple command-line interface application designed to be efficient and easy to use.

## Main Functions

- **Synonym Lookup**: Enter a word, and the tool will display a list of synonyms if available.
- **Antonym Lookup**: Enter a word, and the tool will display a list of antonyms if available.
- **Offline Access**: The tool uses a local thesaurus file, so no internet connection is required.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder.
   ```bash
   cd <project-directory>
   ```

3. **No External Dependencies**: This project does not require any external Python packages, so you can skip the installation of dependencies.

## How to Use

1. **Run the Application**: Execute the main application file using Python.
   ```bash
   python main.py
   ```

2. **Enter a Word**: When prompted, type a word to look up its synonyms and antonyms. For example:
   ```
   Enter a word (or type 'exit' to quit): happy
   ```

3. **View Results**: The tool will display synonyms and antonyms for the entered word if available.
   ```
   Synonyms for 'happy': joyful, content
   Antonyms for 'happy': sad, unhappy
   ```

4. **Exit the Application**: Type 'exit' to quit the application.
   ```
   Enter a word (or type 'exit' to quit): exit
   ```

## Thesaurus File Format

The `thesaurus.txt` file should be formatted as follows:
- Each line represents a word entry.
- Format: `word:synonym1,synonym2:antonym1,antonym2`
- Example:
  ```
  happy:joyful,content:sad,unhappy
  sad:unhappy,down:happy,joyful
  ```

Ensure that the `thesaurus.txt` file is located in the same directory as the Python scripts for the application to function correctly.

Enjoy using the CLI Thesaurus Lookup Tool to enhance your vocabulary and writing!