# Prime Length Words Extractor

This software provides a function to extract words from a given sentence whose lengths are prime numbers. It is a simple utility that can be used in various applications where filtering words based on their length is required.

## Main Functionality

The main function of this software is `words_in_sentence(sentence)`, which takes a sentence as input and returns a string containing only the words whose lengths are prime numbers. The order of the words in the output string is the same as in the original sentence.

### Example Usage

- **Input:** "This is a test"
- **Output:** "is"

- **Input:** "lets go for swimming"
- **Output:** "go for"

## Installation

This software does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository:**
   - Clone or download the repository containing the `main.py` file.

3. **Run the Code:**
   - Navigate to the directory containing `main.py` and run the script using Python.

## How to Use

1. **Prepare Your Environment:**
   - Open a terminal or command prompt.

2. **Navigate to the Directory:**
   - Use `cd` to navigate to the directory where `main.py` is located.

3. **Run the Script:**
   - Execute the script by running `python main.py` in the terminal.

4. **Use the Function:**
   - You can call the `words_in_sentence(sentence)` function within the script or import it into another Python script to use it with different sentences.

## Example Code

Here is an example of how you can use the function in a Python script:

```python
from main import words_in_sentence

sentence = "This is a test"
result = words_in_sentence(sentence)
print(result)  # Output: "is"

sentence = "lets go for swimming"
result = words_in_sentence(sentence)
print(result)  # Output: "go for"
```

## Conclusion

This software provides a straightforward utility to filter words based on prime number lengths. It is easy to integrate into larger projects or use as a standalone tool for text processing tasks.