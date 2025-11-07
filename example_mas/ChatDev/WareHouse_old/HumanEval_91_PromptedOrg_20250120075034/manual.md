manual.md

```
# Boredom Counter

A simple Python application to count the number of "boredoms" in a given string. A "boredom" is defined as a sentence that starts with the word "I". Sentences are delimited by '.', '?' or '!'.

## Quick Install

This application does not require any external dependencies, so you can run it with a standard Python environment.

## 🤔 What is this?

The Boredom Counter is a utility function that processes a string of text and counts how many sentences start with the word "I". This can be useful for text analysis or natural language processing tasks where identifying specific sentence patterns is necessary.

## 📖 How to Use

### Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py` using your command line interface.

### Running the Application

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the script using Python:

   ```bash
   python main.py
   ```

4. You can modify the example usage in the `main.py` file to test with different strings:

   ```python
   print(is_bored("Hello world"))  # Output: 0
   print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
   ```

### Function Details

- **Function Name:** `is_bored(S)`
  
- **Parameters:** 
  - `S` (str): A string of text containing one or more sentences.

- **Returns:** 
  - An integer representing the number of sentences that start with the word "I".

- **Example Usage:**

  ```python
  print(is_bored("I am happy. You are here. I love coding!"))  # Output: 2
  ```

### Notes

- The function uses regular expressions to split the input string into sentences based on the delimiters '.', '?', and '!'.
- It then checks each sentence to see if it starts with the word "I" and counts such occurrences.

This simple utility can be integrated into larger text processing pipelines or used as a standalone tool for specific text analysis tasks.
```