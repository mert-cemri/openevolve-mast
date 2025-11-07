# Anti-Shuffle User Manual

Welcome to the Anti-Shuffle software! This tool is designed to take a string and return an ordered version of it, where all words are rearranged such that their characters are in ascending order based on ASCII value. The order of words and spaces in the sentence is preserved.

## Main Functionality

The primary function of this software is `anti_shuffle`, which processes a given string and returns a new string with each word's characters sorted in ascending order.

### Example Usage

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

This software is implemented in Python and does not require any external dependencies. You can run it in any environment that supports Python.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required as there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script using the command:
   ```bash
   python main.py
   ```

4. You can modify the `main.py` file to test the `anti_shuffle` function with different input strings by changing the arguments in the `print` statements.

## Documentation

The `anti_shuffle` function is straightforward and does not require additional libraries or complex setup. The logic is encapsulated within the function, which splits the input string into words, sorts the characters in each word, and then reconstructs the sentence with the sorted words.

For further customization or integration into larger projects, you can import the `anti_shuffle` function from `main.py` into your own Python scripts.

Feel free to explore and modify the code to suit your needs. If you encounter any issues or have questions, please reach out to our support team.

Thank you for using Anti-Shuffle!