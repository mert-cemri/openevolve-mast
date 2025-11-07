# is_bored Function User Manual

## Introduction

The `is_bored` function is a simple Python utility designed to analyze a string of text and count the number of sentences that start with the word "I". This function can be useful in text analysis tasks where identifying specific sentence patterns is required.

## Main Functionality

- **is_bored(S)**: This function takes a single argument, `S`, which is a string containing one or more sentences. It returns an integer representing the number of sentences that start with the word "I". Sentences are considered to be delimited by the characters '.', '?', or '!'.

## Installation

The `is_bored` function does not require any external dependencies beyond Python itself. Therefore, no additional installation steps are necessary. Ensure you have Python installed on your system.

## How to Use

1. **Prepare Your Environment**:
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Code**:
   - Copy the provided `is_bored` function code into a file named `main.py`.

3. **Run the Function**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the Python script using the command:
     ```bash
     python main.py
     ```
   - You can test the function by calling it with different strings. For example:
     ```python
     print(is_bored("The sky is blue. The sun is shining. I love this weather"))
     ```
   - This will output `1`, as there is one sentence starting with "I".

## Example Usage

Here is an example of how to use the `is_bored` function in a Python script:

```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    import re
    sentences = re.split(r'[.?!]', S)
    boredom_count = sum(1 for sentence in sentences if sentence.strip().startswith('I'))
    return boredom_count

# Example usage
text = "I am happy. Are you? I think we should go!"
print(is_bored(text))  # Output: 2
```

## Conclusion

The `is_bored` function is a straightforward tool for counting sentences that start with "I" in a given text. With no external dependencies, it is easy to integrate into larger projects or use as a standalone utility for text analysis tasks.