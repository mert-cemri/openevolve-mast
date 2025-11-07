# Anti-Shuffle User Manual

Welcome to the Anti-Shuffle software, a simple yet effective tool for rearranging characters in words to create an ordered version of a string. This manual will guide you through the main functions of the software, how to install necessary dependencies, and how to use the software effectively.

## Main Functions

The primary function of this software is `anti_shuffle`, which takes a string as input and returns an ordered version of it. The ordered version of the string is such that all words (separated by spaces) are replaced by new words where all the characters are arranged in ascending order based on ASCII value. The order of words and blank spaces in the sentence are preserved.

### Example Usage

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

### Environment Setup

To use the Anti-Shuffle software, you need to have Python installed on your system. This software does not require any additional dependencies, so you can directly run the Python script.

### Quick Install

1. **Install Python**: If you haven't already, download and install Python from the official website: [python.org](https://www.python.org/).

2. **Clone the Repository**: Download the `main.py` file containing the `anti_shuffle` function.

3. **Run the Script**: You can run the script directly using Python. Navigate to the directory containing `main.py` and execute the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

## How to Use

1. **Open the Script**: Open `main.py` in a text editor or IDE of your choice.

2. **Modify Input**: You can modify the input string in the `if __name__ == "__main__":` block to test different strings.

3. **Run the Script**: Execute the script to see the output of the `anti_shuffle` function.

4. **Integrate into Your Project**: You can copy the `anti_shuffle` function into your own Python projects to use it as needed.

## Documentation

For further information on Python and its capabilities, please refer to the official Python documentation: [Python Documentation](https://docs.python.org/3/).

This concludes the user manual for the Anti-Shuffle software. If you have any questions or require further assistance, please feel free to reach out to our support team. Happy coding!