# Anti-Shuffle User Manual

Welcome to the Anti-Shuffle software! This tool is designed to take a string and return an ordered version of it. The ordered version of the string is created by rearranging all characters in each word in ascending order based on their ASCII values, while preserving the order of words and spaces in the sentence.

## Main Functionality

The main function provided by this software is `anti_shuffle`, which processes a given string to produce an ordered version of it. Here is a brief overview of its functionality:

- **Input**: A string containing words and spaces.
- **Output**: A string where each word's characters are sorted in ascending order based on ASCII values, with the original order of words and spaces preserved.

### Examples

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `anti_shuffle` function.

3. **Run the script**: You can execute the script directly using Python.

## How to Use

1. **Open a terminal or command prompt**.

2. **Navigate to the directory containing `main.py`**.

3. **Run the Python script**: Use the following command to execute the script and test the `anti_shuffle` function:

   ```bash
   python main.py
   ```

4. **Call the `anti_shuffle` function**: You can modify the `main.py` file to include test cases or use an interactive Python shell to call the function with different input strings.

## Documentation

For further details on using the `anti_shuffle` function, please refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into other Python projects.

We hope you find the Anti-Shuffle software useful for your text processing needs! If you have any questions or feedback, please feel free to reach out.