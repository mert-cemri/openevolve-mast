manual.md

```
# Select Words by Consonant Count

## Introduction

The `select_words` function is a Python utility designed to extract words from a given string that contain exactly a specified number of consonants. This tool is particularly useful for text analysis tasks where consonant patterns are of interest.

## Main Functionality

- **Function Name:** `select_words`
- **Purpose:** Returns a list of words from a given string that contain exactly a specified number of consonants.
- **Input:**
  - `s`: A string containing words separated by spaces. The string is assumed to contain only letters and spaces.
  - `n`: A natural number representing the exact number of consonants a word must have to be included in the result.
- **Output:** A list of words from the input string `s` that contain exactly `n` consonants, in the order they appear in the string.

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/).

## How to Use

1. **Set Up Your Environment:**

   Ensure you have Python installed. You can verify your installation by running the following command in your terminal or command prompt:

   ```bash
   python --version
   ```

   If Python is installed, this command will return the version number.

2. **Using the Function:**

   - Save the provided code into a file named `main.py`.
   - You can then use the function by importing it into your Python script or by directly calling it in the Python interactive shell.

   Example usage:

   ```python
   from main import select_words

   result = select_words("Mary had a little lamb", 4)
   print(result)  # Output: ["little"]

   result = select_words("Hello world", 4)
   print(result)  # Output: ["world"]
   ```

3. **Running the Function:**

   You can run the function in a Python environment by executing the script or by using an interactive Python shell.

   ```bash
   python main.py
   ```

   Ensure that you modify the script to include test cases or interactive input as needed.

## Additional Notes

- The function assumes that the input string contains only letters and spaces. It does not handle punctuation or special characters.
- The function is case-insensitive with respect to consonants, meaning it treats uppercase and lowercase consonants equally.

This utility is simple yet effective for tasks involving text processing where consonant patterns are of interest. Feel free to integrate it into larger projects or use it as a standalone tool for specific text analysis tasks.
```