# Words in Sentence

This software module provides a function to extract words from a sentence where the length of each word is a prime number. It is designed to be simple and efficient, with no external dependencies required.

## Main Functions

The main function provided by this module is `words_in_sentence(sentence)`. This function takes a sentence as input and returns a string containing the words from the original sentence whose lengths are prime numbers, maintaining the original order.

### Function Details

- **`words_in_sentence(sentence)`**:
  - **Input**: A string `sentence` representing a sentence with words separated by spaces.
  - **Output**: A string containing words with prime lengths, in the original order.
  - **Example**:
    - Input: `"This is a test"`
    - Output: `"is"`

## Installation

This module does not require any external dependencies, making it easy to use without additional setup. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the module**: Obtain the `main.py` file containing the function.

## How to Use

1. **Import the function**: Ensure the `main.py` file is in your working directory or adjust your Python path accordingly.

2. **Call the function**: Use the `words_in_sentence(sentence)` function by passing a sentence string as an argument.

### Example Usage

```python
# Import the function from the module
from main import words_in_sentence

# Example sentences
sentence1 = "This is a test"
sentence2 = "lets go for swimming"

# Get words with prime lengths
result1 = words_in_sentence(sentence1)
result2 = words_in_sentence(sentence2)

# Print the results
print(result1)  # Output: "is"
print(result2)  # Output: "go for"
```

## Additional Information

- **Prime Number Check**: The module includes an internal helper function `is_prime(n)` to determine if a number is prime. This function is used to filter words based on their lengths.

- **Constraints**: The input sentence should only contain letters and spaces, with a length between 1 and 100 characters.

This module is designed to be straightforward and efficient, providing a simple utility for filtering words based on prime lengths. Enjoy using it in your projects!