# Boredom Counter

This software provides a simple function to count the number of "boredoms" in a given string. A boredom is defined as a sentence that starts with the word "I". Sentences are delimited by '.', '?' or '!'.

## Main Function

The main function of this software is `is_bored(S)`, which takes a string `S` as input and returns the number of sentences that start with the word "I".

### Example Usage

```python
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
```

## Installation

This software does not require any external dependencies, so you can run it in any standard Python environment. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Navigate to the directory** where `main.py` is located.

3. **Run the script** using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Open the `main.py` file** in a text editor or IDE of your choice.

2. **Modify the input string** in the `print` statements at the bottom of the file to test different cases.

3. **Run the script** to see the output, which will be the count of sentences starting with "I".

## Documentation

The function `is_bored(S)` is documented within the code itself. The docstring provides a brief overview of its purpose and usage.

### Function Definition

```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
```

### Implementation Details

- The function uses regular expressions to split the input string into sentences based on the delimiters '.', '?', and '!'.
- It then iterates over each sentence, stripping leading and trailing whitespace.
- If a sentence starts with "I", it increments the boredom count.
- Finally, it returns the total count of boredoms.

This software is designed to be simple and efficient, providing a straightforward solution to the task of counting specific sentence types in a text.