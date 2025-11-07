# Anti-Shuffle Function User Manual

Welcome to the user manual for the Anti-Shuffle function. This document will guide you through the main features of the software, how to set up the environment, and how to use the function effectively.

## Overview

The Anti-Shuffle function is a simple Python utility designed to reorder the characters of each word in a given string based on their ASCII values. The function maintains the original order of words and spaces in the sentence.

### Main Functionality

- **anti_shuffle(s):** This function takes a string `s` as input and returns a new string where each word's characters are sorted in ascending order based on their ASCII values. The order of words and spaces in the input string is preserved.

#### Examples

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

To use the Anti-Shuffle function, you need to have Python installed on your machine. The function does not require any additional dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed:** You can download Python from the [official website](https://www.python.org/downloads/).

2. **Clone or download the repository:** You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory:**

   ```bash
   cd <project-directory>
   ```

## Usage

To use the Anti-Shuffle function, follow these steps:

1. **Open the main.py file:** This file contains the implementation of the `anti_shuffle` function.

2. **Call the function:** You can call the `anti_shuffle` function with your desired string as an argument.

   ```python
   # Example usage
   print(anti_shuffle('Hi'))  # Output: 'Hi'
   print(anti_shuffle('hello'))  # Output: 'ehllo'
   print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
   ```

3. **Run the script:** Execute the script to see the output.

   ```bash
   python main.py
   ```

## Conclusion

The Anti-Shuffle function is a straightforward tool for reordering characters within words of a string. It is easy to set up and use, requiring only a basic Python environment. We hope this manual helps you get the most out of the Anti-Shuffle function. If you have any questions or need further assistance, please feel free to reach out.