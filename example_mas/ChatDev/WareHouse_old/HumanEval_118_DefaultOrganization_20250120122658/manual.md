# ChatDev Software User Manual

## Introduction

Welcome to the ChatDev software solution for identifying the closest vowel between two consonants in a given word. This software is designed to process a string of English letters and return the closest vowel that stands between two consonants from the right side of the word. This tool is useful for linguistic analysis and text processing tasks.

## Main Function

The core function of this software is `get_closest_vowel(word)`. This function takes a single argument, `word`, which is a string of English letters. It returns the closest vowel that is situated between two consonants from the right side of the word. If no such vowel exists, it returns an empty string.

### Function Details

- **Input**: A string `word` containing English letters only.
- **Output**: A single character string representing the closest vowel between two consonants, or an empty string if no such vowel exists.

### Example Usage

```python
get_closest_vowel("yogurt")  # Returns "u"
get_closest_vowel("FULL")    # Returns "U"
get_closest_vowel("quick")   # Returns ""
get_closest_vowel("ab")      # Returns ""
```

## Installation

To use this software, you need to have Python installed on your system. The function does not require any additional dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: You can clone the repository using Git or download the ZIP file and extract it.

3. **Navigate to the project directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open the `main.py` file**: You can use any text editor or IDE of your choice.

2. **Call the `get_closest_vowel` function**: Pass the word you want to analyze as an argument to the function.

3. **Run the script**: Execute the script in your terminal or command prompt using the command `python main.py`.

4. **View the result**: The function will return the closest vowel between two consonants from the right side of the word.

## Documentation

For further details on the function and its usage, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the function.

## Support

If you encounter any issues or have questions about the software, please feel free to reach out to our support team at support@chatdev.com. We are here to assist you with any inquiries you may have.

Thank you for choosing ChatDev for your text processing needs!