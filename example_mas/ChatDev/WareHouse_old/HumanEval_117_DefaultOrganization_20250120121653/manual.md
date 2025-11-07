manual.md

```
# Select Words by Consonant Count

This software provides a function to extract words from a given string that contain exactly a specified number of consonants. It is designed to be simple and efficient, focusing solely on the task of word selection based on consonant count.

## Main Functionality

The core functionality of this software is encapsulated in the `select_words` function. This function takes two inputs:
- A string `s` which contains words separated by spaces.
- A natural number `n` which specifies the exact number of consonants a word must have to be included in the result.

The function returns a list of words from the string `s` that contain exactly `n` consonants, preserving the order in which they appear in the string.

### Example Usage

```python
# Example usage of the select_words function
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))     # Output: []
print(select_words("Hello world", 4))            # Output: ["world"]
print(select_words("Uncle sam", 3))              # Output: ["Uncle"]
```

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. The function does not require any external libraries, so there are no additional dependencies to install.

### Quick Start

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.
2. **Run the Script**: You can run the script directly using Python to test the function with your own inputs.

```bash
python main.py
```

## How to Use

1. **Prepare Your Input**: Ensure your input string contains only letters and spaces.
2. **Call the Function**: Use the `select_words` function by passing your string and the desired number of consonants as arguments.
3. **Interpret the Output**: The function will return a list of words that meet the criteria.

## Additional Information

- The function assumes that the input string contains only alphabetic characters and spaces.
- If the input string is empty, the function will return an empty list.
- The function is case-insensitive with respect to vowels and consonants.

This software is designed to be straightforward and efficient, making it easy to integrate into larger projects or use as a standalone tool for text processing tasks.
```