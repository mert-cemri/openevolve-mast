manual.md

```
# Boredom Counter

A simple Python application to count the number of sentences starting with the word "I" in a given string. This application is useful for analyzing text to determine how often sentences begin with a personal pronoun, which can be indicative of a certain writing style or focus.

## Main Functionality

The main function of this software is to count the number of sentences that start with the word "I". Sentences are considered to be delimited by '.', '?' or '!'. The function will return the count of such sentences.

### Example Usage

- Input: "Hello world"
  - Output: 0
- Input: "The sky is blue. The sun is shining. I love this weather"
  - Output: 1

## Installation

This application does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change into the directory containing the `main.py` file:
   ```bash
   cd <directory-name>
   ```

## How to Use

1. **Run the Script**: You can run the script directly from the command line. Navigate to the directory containing `main.py` and execute:
   ```bash
   python main.py
   ```

2. **Modify Input**: To test with different strings, modify the example usage section in the `main.py` file:
   ```python
   if __name__ == "__main__":
       print(is_bored("Your test string here"))
   ```

3. **Interpret Results**: The script will output the number of sentences starting with "I" based on the input string provided.

## Documentation

For further details on how the function works, refer to the docstring within the `main.py` file. It provides a concise explanation of the function's purpose, input, and expected output.

This software is designed to be simple and efficient, with no additional setup required beyond having Python installed. Enjoy analyzing your text for boredom!
```