# Words in Sentence

This software module provides functionality to filter words in a sentence based on the length of the words being prime numbers. It is a simple Python application that processes a given sentence and returns words whose lengths are prime numbers.

## Main Functions

### `is_prime(n)`

- **Purpose**: Checks if a number is a prime number.
- **Parameters**: 
  - `n` (int): The integer to check for primality.
- **Returns**: 
  - `True` if `n` is a prime number, `False` otherwise.

### `words_in_sentence(sentence)`

- **Purpose**: Processes a given sentence and returns a string containing words whose lengths are prime numbers.
- **Parameters**: 
  - `sentence` (str): A string representing a sentence with words separated by spaces.
- **Returns**: 
  - A string containing words from the original sentence whose lengths are prime numbers, maintaining the original order.

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. Follow these steps to set up your environment:

1. **Install Python**: 
   - Download and install Python from the official website: [Python.org](https://www.python.org/downloads/).

2. **Clone the Repository**:
   - Clone the repository containing the `main.py` file to your local machine.

3. **Install Dependencies**:
   - This project does not have any external dependencies, so no additional installations are required.

## Usage

To use the `words_in_sentence` function, follow these steps:

1. **Open a Terminal**:
   - Navigate to the directory where `main.py` is located.

2. **Run Python Interpreter**:
   - Start the Python interpreter by typing `python` in the terminal.

3. **Import the Function**:
   - Import the `words_in_sentence` function by executing:
     ```python
     from main import words_in_sentence
     ```

4. **Call the Function**:
   - Call the `words_in_sentence` function with a sentence of your choice:
     ```python
     result = words_in_sentence("This is a test")
     print(result)  # Output: "is"
     ```

5. **Example Usage**:
   - You can test the function with different sentences:
     ```python
     print(words_in_sentence("lets go for swimming"))  # Output: "go for"
     ```

## Conclusion

This software provides a simple yet effective way to filter words in a sentence based on prime number lengths. It is easy to use and does not require any additional dependencies, making it a lightweight solution for text processing tasks.