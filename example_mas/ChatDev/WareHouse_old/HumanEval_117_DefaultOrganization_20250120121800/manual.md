manual.md

```
# Select Words by Consonant Count

## Overview

The "Select Words by Consonant Count" software is a Python-based utility designed to extract words from a given string that contain a specified number of consonants. This tool is particularly useful for text analysis and linguistic research, where understanding the consonant structure of words is necessary.

## Main Functionality

The core functionality of this software is encapsulated in the `select_words` function. This function takes two inputs:
- A string `s` which contains words separated by spaces.
- A natural number `n` which specifies the exact number of consonants a word must have to be included in the output list.

The function returns a list of words from the input string that contain exactly `n` consonants, preserving the order in which they appear in the string.

### Example Usage

```python
# Example 1
result = select_words("Mary had a little lamb", 4)
print(result)  # Output: ["little"]

# Example 2
result = select_words("Hello world", 4)
print(result)  # Output: ["world"]
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script**:
   Since there are no external dependencies, you can directly run the script using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Prepare Your Input**: Ensure your input string contains only letters and spaces. The function assumes this format and does not handle punctuation or numbers.

2. **Call the Function**: Use the `select_words` function with your desired string and consonant count.

3. **Interpret the Results**: The function will return a list of words that match the specified consonant count. If no words match, it will return an empty list.

## Documentation

For further details and examples, refer to the in-line comments within the `main.py` file. This will provide additional context on how the function operates and its expected inputs and outputs.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you make the most of this software.

```