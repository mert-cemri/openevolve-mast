manual.md

```
# Word Selector

A Python-based application to select words from a given string that contain exactly a specified number of consonants.

## Overview

The Word Selector application provides a simple function, `select_words`, that processes a string and returns a list of words containing exactly a specified number of consonants. This tool can be useful for text analysis, linguistic studies, or any application where filtering words by consonant count is necessary.

## Main Functionality

### `select_words(s, n)`

- **Description**: This function takes a string `s` and a natural number `n`, and returns a list of words from the string that contain exactly `n` consonants.
- **Parameters**:
  - `s` (str): The input string containing words separated by spaces.
  - `n` (int): The exact number of consonants a word must have to be included in the result.
- **Returns**: A list of words from the input string that contain exactly `n` consonants. If no such words exist, it returns an empty list.

### Example Usage

```python
# Example usage:
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))     # Output: []
print(select_words("Hello world", 4))            # Output: ["world"]
print(select_words("Uncle sam", 3))              # Output: ["Uncle"]
```

## Installation

### Requirements

This application does not require any external Python packages. It only uses Python's built-in capabilities.

### Setting Up the Environment

1. **Python Installation**: Ensure that you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the Script**: You can run the script directly using Python:
   ```bash
   python main.py
   ```

## Usage

To use the `select_words` function, simply import it into your Python script and call it with the desired string and consonant count. Ensure that your input string contains only letters and spaces to avoid unexpected behavior.

```python
from main import select_words

result = select_words("Your input string here", 3)
print(result)
```

## Conclusion

The Word Selector application is a straightforward tool for filtering words by consonant count. With no external dependencies, it is easy to set up and integrate into larger projects. Whether for educational purposes or practical applications, this tool provides a simple yet effective solution for word selection based on consonant count.
```