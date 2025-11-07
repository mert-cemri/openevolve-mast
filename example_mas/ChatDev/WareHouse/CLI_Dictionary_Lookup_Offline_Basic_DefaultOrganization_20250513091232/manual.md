```markdown
# CLI Dictionary Lookup Tool

A simple command-line interface (CLI) tool for looking up word definitions using a local, offline dictionary file.

## Overview

The CLI Dictionary Lookup Tool allows users to input a word and receive its definition from a locally stored dictionary file. This tool is designed to work offline, ensuring that you can access word definitions without an internet connection.

## Main Functions

- **Load Dictionary**: Reads a dictionary file formatted with `word:definition` pairs and loads it into memory.
- **Lookup Word**: Prompts the user to enter a word and displays its definition if found in the dictionary.
- **Exit**: Allows the user to exit the application by typing 'exit'.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the CLI Dictionary Lookup Tool.

2. **No External Dependencies**: This tool does not require any external Python packages, so you don't need to install any additional dependencies.

3. **Prepare the Dictionary File**: Ensure you have a dictionary file named `dictionary.txt` in the same directory as the `main.py` script. The file should be formatted with each line containing a `word:definition` pair.

## Usage

1. **Run the Application**: Open a terminal or command prompt and navigate to the directory containing `main.py`. Execute the following command:

   ```bash
   python main.py
   ```

2. **Enter a Word**: When prompted, type the word you want to look up and press Enter.

3. **View the Definition**: The tool will display the definition of the word if it exists in the dictionary. If the word is not found, it will inform you that the word is not in the dictionary.

4. **Exit the Application**: Type 'exit' and press Enter to close the application.

## Example

```bash
$ python main.py
Enter word (or type 'exit' to quit): apple
Definition: A fruit that is typically round, red or green, and crisp.

Enter word (or type 'exit' to quit): banana
Definition: A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.

Enter word (or type 'exit' to quit): exit
```

## Additional Information

- **Error Handling**: The tool includes basic error handling for file not found errors and improperly formatted lines in the dictionary file.
- **Customization**: You can customize the dictionary file by adding or modifying `word:definition` pairs as needed.

Enjoy using the CLI Dictionary Lookup Tool for quick and easy access to word definitions offline!
```