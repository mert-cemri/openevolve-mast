manual.md

```
# Boredom Counter

A simple Python function to count the number of sentences starting with the word "I" in a given string. This function is useful for text analysis where identifying specific sentence patterns is required.

## Quick Install

This software does not require any external dependencies, so you can run it directly with Python installed on your system. Ensure you have Python installed by running:

```bash
python --version
```

If Python is not installed, you can download it from [Python's official website](https://www.python.org/downloads/).

## 🤔 What is this?

The `is_bored` function is designed to analyze a string of text and count how many sentences start with the word "I". Sentences are considered to be delimited by '.', '?' or '!'. This can be particularly useful in text processing tasks where identifying specific sentence structures is necessary.

### Main Function

- **is_bored(S)**: Takes a string `S` as input and returns the count of sentences starting with the word "I".

### Example Usage

```python
from main import is_bored

# Example 1
text1 = "Hello world"
print(is_bored(text1))  # Output: 0

# Example 2
text2 = "The sky is blue. The sun is shining. I love this weather"
print(is_bored(text2))  # Output: 1
```

## 📖 Documentation

### Function Details

- **is_bored(S)**:
  - **Parameters**: 
    - `S` (str): A string containing sentences delimited by '.', '?' or '!'.
  - **Returns**: 
    - `int`: The number of sentences starting with the word "I".

### How to Use

1. Ensure Python is installed on your system.
2. Save the provided code in a file named `main.py`.
3. Import the `is_bored` function from `main.py` in your Python script.
4. Call the `is_bored` function with a string input to get the count of sentences starting with "I".

This function is straightforward and does not require any additional setup or dependencies. Simply integrate it into your Python projects where needed.
```