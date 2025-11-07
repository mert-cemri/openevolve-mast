```markdown
# CLI Dictionary Lookup Tool

Welcome to the CLI Dictionary Lookup Tool! This tool allows you to look up definitions of words using a local, offline dictionary file. It is a simple command-line interface (CLI) application written in Python.

## Main Functions

The CLI Dictionary Lookup Tool provides the following main functions:

- **Load Dictionary**: Reads a local dictionary file in the format `word:definition` and loads it into memory.
- **Word Lookup**: Allows users to input a word and retrieves its definition from the loaded dictionary.
- **Exit Option**: Users can exit the lookup tool by typing 'exit'.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: Download or clone the project files to your local machine.

2. **No External Dependencies**: This project does not require any external Python packages, so you do not need to install additional dependencies.

## Usage

1. **Prepare the Dictionary File**: Ensure you have a dictionary file named `dictionary.txt` in the same directory as `main.py`. The file should contain entries in the format `word:definition`, each on a new line.

2. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the application using the command:
     ```
     python main.py
     ```

3. **Lookup Words**:
   - Once the application is running, you will be prompted to enter a word.
   - Type the word you want to look up and press Enter.
   - The tool will display the definition if the word is found in the dictionary.
   - If the word is not found, it will notify you that the word is not in the dictionary.

4. **Exit the Application**:
   - To exit the application, type `exit` and press Enter.

## Example

```
Enter a word (or type 'exit' to quit): apple
Definition: A fruit that is typically round, red or green, and crisp.

Enter a word (or type 'exit' to quit): banana
Definition: A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.

Enter a word (or type 'exit' to quit): exit
Exiting the dictionary lookup tool.
```

Enjoy using the CLI Dictionary Lookup Tool for quick and easy word definitions!
```