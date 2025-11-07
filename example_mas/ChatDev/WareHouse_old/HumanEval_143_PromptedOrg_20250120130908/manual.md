# Prime Length Words Filter

This software module provides a function to filter words in a sentence based on the length of the words being prime numbers. It is designed to process a given sentence and return a string containing only those words whose lengths are prime numbers.

## Main Functionality

The primary function of this module is `words_in_sentence(sentence)`, which takes a sentence as input and returns a string of words from the original sentence whose lengths are prime numbers. The order of the words in the returned string is the same as in the original sentence.

### Key Functions

1. **is_prime(n)**: 
   - Checks if a given number `n` is a prime number.
   - Returns `True` if `n` is a prime number, `False` otherwise.

2. **words_in_sentence(sentence)**:
   - Splits the input sentence into words.
   - Filters words whose lengths are prime numbers using the `is_prime` function.
   - Returns a string of these words, maintaining their original order.

## Installation

This module does not require any external dependencies. It is implemented using standard Python libraries.

### Quick Install

Since there are no external dependencies, you can directly use the module in your Python environment. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Module**: You can use the module in your Python scripts or interactively in a Python shell.

### Example Usage

```python
from main import words_in_sentence

# Example 1
sentence1 = "This is a test"
result1 = words_in_sentence(sentence1)
print(result1)  # Output: "is"

# Example 2
sentence2 = "lets go for swimming"
result2 = words_in_sentence(sentence2)
print(result2)  # Output: "go for"
```

## Documentation

For further details on the implementation and usage, refer to the comments within the `main.py` file. The code is self-explanatory with inline comments explaining the logic behind checking for prime numbers and filtering words based on their lengths.

Feel free to modify and extend the functionality as per your requirements. The module is designed to be simple and efficient, focusing on the core task of filtering words by prime length.