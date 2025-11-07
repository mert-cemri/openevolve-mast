# Words in Sentence

This software provides a function to extract words from a sentence whose lengths are prime numbers. It is designed to process a given sentence and return a string containing only the words whose lengths are prime numbers, maintaining the original order.

## Main Functions

### `words_in_sentence(sentence)`

- **Description**: This function takes a sentence as input and returns a string of words whose lengths are prime numbers.
- **Input**: A string `sentence` containing words separated by spaces.
- **Output**: A string containing words from the input sentence whose lengths are prime numbers.

### `is_prime(n)`

- **Description**: This helper function checks if a given number `n` is a prime number.
- **Input**: An integer `n`.
- **Output**: Returns `True` if `n` is a prime number, otherwise returns `False`.

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is Installed**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, download the `main.py` file.

3. **Run the Code**: You can run the code directly using Python.

## How to Use

1. **Prepare Your Environment**: Ensure Python is installed and set up on your machine.

2. **Run the Function**: You can use the `words_in_sentence` function by importing it into your Python script or running it directly in an interactive Python session.

### Example Usage

```python
# Import the function from the module
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

The code is self-contained and does not require additional documentation beyond this manual. The logic for determining prime numbers is implemented in the `is_prime` function, and the main functionality is provided by the `words_in_sentence` function.

For any further questions or support, please contact the development team at ChatDev.